# Memory comparison — One product, one shipment (accuracy & correctness)

Source: `memory_comparison_one_product_one_shipment.md`  
Chat: `long_single_product_single_shipment.json` (1 shipment: 10 bags KNM Coffee).

## Ground truth (expected)

- **1 contract** (one shipment).
- **Contract 1:** Nov 28 — 10 bags KNM Coffee, $23.75/bag (5% off), $237.50 total → 100 Finance Ave.

---

## Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
|-------|------|-----------|-----|-----|---------------|--------------|-----|-----|
| openai (gpt-4.1-2025-04-14) | 10 | 100.0 | 100 | 100 | 10/10 | 1.82 | 1.42 | 2.39 |
| openai (gpt-4o-2024-08-06) | 10 | 100.0 | 100 | 100 | 10/10 | 2.90 | 1.93 | 3.59 |
| gemini (google/gemini-2.5-pro) | 10 | 85.0 | 25 | 100 | 8/10 | 27.45 | 15.64 | 45.42 |
| gemini (google/gemini-2.5-flash) | 10 | 62.5 | 25 | 100 | 5/10 | 14.81 | 11.13 | 17.69 |
| openai (gpt-5-mini-2025-08-07) | 10 | 62.5 | 25 | 100 | 5/10 | 19.54 | 17.30 | 23.79 |
| gemini (google/gemini-2.0-flash) | 10 | 40.0 | 25 | 100 | 2/10 | 2.47 | 2.11 | 2.79 |
| openai (gpt-5.2-2025-12-11) | 10 | 32.5 | 25 | 100 | 1/10 | 2.69 | 2.34 | 3.70 |

**Score:** 0–100 (25 pts: 1 contract; 75 pts: correct item/qty/total/date/address).  
**Perfect:** run with score ≥ 99.

---

## Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
|-------|---------------|----------|-------|------------|------------|
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_1 | 2.44 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_10 | 2.47 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_2 | 2.22 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_3 | 2.36 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_4 | 2.42 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_5 | 2.43 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_6 | 2.11 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_7 | 2.76 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_8 | 2.79 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_9 | 2.67 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 12.07 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 17.62 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 17.69 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 16.54 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 15.33 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 12.79 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 13.33 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 14.89 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 16.66 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 11.13 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 29.45 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 21.76 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 21.03 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 19.91 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 45.42 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 28.85 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 15.64 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 26.61 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 32.33 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 33.45 | 25 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 1.67 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 1.62 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 2.02 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 1.95 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 1.67 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 2.13 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 1.76 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 2.39 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 1.42 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 1.56 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 3.59 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.98 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.93 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 2.66 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 1.93 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 3.16 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.92 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 3.13 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 3.42 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.27 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_1 | 18.67 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_10 | 19.85 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_2 | 18.32 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_3 | 18.26 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_4 | 20.81 | 25 | ✓ | ✗ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_5 | 17.60 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_6 | 19.19 | 25 | ✓ | ✗ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_7 | 21.62 | 25 | ✓ | ✗ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_8 | 17.30 | 25 | ✓ | ✗ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_9 | 23.79 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 2.49 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 2.56 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 2.69 | 100 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.59 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 3.08 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 3.70 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.50 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.34 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 2.59 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 2.34 | 25 | ✓ | ✗ |
