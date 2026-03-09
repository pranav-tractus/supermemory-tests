# Test results by model provider

Summary reports are organised by provider and by scope (single-provider vs multi-model).

## Folder structure

| Folder | Description | Files |
|--------|-------------|-------|
| **results/google/** | Google Gemini–only tests | `gemini_flash_summary.md`, `gemini_flash.md`, `gemini_flash_vs_pro.md`, `gemini_pro.md`, `gemini-comparison-with-new-prompt.md` |
| **results/openai/** | OpenAI/ChatGPT–only tests | `chatgpt-comparison-with-new-prompt.md`, `gpt54_new_prompt_summary.md`, `gpt54_old_prompt_summary.md`, `openai_5-4_test_summary.md`, `openai_memory_only_mem0_summary.md`, `openai_memory_only_summary.md` |
| **results/anthropic/** | Anthropic Claude–only tests | `claude_all_types_summary.md`, `claude_bedrock_test_summary.md`, `claude_fewshot_results_summary.md`, `claude_memory_all_types_summary_new.md`, `claude_memory_results_summary.md`, `few_shot_summary.md` |
| **results/all/** | Tests comparing 2+ provider types (Claude, Gemini, OpenAI) | `all_model_comparison.md`, `memory_comparison_*.md`, `model_chat_comparison_results_summary*.md`, `Results.md` |

- **Single-provider folders** (`results/google/`, `results/openai/`, `results/anthropic/`): results for one provider’s models only.
- **results/all/**: cross-provider comparisons and memory/comparison runs that include more than one provider.
