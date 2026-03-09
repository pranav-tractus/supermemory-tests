# Model comparison — Accuracy & correctness

Source: `model_chat_comparison_results.md`
Chats: `multiple_product_multiple_shipment_complex.json`, `multiple_product_multiple_shipment_medium.json`, `multiple_product_multiple_shipment_simple.json`, `single_product_multiple_shipment_complex.json`, `single_product_multiple_shipment_medium.json`, `single_product_multiple_shipment_simple.json`, `single_product_single_shipment_complex.json`, `single_product_single_shipment_medium.json`, `single_product_single_shipment_simple.json`

---

## Chat: multiple_product_multiple_shipment_complex.json

### Ground truth (expected)

- **3 contracts** (expected).

- **Contract 1:** 2025-11-28 — 12 bags KNM Coffee, $25.00/bags, $300.00 total → 100 Finance Ave.
- **Contract 2:** 2025-12-05 — 30 boxes Assam tea, $12.00/boxes, $360.00 total; 50 reams paper, $4.00/reams, $200.00 total → 100 Finance Ave.
- **Contract 3:** 2025-12-12 — 3000 1000 Red Balloons, $3000.00/1000, $9000.00 total → Changi Hospital Way Singapore 700339.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | 91.0 | 91 | 91 | 0/10 | 12.36 | 11.28 | 13.39 |
| claude (claude-opus-4-6) | 10 | 90.6 | 15 | 99 | 9/10 | 11.14 | 9.61 | 11.76 |
| claude (claude-sonnet-4-5@20250929) | 10 | 97.5 | 97 | 98 | 10/10 | 13.74 | 13.19 | 14.77 |
| claude (claude-sonnet-4-6) | 10 | 98.0 | 98 | 98 | 10/10 | 10.94 | 10.49 | 11.48 |
| gemini (google/gemini-2.5-flash) | 10 | 95.2 | 89 | 98 | 8/10 | 25.30 | 18.29 | 33.25 |
| gemini (google/gemini-2.5-pro) | 10 | 94.3 | 90 | 98 | 6/10 | 33.99 | 24.42 | 48.86 |
| gemini (google/gemini-3-flash-preview) | 9 | 91.8 | 88 | 96 | 2/9 | 40.53 | 30.42 | 51.30 |
| openai (gpt-4.1-2025-04-14) | 9 | 45.9 | 13 | 91 | 0/9 | 5.10 | 2.89 | 8.22 |
| openai (gpt-4o-2024-08-06) | 10 | 51.3 | 12 | 82 | 0/10 | 4.67 | 2.41 | 8.26 |
| openai (gpt-5.2-2025-12-11) | 10 | 26.5 | 13 | 77 | 0/10 | 4.52 | 3.55 | 6.95 |

**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 3 contracts | C1 correct | C2 correct | C3 correct |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 12.32 | 91 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 11.28 | 91 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 12.53 | 91 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 12.60 | 91 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 12.19 | 91 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 13.39 | 91 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 12.54 | 91 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 12.51 | 91 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 12.20 | 91 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 12.06 | 91 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 10.89 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 11.04 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 11.26 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 11.23 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 11.70 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 11.76 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 11.53 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 9.61 | 15 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 11.40 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 10.96 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 13.28 | 97 | ✓ | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 14.75 | 98 | ✓ | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 13.36 | 98 | ✓ | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 14.77 | 97 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 13.30 | 98 | ✓ | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 13.61 | 98 | ✓ | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 13.46 | 97 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 13.19 | 97 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 14.23 | 97 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 13.46 | 98 | ✓ | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 11.30 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 10.49 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 10.95 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 10.60 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 10.80 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 11.07 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 11.48 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 10.74 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 11.19 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 10.80 | 98 | ✓ | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 20.26 | 89 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 20.77 | 97 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 33.25 | 95 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 25.99 | 98 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 25.32 | 96 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 30.02 | 96 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 18.29 | 96 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 25.08 | 95 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 29.99 | 96 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 24.07 | 94 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 48.86 | 96 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 45.28 | 94 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 44.09 | 91 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 26.14 | 98 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 24.42 | 97 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 29.88 | 90 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 30.46 | 97 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 33.55 | 95 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 30.02 | 90 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 27.19 | 95 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 32.07 | 94 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 38.42 | 95 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 41.39 | 96 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 50.98 | 89 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 46.18 | 88 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 37.64 | 94 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 51.30 | 88 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 36.33 | 88 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 30.42 | 94 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 6.98 | 88 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 4.63 | 91 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 5.48 | 13 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 4.69 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 3.30 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 2.99 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 6.72 | 81 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 8.22 | 84 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 2.89 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.41 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 5.35 | 82 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 5.63 | 57 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 5.11 | 82 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 4.67 | 20 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 3.10 | 12 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.68 | 13 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 8.26 | 78 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 4.76 | 82 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 4.77 | 73 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 3.63 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 5.15 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 6.95 | 77 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 3.75 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 4.28 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 3.55 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 3.84 | 13 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 4.00 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 6.46 | 77 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 3.56 | 14 | ✗ | ✗ | ✗ | ✗ |


## Chat: multiple_product_multiple_shipment_medium.json

### Ground truth (expected)

- **2 contracts** (expected).

- **Contract 1:** 2025-11-28 — 12 bags KNM Coffee, $25.00/bags, $300.00 total → 100 Finance Ave.
- **Contract 2:** 2025-12-05 — 30 boxes Assam tea, $12.00/boxes, $360.00 total; 50 reams paper, $4.00/reams, $200.00 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | 25.0 | 25 | 25 | 0/10 | 7.26 | 6.93 | 7.95 |
| claude (claude-opus-4-6) | 10 | 23.0 | 23 | 23 | 0/10 | 7.63 | 6.89 | 9.70 |
| claude (claude-sonnet-4-5@20250929) | 10 | 97.4 | 97 | 98 | 10/10 | 8.86 | 8.45 | 9.19 |
| claude (claude-sonnet-4-6) | 10 | 100.0 | 100 | 100 | 10/10 | 7.71 | 7.35 | 8.05 |
| gemini (google/gemini-2.5-flash) | 10 | 96.5 | 91 | 98 | 9/10 | 21.23 | 15.82 | 24.31 |
| gemini (google/gemini-2.5-pro) | 10 | 97.8 | 97 | 99 | 10/10 | 28.59 | 18.14 | 36.79 |
| gemini (google/gemini-3-flash-preview) | 10 | 97.2 | 97 | 98 | 10/10 | 35.27 | 20.59 | 56.47 |
| openai (gpt-4.1-2025-04-14) | 10 | 35.6 | 23 | 86 | 0/10 | 3.53 | 2.31 | 8.60 |
| openai (gpt-4o-2024-08-06) | 10 | 40.2 | 22 | 82 | 0/10 | 3.16 | 2.28 | 4.82 |
| openai (gpt-5.2-2025-12-11) | 10 | 77.0 | 21 | 84 | 0/10 | 4.09 | 3.30 | 4.89 |

**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 2 contracts | C1 correct | C2 correct |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 6.93 | 25 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 7.07 | 25 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 7.15 | 25 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 7.41 | 25 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 7.19 | 25 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 7.62 | 25 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 7.95 | 25 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 7.03 | 25 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 7.09 | 25 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 7.17 | 25 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 7.70 | 23 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 7.63 | 23 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 7.22 | 23 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 7.23 | 23 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 7.07 | 23 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 7.50 | 23 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 7.37 | 23 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 6.89 | 23 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 7.96 | 23 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 9.70 | 23 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 8.86 | 97 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 9.04 | 97 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 8.68 | 98 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 8.98 | 97 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 8.47 | 98 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 9.00 | 98 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 9.11 | 97 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 8.45 | 98 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 8.84 | 97 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 9.19 | 97 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 7.72 | 100 | ✓ | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 7.66 | 100 | ✓ | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 7.81 | 100 | ✓ | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 7.89 | 100 | ✓ | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 7.43 | 100 | ✓ | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 8.05 | 100 | ✓ | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 7.59 | 100 | ✓ | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 7.61 | 100 | ✓ | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 7.35 | 100 | ✓ | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 7.98 | 100 | ✓ | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 23.87 | 96 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 22.68 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 15.82 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 20.32 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 23.80 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 17.74 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 24.31 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 23.17 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 21.19 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 19.42 | 91 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 26.28 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 36.76 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 18.14 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 36.79 | 99 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 27.34 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 29.46 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 25.22 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 27.67 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 28.21 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 30.07 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 46.28 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 27.42 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 56.47 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 33.28 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 20.59 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 35.16 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 30.02 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 26.23 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 42.21 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 35.01 | 97 | ✓ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 2.31 | 25 | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 5.52 | 86 | ✓ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 3.06 | 24 | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 8.60 | 78 | ✓ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 2.44 | 23 | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 2.76 | 23 | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 3.09 | 25 | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 2.43 | 23 | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 2.59 | 25 | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 2.46 | 24 | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 4.13 | 82 | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.28 | 25 | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.66 | 24 | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 4.11 | 76 | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 2.28 | 24 | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 4.82 | 23 | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 3.12 | 24 | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 2.56 | 22 | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 2.59 | 24 | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 3.03 | 78 | ✓ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 4.37 | 83 | ✓ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 4.86 | 83 | ✓ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 3.73 | 83 | ✓ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 4.89 | 83 | ✓ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 3.46 | 84 | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 3.91 | 84 | ✓ | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 3.62 | 83 | ✓ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 3.30 | 21 | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 4.68 | 83 | ✓ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 4.04 | 83 | ✓ | ✗ | ✗ |


## Chat: multiple_product_multiple_shipment_simple.json

### Ground truth (expected)

- **1 contract** (expected).

- **Contract 1:** 10 bags KNM Coffee, $25.00/bags, $250.00 total; 20 boxes Assam tea, $12.00/boxes, $240.00 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | 83.0 | 83 | 83 | 0/10 | 5.89 | 5.45 | 6.49 |
| claude (claude-opus-4-6) | 10 | 82.2 | 82 | 83 | 0/10 | 6.36 | 5.92 | 6.72 |
| claude (claude-sonnet-4-5@20250929) | 10 | 49.0 | 49 | 49 | 0/10 | 7.31 | 7.01 | 7.61 |
| claude (claude-sonnet-4-6) | 10 | 41.0 | 41 | 41 | 0/10 | 6.51 | 6.28 | 7.00 |
| gemini (google/gemini-2.5-flash) | 10 | 42.3 | 40 | 49 | 0/10 | 19.23 | 12.73 | 25.51 |
| gemini (google/gemini-2.5-pro) | 10 | 49.7 | 49 | 50 | 0/10 | 23.62 | 17.77 | 32.64 |
| gemini (google/gemini-3-flash-preview) | 10 | 63.2 | 48 | 98 | 3/10 | 27.76 | 19.55 | 43.97 |
| openai (gpt-4.1-2025-04-14) | 10 | 90.0 | 75 | 100 | 6/10 | 4.59 | 2.04 | 6.61 |
| openai (gpt-4o-2024-08-06) | 10 | 82.5 | 82 | 83 | 0/10 | 2.70 | 1.76 | 6.24 |
| openai (gpt-5.2-2025-12-11) | 10 | 48.4 | 40 | 82 | 0/10 | 3.25 | 2.20 | 4.34 |

**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
| ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 6.03 | 83 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 5.83 | 83 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 5.83 | 83 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 6.06 | 83 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 5.69 | 83 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 5.62 | 83 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 5.76 | 83 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 6.49 | 83 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 6.16 | 83 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 5.45 | 83 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 6.39 | 83 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 6.72 | 82 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 6.59 | 82 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 6.36 | 83 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 6.49 | 82 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 6.32 | 82 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 6.50 | 82 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.92 | 82 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 6.05 | 82 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 6.24 | 82 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 7.21 | 49 | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 7.40 | 49 | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 7.25 | 49 | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 7.57 | 49 | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 7.33 | 49 | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 7.08 | 49 | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 7.01 | 49 | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 7.27 | 49 | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 7.38 | 49 | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 7.61 | 49 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 6.35 | 41 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 7.00 | 41 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 6.28 | 41 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 6.64 | 41 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 6.54 | 41 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 6.47 | 41 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 6.29 | 41 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 6.66 | 41 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 6.28 | 41 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 6.57 | 41 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 16.38 | 41 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 23.39 | 40 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 20.81 | 40 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 17.58 | 41 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 13.94 | 40 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 25.51 | 48 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 16.07 | 49 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 24.31 | 42 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 21.63 | 41 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 12.73 | 41 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 18.50 | 50 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 24.43 | 50 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 25.76 | 50 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 23.99 | 50 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 20.41 | 50 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 23.35 | 50 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 23.20 | 49 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 32.64 | 49 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 26.15 | 50 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 17.77 | 49 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 43.97 | 48 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 19.55 | 98 | ✓ | ✓ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 21.25 | 48 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 23.03 | 48 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 22.65 | 49 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 22.63 | 98 | ✓ | ✓ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 29.40 | 49 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 32.75 | 48 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 31.76 | 48 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 30.66 | 98 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 2.04 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 5.05 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 5.78 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 3.38 | 75 | ✗ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 4.81 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 6.61 | 75 | ✗ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 5.48 | 75 | ✗ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 5.11 | 75 | ✗ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 3.80 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 3.85 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.93 | 83 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.45 | 82 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.27 | 82 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 2.00 | 83 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 2.74 | 83 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 6.24 | 83 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.35 | 82 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 1.80 | 82 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 1.76 | 82 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.41 | 83 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 3.37 | 40 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 3.42 | 40 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 3.18 | 40 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.72 | 82 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 3.08 | 40 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 3.43 | 40 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 3.51 | 40 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.20 | 82 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 3.27 | 40 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 4.34 | 40 | ✗ | ✗ |


## Chat: single_product_multiple_shipment_complex.json

### Ground truth (expected)

- **3 contracts** (expected).

- **Contract 1:** 2025-11-28 — 14 bags KNM Coffee, $22.75/bags, $318.50 total → 100 Finance Ave.
- **Contract 2:** 2025-12-04 — 10 bags KNM Coffee, $22.75/bags, $227.50 total → 200 Warehouse Lane.
- **Contract 3:** 2025-12-10 — 8 bags KNM Coffee, $22.75/bags, $182.00 total → 15 New Branch Rd.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | 99.0 | 99 | 99 | 10/10 | 10.15 | 9.66 | 10.91 |
| claude (claude-opus-4-6) | 10 | 15.1 | 15 | 16 | 0/10 | 6.15 | 5.72 | 6.77 |
| claude (claude-sonnet-4-5@20250929) | 10 | 98.0 | 98 | 98 | 10/10 | 10.65 | 10.14 | 11.31 |
| claude (claude-sonnet-4-6) | 10 | 98.4 | 98 | 99 | 10/10 | 9.32 | 8.78 | 9.65 |
| gemini (google/gemini-2.5-flash) | 10 | 87.3 | 15 | 98 | 6/10 | 22.21 | 17.40 | 29.48 |
| gemini (google/gemini-2.5-pro) | 10 | 98.4 | 97 | 99 | 10/10 | 29.79 | 22.10 | 41.36 |
| gemini (google/gemini-3-flash-preview) | 10 | 63.2 | 14 | 97 | 6/10 | 28.27 | 16.01 | 37.32 |
| openai (gpt-4.1-2025-04-14) | 10 | 35.9 | 16 | 91 | 0/10 | 4.96 | 2.98 | 6.97 |
| openai (gpt-4o-2024-08-06) | 10 | 51.0 | 14 | 96 | 1/10 | 3.58 | 1.74 | 6.77 |
| openai (gpt-5.2-2025-12-11) | 10 | 45.7 | 15 | 90 | 0/10 | 3.70 | 2.12 | 5.21 |

**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 3 contracts | C1 correct | C2 correct | C3 correct |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 10.91 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 10.19 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 10.09 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 10.33 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 10.00 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 9.66 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 10.01 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 9.96 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 10.34 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 9.99 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 6.77 | 15 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 5.95 | 15 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 6.60 | 15 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 6.03 | 15 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 6.07 | 15 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 6.14 | 15 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 6.00 | 16 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.72 | 15 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 6.11 | 15 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 6.09 | 15 | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 10.58 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 10.19 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 10.79 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 10.88 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 10.80 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 10.61 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 10.80 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 11.31 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 10.14 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 10.36 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 9.63 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 9.33 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 9.32 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 9.65 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 9.41 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 8.78 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 9.05 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 9.62 | 99 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 9.16 | 98 | ✓ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 9.30 | 99 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 21.97 | 98 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 17.40 | 98 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 19.69 | 91 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 21.29 | 15 | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 18.27 | 91 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 29.48 | 96 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 22.08 | 98 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 27.84 | 97 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 20.95 | 98 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 23.18 | 91 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 29.24 | 98 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 22.10 | 97 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 27.88 | 98 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 24.30 | 98 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 24.36 | 98 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 29.38 | 99 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 30.39 | 99 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 33.54 | 99 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 41.36 | 99 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 35.31 | 99 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 27.77 | 14 | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 21.31 | 96 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 30.42 | 97 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 35.59 | 14 | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 37.32 | 95 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 16.01 | 96 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 28.62 | 95 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 34.18 | 95 | ✓ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 24.62 | 14 | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 26.84 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 6.97 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 4.80 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 3.10 | 65 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 2.98 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 5.68 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 4.75 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 5.19 | 91 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 5.00 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 4.78 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 6.40 | 91 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 5.06 | 96 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 1.74 | 15 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 4.04 | 89 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 3.42 | 90 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 3.56 | 15 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 6.77 | 70 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.46 | 15 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 3.59 | 91 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 3.18 | 14 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 1.96 | 15 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 5.21 | 90 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 2.85 | 15 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 2.30 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.49 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 5.01 | 72 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 4.89 | 72 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.28 | 16 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.12 | 15 | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 4.98 | 72 | ✓ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 4.92 | 73 | ✓ | ✗ | ✗ | ✗ |


## Chat: single_product_multiple_shipment_medium.json

### Ground truth (expected)

- **2 contracts** (expected).

- **Contract 1:** 2025-11-28 — 12 bags KNM Coffee, $23.75/bags, $285.00 total → 100 Finance Ave.
- **Contract 2:** 2025-12-06 — 8 bags KNM Coffee, $23.75/bags, $190.00 total → 50 Changi Business Park.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | 70.6 | 27 | 99 | 6/10 | 6.89 | 5.76 | 7.86 |
| claude (claude-opus-4-6) | 10 | 28.0 | 28 | 28 | 0/10 | 6.93 | 6.68 | 7.36 |
| claude (claude-sonnet-4-5@20250929) | 10 | 26.0 | 26 | 26 | 0/10 | 6.67 | 6.09 | 7.64 |
| claude (claude-sonnet-4-6) | 10 | 98.8 | 98 | 99 | 10/10 | 7.03 | 6.51 | 7.33 |
| gemini (google/gemini-2.5-flash) | 10 | 90.7 | 27 | 99 | 9/10 | 19.07 | 13.10 | 28.32 |
| gemini (google/gemini-2.5-pro) | 10 | 98.1 | 97 | 99 | 10/10 | 20.24 | 15.30 | 27.72 |
| gemini (google/gemini-3-flash-preview) | 10 | 88.8 | 25 | 98 | 8/10 | 25.16 | 17.24 | 32.91 |
| openai (gpt-4.1-2025-04-14) | 10 | 71.4 | 28 | 90 | 0/10 | 7.22 | 1.81 | 15.59 |
| openai (gpt-4o-2024-08-06) | 10 | 77.9 | 26 | 99 | 1/10 | 3.52 | 2.09 | 6.57 |
| openai (gpt-5.2-2025-12-11) | 10 | 31.3 | 24 | 76 | 0/10 | 2.46 | 1.97 | 3.29 |

**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 2 contracts | C1 correct | C2 correct |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 7.51 | 99 | ✓ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 5.98 | 27 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 7.70 | 99 | ✓ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 5.76 | 29 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 6.07 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 7.16 | 99 | ✓ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 6.23 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 7.86 | 99 | ✓ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 7.36 | 99 | ✓ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 7.29 | 99 | ✓ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 6.76 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 6.68 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 7.27 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 7.36 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 6.93 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 7.06 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 6.88 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 6.69 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 6.87 | 28 | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 6.77 | 28 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 6.63 | 26 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 7.31 | 26 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 6.57 | 26 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 7.22 | 26 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 6.49 | 26 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 7.64 | 26 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 6.35 | 26 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 6.26 | 26 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 6.09 | 26 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 6.15 | 26 | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 7.03 | 99 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 7.24 | 99 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 7.10 | 99 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 7.33 | 98 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 7.00 | 98 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 7.20 | 99 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 6.97 | 99 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 6.51 | 99 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 6.76 | 99 | ✓ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 7.17 | 99 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 15.43 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 22.34 | 27 | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 13.10 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 23.82 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 28.32 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 15.86 | 99 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 19.54 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 14.59 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 16.61 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 21.06 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 23.28 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 27.72 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 16.14 | 99 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 21.34 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 19.03 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 26.32 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 15.30 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 16.88 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 19.62 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 16.73 | 99 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 21.73 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 17.24 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 21.52 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 32.91 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 28.84 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 22.87 | 25 | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 25.25 | 97 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 26.27 | 85 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 22.23 | 98 | ✓ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 32.76 | 97 | ✓ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 14.20 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 4.00 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 2.19 | 28 | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 5.51 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 3.14 | 28 | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 10.05 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 12.08 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 15.59 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 1.81 | 28 | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 3.61 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.43 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.53 | 89 | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 3.40 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 2.09 | 27 | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 3.05 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 6.57 | 99 | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 5.00 | 89 | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 3.12 | 26 | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 2.84 | 90 | ✓ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 4.13 | 89 | ✓ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 2.52 | 26 | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 1.97 | 28 | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 3.29 | 76 | ✓ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.55 | 28 | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 2.64 | 28 | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.13 | 26 | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.66 | 24 | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.25 | 24 | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 2.06 | 27 | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 2.52 | 26 | ✗ | ✗ | ✗ |


## Chat: single_product_multiple_shipment_simple.json

### Ground truth (expected)

- **1 contract** (expected).

- **Contract 1:** 15 bags KNM Coffee, $25.00/bags, $375.00 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | 74.0 | 74 | 74 | 0/10 | 6.15 | 5.82 | 6.49 |
| claude (claude-opus-4-6) | 10 | 100.0 | 100 | 100 | 10/10 | 5.93 | 5.51 | 6.81 |
| claude (claude-sonnet-4-5@20250929) | 10 | 99.0 | 99 | 99 | 10/10 | 5.60 | 4.97 | 5.91 |
| claude (claude-sonnet-4-6) | 10 | 62.0 | 62 | 62 | 0/10 | 6.70 | 6.32 | 7.84 |
| gemini (google/gemini-2.5-flash) | 10 | 66.2 | 48 | 98 | 1/10 | 15.30 | 11.26 | 19.36 |
| gemini (google/gemini-2.5-pro) | 10 | 62.5 | 62 | 63 | 0/10 | 21.28 | 13.27 | 26.47 |
| gemini (google/gemini-3-flash-preview) | 9 | 66.8 | 61 | 99 | 1/9 | 25.82 | 20.44 | 35.96 |
| openai (gpt-4.1-2025-04-14) | 10 | 89.3 | 74 | 100 | 6/10 | 3.30 | 1.55 | 5.08 |
| openai (gpt-4o-2024-08-06) | 10 | 78.2 | 49 | 100 | 2/10 | 2.42 | 1.62 | 3.92 |
| openai (gpt-5.2-2025-12-11) | 10 | 68.0 | 48 | 97 | 3/10 | 2.98 | 2.13 | 3.69 |

**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
| ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 6.03 | 74 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 5.82 | 74 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 6.29 | 74 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 6.00 | 74 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 6.44 | 74 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 6.16 | 74 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 6.26 | 74 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 5.96 | 74 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 6.09 | 74 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 6.49 | 74 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 5.59 | 100 | ✓ | ✓ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 5.71 | 100 | ✓ | ✓ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 5.58 | 100 | ✓ | ✓ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 6.81 | 100 | ✓ | ✓ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 5.67 | 100 | ✓ | ✓ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 6.13 | 100 | ✓ | ✓ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 6.12 | 100 | ✓ | ✓ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.88 | 100 | ✓ | ✓ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 6.27 | 100 | ✓ | ✓ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 5.51 | 100 | ✓ | ✓ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 5.81 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 5.91 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 5.41 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 5.57 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 4.97 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 5.68 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 5.75 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 5.85 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 5.62 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 5.45 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 7.84 | 62 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 6.66 | 62 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 6.78 | 62 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 6.43 | 62 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 6.37 | 62 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 7.02 | 62 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 6.50 | 62 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 6.32 | 62 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 6.66 | 62 | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 6.41 | 62 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 13.55 | 62 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 12.40 | 48 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 16.31 | 61 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 17.02 | 62 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 13.13 | 61 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 17.51 | 98 | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 19.36 | 73 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 14.35 | 61 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 11.26 | 63 | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 18.13 | 73 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 26.47 | 63 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 25.37 | 63 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 19.95 | 62 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 21.72 | 62 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 22.06 | 62 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 24.15 | 63 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 21.54 | 62 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 17.02 | 63 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 21.23 | 62 | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 13.27 | 63 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 20.44 | 73 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 35.96 | 61 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 26.53 | 62 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 20.77 | 99 | ✓ | ✓ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 21.79 | 61 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 33.34 | 61 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 26.28 | 61 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 26.48 | 61 | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 20.82 | 62 | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 3.13 | 98 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 1.55 | 98 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 4.03 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 5.08 | 75 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 3.43 | 100 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 2.85 | 99 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 1.94 | 74 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 3.62 | 75 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 3.33 | 99 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 4.01 | 75 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 1.99 | 75 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.42 | 74 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.13 | 98 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 1.99 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 3.48 | 49 | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 2.24 | 75 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.16 | 75 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 3.92 | 75 | ✗ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 1.62 | 86 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.27 | 75 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 3.49 | 49 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 3.42 | 48 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 3.27 | 48 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.88 | 74 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 2.13 | 97 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.64 | 73 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.41 | 97 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.23 | 97 | ✓ | ✓ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 3.69 | 49 | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 3.61 | 48 | ✗ | ✗ |


## Chat: single_product_single_shipment_complex.json

### Ground truth (expected)

- **1 contract** (expected).

- **Contract 1:** 2025-11-28 — 10 bags KNM Coffee, $23.75/bags, $237.50 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | 94.8 | 92 | 99 | 4/10 | 6.24 | 6.02 | 6.70 |
| claude (claude-opus-4-6) | 10 | 99.0 | 99 | 99 | 10/10 | 6.35 | 5.97 | 7.40 |
| claude (claude-sonnet-4-5@20250929) | 10 | 99.0 | 99 | 99 | 10/10 | 6.80 | 6.27 | 7.45 |
| claude (claude-sonnet-4-6) | 10 | 98.0 | 98 | 98 | 10/10 | 5.66 | 5.26 | 6.57 |
| gemini (google/gemini-2.5-flash) | 10 | 98.1 | 97 | 99 | 10/10 | 15.68 | 12.00 | 22.77 |
| gemini (google/gemini-2.5-pro) | 10 | 97.9 | 97 | 99 | 10/10 | 17.82 | 12.81 | 23.97 |
| gemini (google/gemini-3-flash-preview) | 10 | 95.3 | 87 | 99 | 9/10 | 28.19 | 16.80 | 40.33 |
| openai (gpt-4.1-2025-04-14) | 10 | 99.0 | 99 | 99 | 10/10 | 2.45 | 1.41 | 4.22 |
| openai (gpt-4o-2024-08-06) | 10 | 98.7 | 97 | 99 | 10/10 | 2.02 | 1.71 | 2.93 |
| openai (gpt-5.2-2025-12-11) | 10 | 97.1 | 97 | 98 | 10/10 | 2.59 | 2.30 | 3.02 |

**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
| ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 6.17 | 92 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 6.19 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 6.25 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 6.28 | 92 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 6.05 | 92 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 6.24 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 6.02 | 92 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 6.24 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 6.30 | 92 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 6.70 | 92 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 7.40 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 5.97 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 6.09 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 6.78 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 6.09 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 6.13 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 6.43 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.99 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 6.30 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 6.34 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 6.66 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 6.82 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 6.74 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 7.17 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 6.88 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 6.64 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 7.45 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 6.97 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 6.27 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 6.39 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 5.68 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 5.26 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 6.57 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 5.74 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 5.61 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 5.57 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 5.59 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 5.40 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 5.75 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 5.41 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 12.29 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 14.59 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 22.77 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 12.21 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 15.12 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 16.35 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 18.72 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 12.00 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 18.00 | 97 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 14.74 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 15.67 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 19.44 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 14.84 | 97 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 13.00 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 20.20 | 97 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 23.97 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 19.69 | 97 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 15.44 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 23.17 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 12.81 | 98 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 25.70 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 36.45 | 95 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 24.73 | 95 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 20.89 | 99 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 23.03 | 95 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 25.69 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 40.33 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 16.80 | 96 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 39.64 | 95 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 28.59 | 87 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 4.22 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 3.05 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 3.28 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 1.41 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 3.05 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 1.82 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 2.18 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 2.23 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 1.68 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 1.62 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 1.92 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 1.93 | 98 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 1.88 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 1.73 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 2.93 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 2.13 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 1.80 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 2.28 | 97 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 1.71 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 1.86 | 99 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 2.73 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 2.61 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 2.51 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 3.02 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 2.30 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.66 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.50 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.78 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 2.48 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 2.35 | 97 | ✓ | ✗ |


## Chat: single_product_single_shipment_medium.json

### Ground truth (expected)

- **1 contract** (expected).

- **Contract 1:** 2025-11-28 — 8 bags KNM Coffee, $23.75/bags, $190.00 total → 100 Finance Ave Singapore 018989.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | 99.0 | 99 | 99 | 10/10 | 5.49 | 4.90 | 6.05 |
| claude (claude-opus-4-6) | 10 | 99.0 | 99 | 99 | 10/10 | 5.67 | 5.31 | 6.22 |
| claude (claude-sonnet-4-5@20250929) | 10 | 99.0 | 99 | 99 | 10/10 | 5.76 | 5.36 | 6.29 |
| claude (claude-sonnet-4-6) | 10 | 99.0 | 99 | 99 | 10/10 | 5.12 | 4.91 | 5.36 |
| gemini (google/gemini-2.5-flash) | 10 | 98.4 | 97 | 99 | 10/10 | 11.23 | 8.13 | 18.58 |
| gemini (google/gemini-2.5-pro) | 10 | 98.8 | 98 | 99 | 10/10 | 18.40 | 12.99 | 27.23 |
| gemini (google/gemini-3-flash-preview) | 10 | 97.7 | 97 | 99 | 10/10 | 19.83 | 13.13 | 28.62 |
| openai (gpt-4.1-2025-04-14) | 10 | 99.0 | 99 | 99 | 10/10 | 1.63 | 1.36 | 2.10 |
| openai (gpt-4o-2024-08-06) | 10 | 99.0 | 98 | 100 | 10/10 | 2.37 | 1.66 | 5.00 |
| openai (gpt-5.2-2025-12-11) | 10 | 97.8 | 97 | 98 | 10/10 | 2.41 | 2.18 | 2.77 |

**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
| ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 5.54 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 5.38 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 5.77 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 5.19 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 4.90 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 6.05 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 5.51 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 5.37 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 5.31 | 99 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 5.84 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 6.22 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 5.41 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 5.66 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 5.58 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 5.79 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 5.61 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 5.89 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.31 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 5.69 | 99 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 5.53 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 5.90 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 5.82 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 5.46 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 5.74 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 6.29 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 6.03 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 5.36 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 5.78 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 5.78 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 5.46 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 5.07 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 5.18 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 5.06 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 4.91 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 5.14 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 5.27 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 5.06 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 4.96 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 5.19 | 99 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 5.36 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 16.14 | 97 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 9.96 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 8.94 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 9.57 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 12.19 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 8.13 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 10.96 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 9.71 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 8.16 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 18.58 | 97 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 21.07 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 12.99 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 18.56 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 22.53 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 14.10 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 26.19 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 13.01 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 14.15 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 14.18 | 99 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 27.23 | 99 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 19.15 | 98 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 28.62 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 24.67 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 18.66 | 99 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 13.13 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 17.39 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 20.36 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 18.53 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 18.16 | 99 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 19.64 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 1.36 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 1.93 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 1.49 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 1.75 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 1.40 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 1.73 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 1.48 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 2.10 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 1.49 | 99 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 1.58 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.15 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 1.71 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.05 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 5.00 | 98 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 2.31 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 3.05 | 100 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 1.87 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 1.66 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 1.76 | 99 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.10 | 99 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 2.19 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 2.77 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 2.43 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.39 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 2.19 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.67 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.18 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.41 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 2.49 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 2.37 | 98 | ✓ | ✗ |


## Chat: single_product_single_shipment_simple.json

### Ground truth (expected)

- **1 contract** (expected).

- **Contract 1:** 2025-11-25 — 5 bags KNM Coffee, $25.00/bags, $125.00 total → 100 Finance Ave Singapore 018989.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | 98.0 | 98 | 98 | 10/10 | 5.55 | 5.11 | 6.22 |
| claude (claude-opus-4-6) | 10 | 98.0 | 98 | 98 | 10/10 | 5.68 | 5.03 | 6.63 |
| claude (claude-sonnet-4-5@20250929) | 10 | 98.0 | 98 | 98 | 10/10 | 5.65 | 5.39 | 6.03 |
| claude (claude-sonnet-4-6) | 10 | 98.2 | 98 | 99 | 10/10 | 4.96 | 4.64 | 5.15 |
| gemini (google/gemini-2.5-flash) | 10 | 97.7 | 97 | 98 | 10/10 | 10.00 | 6.64 | 16.93 |
| gemini (google/gemini-2.5-pro) | 10 | 98.0 | 98 | 98 | 10/10 | 14.30 | 11.90 | 20.21 |
| gemini (google/gemini-3-flash-preview) | 10 | 97.2 | 97 | 98 | 10/10 | 17.93 | 15.20 | 21.43 |
| openai (gpt-4.1-2025-04-14) | 10 | 98.4 | 98 | 99 | 10/10 | 3.46 | 1.52 | 4.81 |
| openai (gpt-4o-2024-08-06) | 10 | 97.9 | 96 | 99 | 10/10 | 2.00 | 1.49 | 2.44 |
| openai (gpt-5.2-2025-12-11) | 10 | 96.6 | 85 | 98 | 9/10 | 2.31 | 2.04 | 2.93 |

**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
| ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 5.11 | 98 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 6.22 | 98 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 5.81 | 98 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 6.08 | 98 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 5.71 | 98 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 5.32 | 98 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 5.32 | 98 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 5.36 | 98 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 5.11 | 98 | ✓ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 5.47 | 98 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 5.92 | 98 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 6.63 | 98 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 6.30 | 98 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 5.52 | 98 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 5.56 | 98 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 5.49 | 98 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 5.33 | 98 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.50 | 98 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 5.53 | 98 | ✓ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 5.03 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 5.66 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 5.93 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 5.67 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 5.39 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 5.48 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 5.59 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 5.54 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 5.59 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 5.57 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 6.03 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 4.93 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 4.86 | 99 | ✓ | ✓ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 5.08 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 4.97 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 5.15 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 4.64 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 4.95 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 5.05 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 4.95 | 98 | ✓ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 5.03 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 6.64 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 8.58 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 8.38 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 9.93 | 97 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 14.95 | 97 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 8.05 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 8.56 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 16.93 | 97 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 9.99 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 8.03 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 20.21 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 13.82 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 12.63 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 11.90 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 12.51 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 13.26 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 13.12 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 15.02 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 13.54 | 98 | ✓ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 17.00 | 98 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 20.94 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 15.20 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 18.84 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 17.91 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 16.67 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 21.43 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 16.42 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 16.07 | 98 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 15.99 | 97 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 19.80 | 98 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 3.41 | 99 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 3.66 | 99 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 3.49 | 98 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 1.52 | 98 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 3.04 | 99 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 3.07 | 98 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 4.81 | 98 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 4.22 | 98 | ✓ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 3.81 | 99 | ✓ | ✓ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 3.58 | 98 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.07 | 98 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 1.66 | 98 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.31 | 98 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 2.04 | 99 | ✓ | ✓ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 1.49 | 98 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 1.77 | 96 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 1.72 | 98 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 2.36 | 98 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 2.44 | 98 | ✓ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.17 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 2.34 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 2.22 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 2.18 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.28 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 2.16 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.44 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.93 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.21 | 97 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 2.29 | 98 | ✓ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 2.04 | 85 | ✓ | ✓ |


---

## Overview

- **Chats:** 9 — `multiple_product_multiple_shipment_complex.json`, `multiple_product_multiple_shipment_medium.json`, `multiple_product_multiple_shipment_simple.json`, `single_product_multiple_shipment_complex.json`, `single_product_multiple_shipment_medium.json`, `single_product_multiple_shipment_simple.json`, `single_product_single_shipment_complex.json`, `single_product_single_shipment_medium.json`, `single_product_single_shipment_simple.json`
- **Models:** 10 — `claude (claude-opus-4-5@20251101)`, `claude (claude-opus-4-6)`, `claude (claude-sonnet-4-5@20250929)`, `claude (claude-sonnet-4-6)`, `gemini (google/gemini-2.5-flash)`, `gemini (google/gemini-2.5-pro)`, `gemini (google/gemini-3-flash-preview)`, `openai (gpt-4.1-2025-04-14)`, `openai (gpt-4o-2024-08-06)`, `openai (gpt-5.2-2025-12-11)`
- **Total runs:** 897
- **Correct:** 52 | **Incorrect:** 845 | **N/A:** 0

---

## Incorrect runs (expected vs actual)

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_7`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-12'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_1`):
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 shipping_address: expected one of ['Changi Hospital Way Singapore 700339', 'Changi Hospital Wars 24 Singapore 700339'], got 'Changi Hospital Way, Singapore 700339, +65 9876 5432'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_10`):
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_2`):
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_4`):
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #3 shipping_address: expected one of ['Changi Hospital Way Singapore 700339', 'Changi Hospital Wars 24 Singapore 700339'], got 'Changi Hospital Way, Singapore 700339, +65 9876 5432'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_9`):
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_1`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4230.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_10`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_2`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red and White Balloons'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_4`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Balloons'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_5`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_6`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons and White Balloons'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_7`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red and White Balloons'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_8`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_9`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Balloons (1500 Red, 1500 White)'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red and White Balloons'
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_10`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Balloons (1500 red, 1500 white)'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red and White Balloons'
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red and White Balloons'
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_5`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4230.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got '1500 red and 1500 white balloons'
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_7`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got '1500 red and 1500 white balloons'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_8`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4230.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_9`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red and White Balloons'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_1`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-301', got 'SO-2024-1300'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-301', got 'SO-2024-1300'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
  - ... and 1 more

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_10`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_2`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_5`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4230.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_6`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-301', got 'SO-2024-1300'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-301', got 'SO-2024-1300'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red and 1500 white)'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - ... and 2 more

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_7`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4230.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_8`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (Red)'
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4230.0
  - ... and 1 more

- **multiple_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_9`):
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-301', got 'SO-2024-1300'
  - Contract #2 item #1 total: expected 360.0, got 338.4
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-301', got 'SO-2024-1300'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 item #1 total: expected 9000.0, got 8460.0
  - ... and 2 more

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_1`):
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-03'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_10`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-03'
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_2`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3384.0
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_3`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_5`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_6`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3384.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_7`):
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2025-12-03'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_8`):
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 282.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 339.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 188.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 total: expected 9000.0, got 522.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_9`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3384.0
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_1`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-12'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_10`):
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-03'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_2`):
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-12'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got 'Changi Hospital Way Singapore 700339'
  - Contract #2 items: expected 2, got 1
  - Contract #2 item #1 description: expected 'Assam tea', got 'KNM Coffee'
  - Contract #2 item #1 quantity: expected 30.0, got 12.0
  - Contract #2 item #1 total: expected 360.0, got 3600.0
  - Contract #2 item #2: missing in actual
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-11-28'
  - ... and 6 more

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_3`):
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-03'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_4`):
  - Contract count: expected 3, got 2
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-12'
  - Contract #2 items: expected 2, got 1
  - Contract #2 item #1 description: expected 'Assam tea', got 'Red Balloons'
  - Contract #2 item #1 quantity: expected 30.0, got 3000.0
  - Contract #2 item #1 total: expected 360.0, got 9000.0
  - Contract #2 item #2: missing in actual
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-12'
  - ... and 2 more

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_5`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-02-23'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-301', got 'SO-2024-1300'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_6`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-12'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_7`):
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-03'
  - Contract #3 item #1 total: expected 9000.0, got 27000.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_8`):
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-03'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_9`):
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 items: expected 2, got 3
  - Contract #2 item #1 description: expected 'Assam tea', got 'KNM Coffee'
  - Contract #2 item #1 quantity: expected 30.0, got 12.0
  - Contract #2 item #1 total: expected 360.0, got 3600.0
  - Contract #2 item #2 description: expected 'paper', got 'Assam tea'
  - Contract #2 item #2 quantity: expected 50.0, got 30.0
  - Contract #2 item #2 total: expected 200.0, got 10800.0
  - ... and 2 more

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_1`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_10`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_2`):
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 item #1 total: expected 9000.0, got 27000000.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_3`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_4`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_5`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_6`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-12'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_7`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_8`):
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 item #1 total: expected 9000.0, got 27000000.0
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'

- **multiple_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_9`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_1`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_10`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_2`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_3`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_4`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_5`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_6`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_7`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_8`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_9`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_1`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_10`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_3`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_6`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_7`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_8`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_9`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_1`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_10`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_2`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_4`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'

- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_1`):
  - Contract #1 item #1 total: expected 300.0, got 284.88
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 341.86
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 189.26
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_10`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_3`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_5`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_6`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_7`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_9`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2027-01-04'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #2 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2027-01-04'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_1`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_10`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_2`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_3`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_4`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_5`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_6`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_7`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_8`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_9`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_1`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_10`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_2`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_3`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_4`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_5`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_6`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_7`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_8`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_9`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_1`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_10`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #2 item #1 total: expected 360.0, got 306.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 169.0

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_2`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_3`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #2 item #1 total: expected 360.0, got 1026.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 950.0

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_4`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_5`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 3420.0
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_6`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_7`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 3420.0
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_8`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_9`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_1`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 475.0

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_10`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_2`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_3`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 3000.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_4`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_5`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 343.2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-01-31'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_6`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_7`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 2850.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_8`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_9`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 342.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 total: expected 360.0, got 0.0
  - Contract #2 item #2 description: expected 'paper', got 'Copy paper'
  - Contract #2 item #2 total: expected 200.0, got 0.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_4`):
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_5`):
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_7`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_1`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_10`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_2`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_3`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_4`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_5`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_6`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_7`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_8`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_9`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_1`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_10`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_3`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_6`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_7`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_9`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_1`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_10`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_1`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_10`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 0.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_3`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_5`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_6`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_7`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual
  - Contract #1 payment_date: expected one of ['Net 30 from last delivery', 'Net 30', 'Net 30 from delivery'], got '2025-01-04'

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_9`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_1`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_10`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_3`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_5`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_6`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_7`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_9`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_1`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_3`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_6`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_7`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_3`):
  - Contract count: expected 1, got 2

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_5`):
  - Contract count: expected 1, got 2

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_6`):
  - Contract count: expected 1, got 2

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_7`):
  - Contract count: expected 1, got 2

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_1`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_10`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_2`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_3`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 2400.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_4`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_5`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_6`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_7`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_8`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_9`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_1`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_10`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_5`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_6`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_7`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **multiple_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_9`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_1`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_10`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_2`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_3`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_4`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_5`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_6`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_7`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_8`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_9`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2025-01-09'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #2 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2025-01-09'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'
  - Contract #3 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2025-01-09'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_3`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2027-01-09'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #2 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2027-01-09'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'
  - Contract #3 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2027-01-09'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'
  - Contract #3 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2025-01-09'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #2 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2025-01-09'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'
  - Contract #3 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '2025-01-09'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'
  - Contract #3 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_1`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'
  - Contract #3 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_3`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28, 2026-12-04, 2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'
  - Contract #3 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'
  - Contract #3 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'
  - Contract #3 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'
  - Contract #3 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_8`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-10'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_9`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_1`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_10`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_2`):
  - Contract #1 items: expected 1, got 3
  - Contract #2 items: expected 1, got 0
  - Contract #2 item #1: missing in actual
  - Contract #3 items: expected 1, got 0
  - Contract #3 item #1: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_3`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_4`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_5`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_6`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_7`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_8`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_9`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'
  - Contract #3 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_10`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-01-09'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_2`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_3`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_4`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_5`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 items: expected 1, got 3
  - Contract #2 item #1 quantity: expected 10.0, got 14.0
  - Contract #2 item #1 total: expected 227.5, got 318.5
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 items: expected 1, got 3
  - Contract #3 item #1 quantity: expected 8.0, got 14.0
  - Contract #3 item #1 total: expected 182.0, got 318.5
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_6`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_7`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_8`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-280', got 'SO-2024-1200'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_9`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-01-09'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_1`):
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2025-12-10', got '2024-12-10'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_10`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_2`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_3`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_4`):
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 quantity: expected 10.0, got 32.0
  - Contract #2 item #1 total: expected 227.5, got 728.0
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 item #1 quantity: expected 8.0, got 32.0
  - Contract #3 item #1 total: expected 182.0, got 728.0
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_5`):
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 quantity: expected 10.0, got 32.0
  - Contract #2 item #1 total: expected 227.5, got 728.0
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 item #1 quantity: expected 8.0, got 32.0
  - Contract #3 item #1 total: expected 182.0, got 728.0
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_6`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_7`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **single_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_8`):
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 quantity: expected 10.0, got 32.0
  - Contract #2 item #1 total: expected 227.5, got 728.0
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 item #1 quantity: expected 8.0, got 32.0
  - Contract #3 item #1 total: expected 182.0, got 728.0
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_9`):
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 quantity: expected 10.0, got 32.0
  - Contract #2 item #1 total: expected 227.5, got 728.0
  - Contract #2 do_date: expected one of '2025-12-04', got '2026-12-04'
  - Contract #3 item #1 quantity: expected 8.0, got 32.0
  - Contract #3 item #1 total: expected 182.0, got 728.0
  - Contract #3 do_date: expected one of '2025-12-10', got '2026-12-10'

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_1`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_10`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_2`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_3`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_4`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_5`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_6`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_7`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_8`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_9`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_1`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_10`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_2`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_3`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_4`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_6`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_7`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_8`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_9`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_10`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_5`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28, 2026-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '坐'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
  - Contract #2 payment_date: expected one of ['Net 30 from last delivery', 'Net 30'], got '坐'
  - Contract #2 shipping_address: expected one of ['50 Changi Business Park', 'Changi Business Park'], got '坐'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_1`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_10`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_2`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_3`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_4`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_5`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_6`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_7`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_8`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_9`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2024-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_1`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_10`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_2`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_3`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_4`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_6`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_7`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-02-23'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_8`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_9`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_1`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_10`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_2`):
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #1 quantity: expected 8.0, got 20.0
  - Contract #2 item #1 total: expected 190.0, got 475.0
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'

- **single_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_3`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_4`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_5`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_6`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-06'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '50 Changi Business Park'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_7`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-06'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '50 Changi Business Park'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_8`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2025-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_9`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-06'
  - Contract #2: missing in actual

- **single_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_1`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_10`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_1`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_10`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_3`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_6`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_7`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_9`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_1`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_10`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_3`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_5`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_6`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_7`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_9`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_1`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_10`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_5`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_6`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_7`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_3`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_6`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_7`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_9`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_1`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_10`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_4`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_5`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_6`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_7`):
  - Contract count: expected 1, got 3

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_8`):
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_9`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_1`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_10`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_2`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_3`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_5`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_8`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_multiple_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_9`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got 'November 28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got 'November 28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got 'November 28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got 'November 28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got 'November 28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got 'November 28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'SO-2024-1103'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'SO-2024-1103'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'SO-2024-1103'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'SO-2024-1103'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'SO-2024-1103'

- **single_product_single_shipment_complex.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'SO-2024-1103'
  - Contract #1 payment_date: expected one of ['Net 30 from delivery', 'Net 30', 'Net 30 Days'], got '坐'

- **single_product_single_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_10`):
  - Contract #1 item #1 description: expected 'KNM Coffee', got '10 bags KNM Coffee'
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_complex.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_medium.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_1`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_4`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_4`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_1`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_10`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_3`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_4`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_8`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-flash)** (`gemini_gemini-2_5-flash_run_9`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_1`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_10`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_3`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_4`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_8`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-2.5-pro)** (`gemini_gemini-2_5-pro_run_9`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_1`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_10`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_3`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_4`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_8`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **gemini (google/gemini-3-flash-preview)** (`gemini_gemini-3-flash-preview_run_9`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_3`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4.1-2025-04-14)** (`openai_4_1_run_9`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_1`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_10`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_4`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-30'

- **single_product_single_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_8`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2024-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-4o-2024-08-06)** (`openai_default_run_9`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_1`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_10`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_3`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_4`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

- **single_product_single_shipment_simple.json** — **openai (gpt-5.2-2025-12-11)** (`openai_5_2_run_8`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'
