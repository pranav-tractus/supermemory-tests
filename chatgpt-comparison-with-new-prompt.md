# LLM comparison — ChatGPT models, one product one shipment

Chat: `long_single_product_single_shipment.json` (1 shipment: 10 bags KNM Coffee).  
Models: ChatGPT only (4o, 4.1, 5.2, 5-mini).

## Ground truth (expected)

- **1 contract** (one shipment).
- **Contract 1:** Nov 28 — 10 bags KNM Coffee, $23.75/bag (5% off), $237.50 total → 100 Finance Ave.

---

## Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
|-------|------|-----------|-----|-----|---------------|--------------|-----|-----|
| openai (gpt-4.1-2025-04-14) | 10 | 100.0 | 100 | 100 | 10/10 | 3.27 | 1.81 | 10.82 |
| openai (gpt-4o-2024-08-06) | 10 | 100.0 | 100 | 100 | 10/10 | 2.74 | 1.94 | 5.57 |
| openai (gpt-5-mini-2025-08-07) | 10 | 85.0 | 25 | 100 | 8/10 | 30.89 | 23.45 | 38.36 |
| openai (gpt-5.2-2025-12-11) | 10 | 85.0 | 25 | 100 | 8/10 | 2.30 | 2.03 | 3.00 |

**Score:** 0–100 (25 pts: 1 contract; 75 pts: correct item/qty/total/date/address).  
**Perfect:** run with score ≥ 99.

---

## Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
|-------|---------------|----------|-------|------------|------------|
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 10.82 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 2.03 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 1.92 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 1.98 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 3.44 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 3.66 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 3.15 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 1.81 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 1.82 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 2.10 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.73 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.79 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.03 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 3.01 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 2.43 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 1.94 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.50 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 5.57 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 2.16 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.26 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_1 | 30.87 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_10 | 32.71 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_2 | 26.01 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_3 | 32.49 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_4 | 30.23 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_5 | 31.23 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_6 | 23.45 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_7 | 38.36 | 100 | ✓ | ✓ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_8 | 36.84 | 25 | ✓ | ✗ |
| openai (gpt-5-mini-2025-08-07) | openai_5-mini_run_9 | 26.69 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 2.38 | 100 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 2.20 | 100 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 2.03 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.12 | 100 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 3.00 | 100 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.28 | 100 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.27 | 100 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.30 | 25 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 2.14 | 100 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 2.27 | 100 | ✓ | ✓ |
