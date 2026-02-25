from typing import Any
import os
import argparse
import json
import time
import orjson
from pathlib import Path
from supermemory import Supermemory
from model import (
    SOExtractContractList,
    SOUpdateContractList,
)
from mem0 import MemoryClient
from openai import OpenAI
from anthropic import AnthropicVertex
import instructor
from base_utils import OPENAI_API_KEY, OPENAI_MODEL, logger
from test_utils import (
    BATCH_SIZE,
    _batch_messages,
    customer_info,
    format_contract_summary,
    generic_deal_terms,
    get_contract_generation_prompt,
    team_info,
)
from dotenv import load_dotenv

load_dotenv("../.env")


# --- CONFIGURATION ---
MEM0_API_KEY = os.getenv("MEM0_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Vertex AI (Google Cloud) — used for Claude on Vertex
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
VERTEX_REGION = (
    os.getenv("GOOGLE_CLOUD_LOCATION") or os.getenv("VERTEX_REGION") or "global"
)
API_KEY = os.getenv("SUPERMEMORY_KEY")
BASE_URL = "https://api.supermemory.ai/"
DEFAULT_USER_ID = "1_gemini"


# OpenAI model shorthands and full names
OPENAI_MODELS = {
    "4.1": "gpt-4.1-2025-04-14",
    "5.2": "gpt-5.2-2025-12-11",
    "5-mini": "gpt-5-mini-2025-08-07",
    "default": OPENAI_MODEL,
}

# Vertex AI model IDs for Claude on GCP (see https://docs.anthropic.com/en/api/claude-on-vertex-ai)
ANTHROPIC_MODELS = {
    "default": "claude-sonnet-4-5@20250929",
    "sonnet-4-5": "claude-sonnet-4-5@20250929",
    "sonnet-4-6": "claude-sonnet-4-6",
    "opus-4-5": "claude-opus-4-5@20251101",
    "opus-4-6": "claude-opus-4-6",
}

# Gemini: instructor expects "google/<model-code>". Valid API model codes include
# gemini-3-flash-preview, gemini-3-pro-preview, gemini-2.5-flash, gemini-2.0-flash.
# Stable model; use --gemini-model gemini-3-flash-preview for preview if available
DEFAULT_GEMINI_MODEL = "google/gemini-2.5-pro"


def _get_openai_client():
    return instructor.from_openai(OpenAI(api_key=OPENAI_API_KEY))


def _get_gemini_client(model: str):
    """Model must be 'google/gemini-*' for instructor.from_provider."""
    return instructor.from_provider(model)


def _get_anthropic_client():
    """Patched AnthropicVertex client for Claude on Vertex AI; structured output via instructor (Mode.TOOLS)."""
    if not GOOGLE_CLOUD_PROJECT:
        raise ValueError(
            "GOOGLE_CLOUD_PROJECT must be set for Claude on Vertex AI. "
            "Set env GOOGLE_CLOUD_PROJECT (and optionally GOOGLE_CLOUD_LOCATION or VERTEX_REGION, default 'global')."
        )
    vertex_client = AnthropicVertex(
        project_id=GOOGLE_CLOUD_PROJECT,
        region=VERTEX_REGION,
    )
    return instructor.from_anthropic(
        vertex_client,
        mode=instructor.Mode.ANTHROPIC_JSON,
    )


def get_openai_response(
    prompt: str,
    is_update: bool = False,
    model: str | None = None,
) -> SOExtractContractList | SOUpdateContractList:
    model = model or OPENAI_MODEL
    openai_api = _get_openai_client()
    try:
        logger.info(
            f"get_openai_response::0:: Sending Prompt:: prompt={prompt[:200]}..., model={model}"
        )
        response = openai_api.chat.completions.create(
            model=model,
            response_model=SOExtractContractList
            if not is_update
            else SOUpdateContractList,
            messages=[{"role": "user", "content": prompt}],
        )
        return response
    except Exception as e:
        logger.exception(f"get_openai_response::3:: Error during OpenAI processing {e}")
        raise ValueError(e) from e


def _normalize_gemini_model(name: str) -> str:
    """Ensure model is in form 'google/gemini-*' for instructor."""
    name = (name or "").strip()
    if not name:
        return DEFAULT_GEMINI_MODEL
    if not name.startswith("google/"):
        return f"google/{name}"
    return name


def _gemini_model_for_api(instructor_model: str) -> str:
    """Return model id for google-genai API. SDK builds path as models/{model} - no 'google/' prefix."""
    if not instructor_model:
        return DEFAULT_GEMINI_MODEL.split("/", 1)[-1]
    return (
        instructor_model.split("/", 1)[-1]
        if "/" in instructor_model
        else instructor_model
    )


def get_gemini_response(
    prompt: str,
    is_update: bool = False,
    model: str | None = None,
) -> SOExtractContractList | SOUpdateContractList:
    model = _normalize_gemini_model(model or DEFAULT_GEMINI_MODEL)
    api_model = _gemini_model_for_api(model)
    gemini_api = _get_gemini_client(model)
    try:
        logger.info(
            "get_gemini_response::0:: Sending Prompt (Gemini) model=%s", api_model
        )
        response = gemini_api.chat.completions.create(
            model=api_model,
            response_model=SOExtractContractList
            if not is_update
            else SOUpdateContractList,
            messages=[{"role": "user", "content": prompt}],
        )
        return response
    except Exception as e:
        logger.exception(
            "get_gemini_response::3:: Error during Gemini processing %s", e
        )
        raise ValueError(e) from e


def _resolve_anthropic_model(name: str | None) -> str:
    """Resolve shorthand to Vertex AI Claude model id (e.g. claude-sonnet-4-5@20250929)."""
    name = (name or "default").strip()
    return ANTHROPIC_MODELS.get(name, name)


def get_anthropic_response(
    prompt: str,
    is_update: bool = False,
    model: str | None = None,
) -> SOExtractContractList | SOUpdateContractList:
    model_id = _resolve_anthropic_model(model)
    client = _get_anthropic_client()
    response_model = SOExtractContractList if not is_update else SOUpdateContractList
    try:
        logger.info(
            "get_anthropic_response::0:: Sending Prompt (Claude on Vertex) model=%s",
            model_id,
        )
        response = client.messages.create(
            model=model_id,
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
            response_model=response_model,
        )
        return response
    except Exception as e:
        logger.exception(
            "get_anthropic_response::3:: Error during Claude (Vertex) processing %s", e
        )
        raise ValueError(e) from e


def load_chat_messages(chat_path: str) -> list[dict[str, Any]]:
    """Load messages from a JSON chat file. Path can be absolute or relative to this script's dir."""
    path = Path(chat_path)
    if not path.is_absolute():
        path = Path(__file__).resolve().parent / path
    if not path.exists():
        raise FileNotFoundError(f"Chat file not found: {path}")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "messages" in data:
        return data["messages"]
    raise ValueError(
        f"Chat file must be a JSON array or an object with 'messages' key: {path}"
    )


def _chat_to_mem0_messages(conversation: list[dict[str, Any]]) -> list[dict[str, str]]:
    """Convert chat messages (from_whom, body) to Mem0 format (role, content).
    Mem0 expects: [{"role": "user"|"assistant", "content": "..."}].
    Maps (TEAM2) -> user, (TEAM1) -> assistant; others -> assistant. Skips (CONTEXT).
    """
    mem0_messages: list[dict[str, str]] = []
    for m in conversation:
        from_whom = (m.get("from_whom") or "").strip()
        body = (m.get("body") or "").strip()
        if not body or from_whom == "(CONTEXT)":
            continue
        role = "assistant"
        if "(TEAM2)" in from_whom.upper():
            role = "user"
        elif "(TEAM1)" in from_whom.upper():
            role = "assistant"
        mem0_messages.append({"role": role, "content": body})
    return mem0_messages


def main():
    parser = argparse.ArgumentParser(
        description="Test Contract Parsing with LLM (openai/gemini/claude) and optional Memory (mem0/supermemory). Messages are always batched before adding to memory."
    )
    parser.add_argument(
        "--llm",
        choices=["gemini", "openai", "claude"],
        default="openai",
        help="LLM to use for contract extraction. Default: openai",
    )
    parser.add_argument(
        "--model",
        default="default",
        metavar="NAME",
        help="OpenAI model: shorthand (4o, 4.1, 5.2, 5-mini) or full model name. Only used when --llm openai. Default: default (from env)",
    )
    parser.add_argument(
        "--gemini-model",
        default=None,
        metavar="NAME",
        help="Gemini model (e.g. gemini-2.5-flash, gemini-3-flash-preview, gemini-2.0-flash). Only used when --llm gemini. Default: gemini-2.5-flash",
    )
    parser.add_argument(
        "--claude-model",
        default="default",
        metavar="NAME",
        help="Claude on Vertex: shorthand (default, sonnet-4-5, sonnet-4-6, opus-4-5, opus-4-6, haiku-4-5) or Vertex model id. Only used when --llm claude. Requires GOOGLE_CLOUD_PROJECT. Default: default",
    )
    parser.add_argument(
        "--memory",
        choices=["none", "mem0", "supermemory"],
        default="none",
        help="Memory backend: none, mem0, or supermemory. When set, messages are always batched (size %s) before adding. Default: none"
        % BATCH_SIZE,
    )
    parser.add_argument(
        "--chat",
        default="chats/single_product_single_shipment_simple.json",
        metavar="PATH",
        help="Path to JSON chat file (array of messages or object with 'messages' key). Default: chats/single_product_single_shipment_simple.json",
    )
    parser.add_argument(
        "--user-id",
        default=None,
        metavar="ID",
        help="User id for this run (container_tag / user_id when memory is used). If not set, uses default.",
    )
    parser.add_argument(
        "--results-file",
        default=None,
        metavar="PATH",
        help="Append run results (chat, mode, user_id, contract summary) to this file (e.g. Results.md).",
    )
    args = parser.parse_args()

    user_id = args.user_id if args.user_id is not None else DEFAULT_USER_ID

    full_conversation = load_chat_messages(args.chat)
    print(f"Loaded {len(full_conversation)} messages from {args.chat}")

    start_time = time.perf_counter()

    # --- Memory ---
    if args.memory == "supermemory":
        print(">> MEMORY: SUPERMEMORY (batched)")
        client = Supermemory(api_key=API_KEY, base_url=BASE_URL)
        batches = _batch_messages(full_conversation)
        for batch_idx, batch in enumerate(batches):
            mem_content = "\n".join(f"{m['from_whom']}: {m['body']}" for m in batch)
            first_ts = batch[0]["timestamp"]
            last_ts = batch[-1]["timestamp"]
            client.add(
                content=mem_content,
                container_tag=user_id,
                metadata={
                    "batch_index": batch_idx,
                    "batch_size": len(batch),
                    "ts_start": first_ts,
                    "ts_end": last_ts,
                },
            )
        print(
            f"   [Memory] Anchored {len(full_conversation)} messages in {len(batches)} batch(es) of up to {BATCH_SIZE} into {user_id}"
        )

        search_query = generic_deal_terms.strip()
        search_result = client.search.memories(q=search_query, limit=15)
        seen_content: set[Any] = set()
        context_parts = []
        if search_result and getattr(search_result, "results", None):
            for mem in search_result.results[:10]:
                mem_content = mem.get("content") if isinstance(mem, dict) else str(mem)
                if mem_content and mem_content not in seen_content:
                    seen_content.add(mem_content)
                    context_parts.append(mem_content)
        memory_context_body = (
            "[Relevant context from conversation memory]:\n" + "\n".join(context_parts)
            if context_parts
            else ""
        )
        if memory_context_body:
            context_message = {
                "from_whom": "(CONTEXT)",
                "body": memory_context_body,
                "timestamp": full_conversation[0]["timestamp"] - 1,
            }
            all_messages_for_llm = [context_message] + full_conversation
            print(
                f"   [Memory] Injected 1 context block ({len(context_parts)} items) + full conversation for LLM"
            )
        else:
            all_messages_for_llm = full_conversation

    elif args.memory == "mem0":
        print(">> MEMORY: MEM0 (batched)")
        mem0_client = MemoryClient(api_key=MEM0_API_KEY)
        batches = _batch_messages(full_conversation)
        for batch in batches:
            mem0_messages = _chat_to_mem0_messages(batch)
            if mem0_messages:
                mem0_client.add(messages=mem0_messages, user_id=user_id)
        print(
            f"   [Memory] Anchored {len(full_conversation)} messages in {len(batches)} batch(es) of up to {BATCH_SIZE} into {user_id}"
        )

        search_query = generic_deal_terms.strip()
        mem0_result = mem0_client.search(
            search_query, version="v2", filters={"user_id": user_id}
        )
        context_parts = []
        if mem0_result and mem0_result.get("results"):
            for mem in mem0_result["results"]:
                context_parts.append(mem.get("memory", mem))
        memory_context_body = "\n".join(context_parts)
        if memory_context_body:
            context_message = {
                "from_whom": "(CONTEXT)",
                "body": memory_context_body,
                "timestamp": full_conversation[0]["timestamp"] - 1,
            }
            all_messages_for_llm = [context_message] + full_conversation
            print(
                f"   [Memory] Injected 1 context block ({len(context_parts)} items) + full conversation for LLM"
            )
        else:
            all_messages_for_llm = full_conversation
    else:
        print(">> MEMORY: NONE")
        all_messages_for_llm = full_conversation

    # --- LLM call ---
    llm_label = args.llm
    if args.llm == "openai":
        model_name = OPENAI_MODELS.get(args.model, args.model)
        llm_label = f"openai ({model_name})"
    elif args.llm == "claude":
        claude_model = _resolve_anthropic_model(args.claude_model)
        llm_label = f"claude ({claude_model})"
    else:
        gemini_model = _normalize_gemini_model(
            args.gemini_model or DEFAULT_GEMINI_MODEL
        )
        llm_label = f"gemini ({gemini_model})"
    print(f">> LLM: {llm_label}")
    print(f"\nProcessing contract from {len(all_messages_for_llm)} messages...")
    print("=" * 60)

    prompt = get_contract_generation_prompt(
        messages=all_messages_for_llm,
        organization_info=team_info,
        customer_info=customer_info,
    )

    if args.llm == "gemini":
        summary = get_gemini_response(prompt, model=args.gemini_model)
    elif args.llm == "claude":
        summary = get_anthropic_response(prompt, model=args.claude_model)
    else:
        model_name = OPENAI_MODELS.get(args.model, args.model)
        summary = get_openai_response(prompt, model=model_name)

    print("\n" + "=" * 60)
    print("CONTRACT SUMMARY")
    print("=" * 60)
    summary_text = format_contract_summary(summary)
    print(summary_text)

    if args.results_file:
        elapsed = time.perf_counter() - start_time
        mode_name = f"{llm_label}"
        if args.memory != "none":
            mode_name += f" + memory ({args.memory}, batched)"
        else:
            mode_name += " (no memory)"
        chat_name = Path(args.chat).name
        results_path = Path(args.results_file)
        if not results_path.is_absolute():
            results_path = Path(__file__).resolve().parent / results_path
        with open(results_path, "a", encoding="utf-8") as f:
            f.write(f"\n## {chat_name} — {mode_name}\n\n")
            f.write(f"- **USER_ID**: `{user_id}`\n")
            f.write(f"- **Time taken**: {elapsed:.2f}s\n\n")
            f.write("### Contract summary\n\n```\n")
            f.write(summary_text)
            f.write("\n```\n\n")
            f.write("### Contract data (JSON)\n\n```json\n")
            f.write(
                orjson.dumps(summary.model_dump(), option=orjson.OPT_INDENT_2).decode(
                    "utf-8"
                )
            )
            f.write("\n```\n\n")
        print(f"\n>> Time taken: {elapsed:.2f}s — Appended results to {results_path}")


if __name__ == "__main__":
    main()


# Usage examples:
#
# LLM only (no memory):
#   python test_memory.py
#   python test_memory.py --llm openai --model 4o
#   python test_memory.py --llm openai --model 4.1
#   python test_memory.py --llm gemini
#   python test_memory.py --llm claude
#   python test_memory.py --llm claude --claude-model sonnet-4-6
#
# OpenAI with different models:
#   python test_memory.py --llm openai --model 4o
#   python test_memory.py --llm openai --model 5.2
#
# Memory (messages are always batched before adding):
#   python test_memory.py --memory supermemory
#   python test_memory.py --memory mem0
#   python test_memory.py --llm openai --memory supermemory
#   python test_memory.py --llm gemini --memory mem0
#
# Chat file and results:
#   python test_memory.py --chat chats/short.json
#   python test_memory.py --chat /path/to/chat.json --results-file Results.md --user-id my_user
