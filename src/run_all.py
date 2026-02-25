#!/usr/bin/env python3
"""
Run different models on selected chat(s) and/or email conversation(s).
Configure at the top: RUN_CHATS / RUN_EMAILS, CHAT_FILES (chats/), EMAIL_FILES (emails/).
Results are appended to a single MD file under md/results/.

Runs (chat, model, run) jobs in parallel in batches; each job writes to a temp file,
and the main process appends each result to the MD file as it completes.

Expected results per chat (for correctness comparison in summarize_results.py)
are defined in expected_results.py (key = chat filename, value = expected contract data).
"""

import subprocess
import sys
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

# Max time per iteration; skip (abort) if exceeded
ITERATION_TIMEOUT_SECONDS = 60


SCRIPT_DIR = Path(__file__).resolve().parent
CHATS_DIR = SCRIPT_DIR / "chats"
EMAILS_DIR = SCRIPT_DIR / "emails"
MD_DIR = SCRIPT_DIR / "md"
MD_RESULTS = MD_DIR / "results"

# Set to True to run tests on chat files; False to skip
RUN_CHATS = True
# Set to True to run tests on email conversation files (emails/ directory)
RUN_EMAILS = False

CHAT_FILES = [
    # "single_product_single_shipment_complex.json",
    # "single_product_single_shipment_medium.json",
    # "single_product_single_shipment_simple.json",
    # "multiple_product_multiple_shipment_complex.json",
    # "multiple_product_multiple_shipment_medium.json",
    # "multiple_product_multiple_shipment_simple.json",
    # "single_product_multiple_shipment_complex.json",
    # "single_product_multiple_shipment_medium.json",
    # "single_product_multiple_shipment_simple.json",
    # Real world messages test
    "real_world_msgs_test_v1.json",
    # "real_world_msgs_test_v2.json",
    # "real_world_msgs_test_v3.json",
]

# Email conversation files to test (from emails/ directory); used when RUN_EMAILS is True
EMAIL_FILES = [
    "single_product_single_shipment.json",
    "single_product_multiple_shipments.json",
    "multiple_products_multiple_shipments.json",
]

# Models to run for each chat/email
OPENAI_MODELS = [
    "default",
    "4.1",
    "5.2",
]
GEMINI_MODELS = ["gemini-2.5-pro", "gemini-2.5-flash", "gemini-3-flash-preview"]
ANTHROPIC_MODELS = ["sonnet-4-5", "sonnet-4-6", "opus-4-5", "opus-4-6"]

RUN_OPENAI = False
RUN_GEMINI = False
RUN_ANTHROPIC = True

# Runs per (chat, model) combination
NUM_RUNS = 1

# Number of (chat, model, run) jobs to run in parallel; each result is appended to the MD file as it completes
BATCH_SIZE = 10

# Output: results written to this file under md/results/
RESULTS_MD_FILE = "claude_2.md"

# Memory backend for test_memory.py (e.g. "supermemory"); set to None to omit --memory
MEMORY = None


def _ensure_md_dirs():
    MD_RESULTS.mkdir(parents=True, exist_ok=True)


def _run_one_test(
    llm: str,
    model_arg: str,
    model_value: str,
    run: int,
    chat_path: Path,
    results_file: Path,
) -> bool | None:
    user_id = f"{llm}_{model_value.replace('.', '_')}_run_{run}_new"
    cmd = [
        sys.executable,
        str(SCRIPT_DIR / "test_memory.py"),
        "--chat",
        str(chat_path),
        "--llm",
        llm,
        model_arg,
        model_value,
        "--user-id",
        user_id,
        "--results-file",
        str(results_file),
    ]
    if MEMORY is not None:
        cmd.extend(["--memory", MEMORY])
    try:
        result = subprocess.run(
            cmd, cwd=str(SCRIPT_DIR), timeout=ITERATION_TIMEOUT_SECONDS
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return None  # Caller treats as skip


def main():
    _ensure_md_dirs()

    if not RUN_CHATS and not RUN_EMAILS:
        print(
            "Enable at least one of RUN_CHATS or RUN_EMAILS.",
            file=sys.stderr,
        )
        sys.exit(1)
    if RUN_CHATS and not CHAT_FILES:
        print(
            "RUN_CHATS is True but CHAT_FILES is empty. Add at least one chat filename.",
            file=sys.stderr,
        )
        sys.exit(1)
    if RUN_EMAILS and not EMAIL_FILES:
        print(
            "RUN_EMAILS is True but EMAIL_FILES is empty. Add at least one email filename.",
            file=sys.stderr,
        )
        sys.exit(1)

    conversation_paths: list[Path] = []
    if RUN_CHATS:
        for name in CHAT_FILES:
            p = CHATS_DIR / name.strip()
            if not p.exists():
                print(f"Chat file not found: {p}", file=sys.stderr)
                sys.exit(1)
            conversation_paths.append(p)
    if RUN_EMAILS:
        for name in EMAIL_FILES:
            p = EMAILS_DIR / name.strip()
            if not p.exists():
                print(f"Email file not found: {p}", file=sys.stderr)
                sys.exit(1)
            conversation_paths.append(p)

    out_md = MD_RESULTS / RESULTS_MD_FILE

    # Write header (file is created fresh so we don't duplicate headers on re-runs)
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("# Model comparison — chats × models\n\n")
        if RUN_CHATS:
            chat_paths = [p for p in conversation_paths if p.parent == CHATS_DIR]
            f.write("**Chats:** " + ", ".join(f"`{p.name}`" for p in chat_paths) + "\n\n")
        if RUN_EMAILS:
            email_paths = [p for p in conversation_paths if p.parent == EMAILS_DIR]
            f.write("**Emails:** " + ", ".join(f"`{p.name}`" for p in email_paths) + "\n\n")
        models_line = []
        if RUN_OPENAI:
            models_line.append("OpenAI: " + ", ".join(OPENAI_MODELS))
        if RUN_GEMINI:
            models_line.append("Gemini: " + ", ".join(GEMINI_MODELS))
        if RUN_ANTHROPIC:
            models_line.append("Claude (Anthropic): " + ", ".join(ANTHROPIC_MODELS))
        f.write("**Models:** " + " | ".join(models_line) + "\n\n")
        f.write(f"**Runs per (chat, model):** {NUM_RUNS}\n\n---\n\n")

    # Build flat list of (llm, model_arg, model_value, run, conversation_path, label) for parallel runs
    jobs: list[tuple[str, str, str, int, Path, str]] = []
    for conv_path in conversation_paths:
        conv_name = conv_path.name
        for r in range(1, NUM_RUNS + 1):
            if RUN_OPENAI:
                for model in OPENAI_MODELS:
                    label = f"{conv_name} / OpenAI ({model}) run {r}"
                    jobs.append(("openai", "--model", model, r, conv_path, label))
            if RUN_GEMINI:
                for model in GEMINI_MODELS:
                    label = f"{conv_name} / Gemini ({model}) run {r}"
                    jobs.append(
                        ("gemini", "--gemini-model", model, r, conv_path, label)
                    )
            if RUN_ANTHROPIC:
                for model in ANTHROPIC_MODELS:
                    label = f"{conv_name} / Claude ({model}) run {r}"
                    jobs.append(
                        ("claude", "--claude-model", model, r, conv_path, label)
                    )

    total = len(jobs)
    failed: list[str] = []
    append_lock = threading.Lock()
    temp_dir = Path(tempfile.mkdtemp(prefix="run_all_"))

    def run_one_job(
        idx_job: tuple[int, tuple[str, str, str, int, Path, str]],
    ) -> tuple[int, str, bool | None, Path]:
        idx, (llm, model_arg, model_value, run, conv_path, label) = idx_job
        temp_file = temp_dir / f"result_{idx}.md"
        try:
            ok = _run_one_test(llm, model_arg, model_value, run, conv_path, temp_file)
        except Exception:
            ok = False
        return (idx, label, ok, temp_file)

    run_count = 0
    with ThreadPoolExecutor(max_workers=BATCH_SIZE) as executor:
        futures = {executor.submit(run_one_job, (i, j)): i for i, j in enumerate(jobs)}
        for future in as_completed(futures):
            idx, label, ok, temp_file = future.result()
            run_count += 1
            t = datetime.now().strftime("%H:%M:%S")
            if ok is None:
                print(
                    f"  [{run_count}/{total}] {t} {label}... SKIPPED (timeout > 1 min)"
                )
            else:
                print(
                    f"  [{run_count}/{total}] {t} {label}... {'OK' if ok else 'FAILED'}"
                )
            if ok is False:
                failed.append(label)
            # Append this job's result to the main MD file (one-by-one, serialized)
            if temp_file.exists():
                try:
                    content = temp_file.read_text(encoding="utf-8")
                    with append_lock:
                        with open(out_md, "a", encoding="utf-8") as f:
                            f.write(content)
                finally:
                    temp_file.unlink(missing_ok=True)

    try:
        temp_dir.rmdir()
    except OSError:
        pass

    if failed:
        with open(out_md, "a", encoding="utf-8") as f:
            f.write(
                "\n\n## Failed runs\n\n" + "\n".join("- " + x for x in failed) + "\n"
            )
        print(f"{len(failed)} run(s) failed. Results in {out_md}", file=sys.stderr)
        sys.exit(1)

    print(f"\nDone. Results saved to: {out_md}")


if __name__ == "__main__":
    main()
