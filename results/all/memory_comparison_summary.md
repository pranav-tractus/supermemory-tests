# Memory comparison — accuracy & correctness summary

Source: `memory_comparison_results.md`  
Chat: `short_multi_shipment_multi_product.json` (3 shipments: coffee / tea+paper / balloons).

## Ground truth (expected)

- **3 contracts** (shipments).
- **Contract 1:** Nov 28 — 12 bags KNM Coffee, $3000 total → 100 Finance Ave.
- **Contract 2:** Dec 5 — 30 boxes Assam tea ($10,800) + 50 reams paper ($10,000) → 100 Finance Ave.
- **Contract 3:** Dec 12 — 3000 Red Balloons $9000 → Changi Hospital Wars 24 Singapore 700339.

---

## Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
|-------|------|-----------|-----|-----|---------------|--------------|-----|-----|
| openai (gpt-4.1-2025-04-14) | 10 | 80.0 | 0 | 100 | 8/10 | 5.04 | 3.47 | 10.20 |
| openai (gpt-5.2-2025-12-11) | 10 | 75.0 | 75 | 75 | 0/10 | 6.68 | 5.54 | 10.56 |
| gemini (google/gemini-2.0-flash) | 10 | 67.5 | 25 | 100 | 3/10 | 4.87 | 4.37 | 6.10 |
| gemini (google/gemini-2.5-flash) | 10 | 50.0 | 25 | 100 | 1/10 | 23.38 | 17.24 | 32.38 |
| gemini (google/gemini-2.5-pro) | 10 | 50.0 | 50 | 50 | 0/10 | 29.32 | 27.22 | 36.47 |
| openai (gpt-5-mini-2025-08-07) | 10 | 42.5 | 0 | 50 | 0/10 | 34.66 | 21.84 | 48.90 |
| openai (gpt-4o-2024-08-06) | 10 | 30.0 | 0 | 100 | 1/10 | 4.27 | 2.11 | 7.43 |

**Score:** 0–100 (25 pts each: 3 contracts, C1 correct, C2 correct, C3 correct).  
**Perfect:** run with score ≥ 99.

---

## Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 3 contracts | C1 | C2 | C3 |
|-------|---------------|----------|-------|--------------|----|----|----|
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_1 | 4.37 | 25 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_10 | 5.12 | 75 | ✓ | ✓ | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_2 | 6.10 | 25 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_3 | 4.64 | 100 | ✓ | ✓ | ✓ | ✓ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_4 | 4.64 | 75 | ✓ | ✓ | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_5 | 4.60 | 75 | ✓ | ✓ | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_6 | 4.92 | 25 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_7 | 4.99 | 75 | ✓ | ✓ | ✓ | ✗ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_8 | 4.79 | 100 | ✓ | ✓ | ✓ | ✓ |
| gemini (google/gemini-2.0-flash) | gemini_gemini-2_0-flash_run_9 | 4.53 | 100 | ✓ | ✓ | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 17.24 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 19.21 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 27.21 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 29.54 | 25 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 22.42 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 32.38 | 25 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 23.76 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 19.65 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 17.37 | 100 | ✓ | ✓ | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 25.03 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 28.42 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 32.61 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 27.44 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 28.41 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 27.30 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 27.63 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 28.76 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 28.98 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 27.22 | 50 | ✓ | ✗ | ✗ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 36.47 | 50 | ✓ | ✗ | ✗ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 3.63 | 0 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 4.47 | 100 | ✓ | ✓ | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 4.63 | 100 | ✓ | ✓ | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 4.74 | 100 | ✓ | ✓ | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 4.36 | 100 | ✓ | ✓ | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 3.47 | 0 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 5.25 | 100 | ✓ | ✓ | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 10.20 | 100 | ✓ | ✓ | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 4.67 | 100 | ✓ | ✓ | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 4.95 | 100 | ✓ | ✓ | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 5.14 | 25 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.33 | 0 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 4.89 | 75 | ✓ | ✓ | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 4.21 | 100 | ✓ | ✓ | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 4.40 | 25 | ✗ | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 2.96 | 0 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.11 | 0 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 7.43 | 0 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 6.27 | 75 | ✓ | ✗ | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.97 | 0 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_1 | 30.88 | 50 | ✓ | ✗ | ✗ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_10 | 39.56 | 50 | ✓ | ✗ | ✗ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_2 | 35.29 | 50 | ✓ | ✗ | ✗ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_3 | 32.32 | 25 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_4 | 48.90 | 0 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_5 | 40.35 | 50 | ✓ | ✗ | ✗ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_6 | 38.97 | 50 | ✓ | ✗ | ✗ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_7 | 21.84 | 50 | ✓ | ✗ | ✗ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_8 | 29.19 | 50 | ✓ | ✗ | ✗ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_9 | 29.25 | 50 | ✓ | ✗ | ✗ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 5.74 | 75 | ✓ | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 6.18 | 75 | ✓ | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 7.34 | 75 | ✓ | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 6.76 | 75 | ✓ | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 10.56 | 75 | ✓ | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 5.69 | 75 | ✓ | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 6.18 | 75 | ✓ | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 6.50 | 75 | ✓ | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 6.32 | 75 | ✓ | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 5.54 | 75 | ✓ | ✓ | ✓ | ✗ |
