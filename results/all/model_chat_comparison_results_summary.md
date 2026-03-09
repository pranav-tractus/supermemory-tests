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
| claude (claude-opus-4-5@20251101) | 10 | — | — | — | — | 12.36 | 11.28 | 13.39 |
| claude (claude-opus-4-6) | 10 | — | — | — | — | 11.14 | 9.61 | 11.76 |
| claude (claude-sonnet-4-5@20250929) | 10 | — | — | — | — | 13.74 | 13.19 | 14.77 |
| claude (claude-sonnet-4-6) | 10 | — | — | — | — | 10.94 | 10.49 | 11.48 |
| gemini (google/gemini-2.5-flash) | 10 | — | — | — | — | 25.30 | 18.29 | 33.25 |
| gemini (google/gemini-2.5-pro) | 10 | — | — | — | — | 33.99 | 24.42 | 48.86 |
| gemini (google/gemini-3-flash-preview) | 9 | — | — | — | — | 40.53 | 30.42 | 51.30 |
| openai (gpt-4.1-2025-04-14) | 9 | — | — | — | — | 5.10 | 2.89 | 8.22 |
| openai (gpt-4o-2024-08-06) | 10 | — | — | — | — | 4.67 | 2.41 | 8.26 |
| openai (gpt-5.2-2025-12-11) | 10 | — | — | — | — | 4.52 | 3.55 | 6.95 |

**Score:** 0–100 (25 pts: correct contract count; 75 pts: correct item/qty/total/date/address).
**Perfect:** run with score ≥ 99.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 3 contracts | C1 correct | C2 correct | C3 correct |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 12.32 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 11.28 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 12.53 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 12.60 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 12.19 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 13.39 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 12.54 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 12.51 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 12.20 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 12.06 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 10.89 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 11.04 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 11.26 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 11.23 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 11.70 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 11.76 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 11.53 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 9.61 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 11.40 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 10.96 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 13.28 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 14.75 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 13.36 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 14.77 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 13.30 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 13.61 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 13.46 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 13.19 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 14.23 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 13.46 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 11.30 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 10.49 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 10.95 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 10.60 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 10.80 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 11.07 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 11.48 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 10.74 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 11.19 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 10.80 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 20.26 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 20.77 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 33.25 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 25.99 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 25.32 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 30.02 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 18.29 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 25.08 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 29.99 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 24.07 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 48.86 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 45.28 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 44.09 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 26.14 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 24.42 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 29.88 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 30.46 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 33.55 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 30.02 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 27.19 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 32.07 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 38.42 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 41.39 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 50.98 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 46.18 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 37.64 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 51.30 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 36.33 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 30.42 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 6.98 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 4.63 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 5.48 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 4.69 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 3.30 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 2.99 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 6.72 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 8.22 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 2.89 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.41 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 5.35 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 5.63 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 5.11 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 4.67 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 3.10 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.68 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 8.26 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 4.76 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 4.77 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 3.63 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 5.15 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 6.95 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 3.75 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 4.28 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 3.55 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 3.84 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 4.00 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 6.46 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 3.56 | — | ✗ | ✗ | ✗ | ✗ |


## Chat: multiple_product_multiple_shipment_medium.json

### Ground truth (expected)

- **2 contracts** (expected).

- **Contract 1:** 2025-11-28 — 12 bags KNM Coffee, $25.00/bags, $300.00 total → 100 Finance Ave.
- **Contract 2:** 2025-12-05 — 30 boxes Assam tea, $12.00/boxes, $360.00 total; 50 reams paper, $4.00/reams, $200.00 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | — | — | — | — | 7.26 | 6.93 | 7.95 |
| claude (claude-opus-4-6) | 10 | — | — | — | — | 7.63 | 6.89 | 9.70 |
| claude (claude-sonnet-4-5@20250929) | 10 | — | — | — | — | 8.86 | 8.45 | 9.19 |
| claude (claude-sonnet-4-6) | 10 | — | — | — | — | 7.71 | 7.35 | 8.05 |
| gemini (google/gemini-2.5-flash) | 10 | — | — | — | — | 21.23 | 15.82 | 24.31 |
| gemini (google/gemini-2.5-pro) | 10 | — | — | — | — | 28.59 | 18.14 | 36.79 |
| gemini (google/gemini-3-flash-preview) | 10 | — | — | — | — | 35.27 | 20.59 | 56.47 |
| openai (gpt-4.1-2025-04-14) | 10 | — | — | — | — | 3.53 | 2.31 | 8.60 |
| openai (gpt-4o-2024-08-06) | 10 | — | — | — | — | 3.16 | 2.28 | 4.82 |
| openai (gpt-5.2-2025-12-11) | 10 | — | — | — | — | 4.09 | 3.30 | 4.89 |

**Score:** 0–100 (25 pts: correct contract count; 75 pts: correct item/qty/total/date/address).
**Perfect:** run with score ≥ 99.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 2 contracts | C1 correct | C2 correct |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 6.93 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 7.07 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 7.15 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 7.41 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 7.19 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 7.62 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 7.95 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 7.03 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 7.09 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 7.17 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 7.70 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 7.63 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 7.22 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 7.23 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 7.07 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 7.50 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 7.37 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 6.89 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 7.96 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 9.70 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 8.86 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 9.04 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 8.68 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 8.98 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 8.47 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 9.00 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 9.11 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 8.45 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 8.84 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 9.19 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 7.72 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 7.66 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 7.81 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 7.89 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 7.43 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 8.05 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 7.59 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 7.61 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 7.35 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 7.98 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 23.87 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 22.68 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 15.82 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 20.32 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 23.80 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 17.74 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 24.31 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 23.17 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 21.19 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 19.42 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 26.28 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 36.76 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 18.14 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 36.79 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 27.34 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 29.46 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 25.22 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 27.67 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 28.21 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 30.07 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 46.28 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 27.42 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 56.47 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 33.28 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 20.59 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 35.16 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 30.02 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 26.23 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 42.21 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 35.01 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 2.31 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 5.52 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 3.06 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 8.60 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 2.44 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 2.76 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 3.09 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 2.43 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 2.59 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 2.46 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 4.13 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.28 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.66 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 4.11 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 2.28 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 4.82 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 3.12 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 2.56 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 2.59 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 3.03 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 4.37 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 4.86 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 3.73 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 4.89 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 3.46 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 3.91 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 3.62 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 3.30 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 4.68 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 4.04 | — | ✗ | ✗ | ✗ |


## Chat: multiple_product_multiple_shipment_simple.json

### Ground truth (expected)

- **1 contract** (expected).

- **Contract 1:** 10 bags KNM Coffee, $25.00/bags, $250.00 total; 20 boxes Assam tea, $12.00/boxes, $240.00 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | — | — | — | — | 5.89 | 5.45 | 6.49 |
| claude (claude-opus-4-6) | 10 | — | — | — | — | 6.36 | 5.92 | 6.72 |
| claude (claude-sonnet-4-5@20250929) | 10 | — | — | — | — | 7.31 | 7.01 | 7.61 |
| claude (claude-sonnet-4-6) | 10 | — | — | — | — | 6.51 | 6.28 | 7.00 |
| gemini (google/gemini-2.5-flash) | 10 | — | — | — | — | 19.23 | 12.73 | 25.51 |
| gemini (google/gemini-2.5-pro) | 10 | — | — | — | — | 23.62 | 17.77 | 32.64 |
| gemini (google/gemini-3-flash-preview) | 10 | — | — | — | — | 27.76 | 19.55 | 43.97 |
| openai (gpt-4.1-2025-04-14) | 10 | — | — | — | — | 4.59 | 2.04 | 6.61 |
| openai (gpt-4o-2024-08-06) | 10 | — | — | — | — | 2.70 | 1.76 | 6.24 |
| openai (gpt-5.2-2025-12-11) | 10 | — | — | — | — | 3.25 | 2.20 | 4.34 |

**Score:** 0–100 (25 pts: correct contract count; 75 pts: correct item/qty/total/date/address).
**Perfect:** run with score ≥ 99.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
| ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 6.03 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 5.83 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 5.83 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 6.06 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 5.69 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 5.62 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 5.76 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 6.49 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 6.16 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 5.45 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 6.39 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 6.72 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 6.59 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 6.36 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 6.49 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 6.32 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 6.50 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.92 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 6.05 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 6.24 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 7.21 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 7.40 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 7.25 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 7.57 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 7.33 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 7.08 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 7.01 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 7.27 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 7.38 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 7.61 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 6.35 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 7.00 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 6.28 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 6.64 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 6.54 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 6.47 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 6.29 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 6.66 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 6.28 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 6.57 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 16.38 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 23.39 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 20.81 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 17.58 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 13.94 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 25.51 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 16.07 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 24.31 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 21.63 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 12.73 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 18.50 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 24.43 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 25.76 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 23.99 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 20.41 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 23.35 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 23.20 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 32.64 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 26.15 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 17.77 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 43.97 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 19.55 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 21.25 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 23.03 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 22.65 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 22.63 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 29.40 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 32.75 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 31.76 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 30.66 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 2.04 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 5.05 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 5.78 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 3.38 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 4.81 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 6.61 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 5.48 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 5.11 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 3.80 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 3.85 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.93 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.45 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.27 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 2.00 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 2.74 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 6.24 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.35 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 1.80 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 1.76 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.41 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 3.37 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 3.42 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 3.18 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.72 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 3.08 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 3.43 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 3.51 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.20 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 3.27 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 4.34 | — | ✗ | ✗ |


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
| claude (claude-opus-4-5@20251101) | 10 | — | — | — | — | 10.15 | 9.66 | 10.91 |
| claude (claude-opus-4-6) | 10 | — | — | — | — | 6.15 | 5.72 | 6.77 |
| claude (claude-sonnet-4-5@20250929) | 10 | — | — | — | — | 10.65 | 10.14 | 11.31 |
| claude (claude-sonnet-4-6) | 10 | — | — | — | — | 9.32 | 8.78 | 9.65 |
| gemini (google/gemini-2.5-flash) | 10 | — | — | — | — | 22.21 | 17.40 | 29.48 |
| gemini (google/gemini-2.5-pro) | 10 | — | — | — | — | 29.79 | 22.10 | 41.36 |
| gemini (google/gemini-3-flash-preview) | 10 | — | — | — | — | 28.27 | 16.01 | 37.32 |
| openai (gpt-4.1-2025-04-14) | 10 | — | — | — | — | 4.96 | 2.98 | 6.97 |
| openai (gpt-4o-2024-08-06) | 10 | — | — | — | — | 3.58 | 1.74 | 6.77 |
| openai (gpt-5.2-2025-12-11) | 10 | — | — | — | — | 3.70 | 2.12 | 5.21 |

**Score:** 0–100 (25 pts: correct contract count; 75 pts: correct item/qty/total/date/address).
**Perfect:** run with score ≥ 99.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 3 contracts | C1 correct | C2 correct | C3 correct |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 10.91 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 10.19 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 10.09 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 10.33 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 10.00 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 9.66 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 10.01 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 9.96 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 10.34 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 9.99 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 6.77 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 5.95 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 6.60 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 6.03 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 6.07 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 6.14 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 6.00 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.72 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 6.11 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 6.09 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 10.58 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 10.19 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 10.79 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 10.88 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 10.80 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 10.61 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 10.80 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 11.31 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 10.14 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 10.36 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 9.63 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 9.33 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 9.32 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 9.65 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 9.41 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 8.78 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 9.05 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 9.62 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 9.16 | — | ✗ | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 9.30 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 21.97 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 17.40 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 19.69 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 21.29 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 18.27 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 29.48 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 22.08 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 27.84 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 20.95 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 23.18 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 29.24 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 22.10 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 27.88 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 24.30 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 24.36 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 29.38 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 30.39 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 33.54 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 41.36 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 35.31 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 27.77 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 21.31 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 30.42 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 35.59 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 37.32 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 16.01 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 28.62 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 34.18 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 24.62 | — | ✗ | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 26.84 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 6.97 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 4.80 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 3.10 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 2.98 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 5.68 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 4.75 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 5.19 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 5.00 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 4.78 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 6.40 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 5.06 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 1.74 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 4.04 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 3.42 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 3.56 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 6.77 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.46 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 3.59 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 3.18 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 1.96 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 5.21 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 2.85 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 2.30 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.49 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 5.01 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 4.89 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.28 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.12 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 4.98 | — | ✗ | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 4.92 | — | ✗ | ✗ | ✗ | ✗ |


## Chat: single_product_multiple_shipment_medium.json

### Ground truth (expected)

- **2 contracts** (expected).

- **Contract 1:** 2025-11-28 — 12 bags KNM Coffee, $23.75/bags, $285.00 total → 100 Finance Ave.
- **Contract 2:** 2025-12-06 — 8 bags KNM Coffee, $23.75/bags, $190.00 total → 50 Changi Business Park.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | — | — | — | — | 6.89 | 5.76 | 7.86 |
| claude (claude-opus-4-6) | 10 | — | — | — | — | 6.93 | 6.68 | 7.36 |
| claude (claude-sonnet-4-5@20250929) | 10 | — | — | — | — | 6.67 | 6.09 | 7.64 |
| claude (claude-sonnet-4-6) | 10 | — | — | — | — | 7.03 | 6.51 | 7.33 |
| gemini (google/gemini-2.5-flash) | 10 | — | — | — | — | 19.07 | 13.10 | 28.32 |
| gemini (google/gemini-2.5-pro) | 10 | — | — | — | — | 20.24 | 15.30 | 27.72 |
| gemini (google/gemini-3-flash-preview) | 10 | — | — | — | — | 25.16 | 17.24 | 32.91 |
| openai (gpt-4.1-2025-04-14) | 10 | — | — | — | — | 7.22 | 1.81 | 15.59 |
| openai (gpt-4o-2024-08-06) | 10 | — | — | — | — | 3.52 | 2.09 | 6.57 |
| openai (gpt-5.2-2025-12-11) | 10 | — | — | — | — | 2.46 | 1.97 | 3.29 |

**Score:** 0–100 (25 pts: correct contract count; 75 pts: correct item/qty/total/date/address).
**Perfect:** run with score ≥ 99.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 2 contracts | C1 correct | C2 correct |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 7.51 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 5.98 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 7.70 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 5.76 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 6.07 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 7.16 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 6.23 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 7.86 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 7.36 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 7.29 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 6.76 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 6.68 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 7.27 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 7.36 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 6.93 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 7.06 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 6.88 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 6.69 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 6.87 | — | ✗ | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 6.77 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 6.63 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 7.31 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 6.57 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 7.22 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 6.49 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 7.64 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 6.35 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 6.26 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 6.09 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 6.15 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 7.03 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 7.24 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 7.10 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 7.33 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 7.00 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 7.20 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 6.97 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 6.51 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 6.76 | — | ✗ | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 7.17 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 15.43 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 22.34 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 13.10 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 23.82 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 28.32 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 15.86 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 19.54 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 14.59 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 16.61 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 21.06 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 23.28 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 27.72 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 16.14 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 21.34 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 19.03 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 26.32 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 15.30 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 16.88 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 19.62 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 16.73 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 21.73 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 17.24 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 21.52 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 32.91 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 28.84 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 22.87 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 25.25 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 26.27 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 22.23 | — | ✗ | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 32.76 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 14.20 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 4.00 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 2.19 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 5.51 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 3.14 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 10.05 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 12.08 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 15.59 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 1.81 | — | ✗ | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 3.61 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.43 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.53 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 3.40 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 2.09 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 3.05 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 6.57 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 5.00 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 3.12 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 2.84 | — | ✗ | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 4.13 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 2.52 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 1.97 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 3.29 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.55 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 2.64 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.13 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.66 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.25 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 2.06 | — | ✗ | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 2.52 | — | ✗ | ✗ | ✗ |


## Chat: single_product_multiple_shipment_simple.json

### Ground truth (expected)

- **1 contract** (expected).

- **Contract 1:** 15 bags KNM Coffee, $25.00/bags, $375.00 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | — | — | — | — | 6.15 | 5.82 | 6.49 |
| claude (claude-opus-4-6) | 10 | — | — | — | — | 5.93 | 5.51 | 6.81 |
| claude (claude-sonnet-4-5@20250929) | 10 | — | — | — | — | 5.60 | 4.97 | 5.91 |
| claude (claude-sonnet-4-6) | 10 | — | — | — | — | 6.70 | 6.32 | 7.84 |
| gemini (google/gemini-2.5-flash) | 10 | — | — | — | — | 15.30 | 11.26 | 19.36 |
| gemini (google/gemini-2.5-pro) | 10 | — | — | — | — | 21.28 | 13.27 | 26.47 |
| gemini (google/gemini-3-flash-preview) | 9 | — | — | — | — | 25.82 | 20.44 | 35.96 |
| openai (gpt-4.1-2025-04-14) | 10 | — | — | — | — | 3.30 | 1.55 | 5.08 |
| openai (gpt-4o-2024-08-06) | 10 | — | — | — | — | 2.42 | 1.62 | 3.92 |
| openai (gpt-5.2-2025-12-11) | 10 | — | — | — | — | 2.98 | 2.13 | 3.69 |

**Score:** 0–100 (25 pts: correct contract count; 75 pts: correct item/qty/total/date/address).
**Perfect:** run with score ≥ 99.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
| ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 6.03 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 5.82 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 6.29 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 6.00 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 6.44 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 6.16 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 6.26 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 5.96 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 6.09 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 6.49 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 5.59 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 5.71 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 5.58 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 6.81 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 5.67 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 6.13 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 6.12 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.88 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 6.27 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 5.51 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 5.81 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 5.91 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 5.41 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 5.57 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 4.97 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 5.68 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 5.75 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 5.85 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 5.62 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 5.45 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 7.84 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 6.66 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 6.78 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 6.43 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 6.37 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 7.02 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 6.50 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 6.32 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 6.66 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 6.41 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 13.55 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 12.40 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 16.31 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 17.02 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 13.13 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 17.51 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 19.36 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 14.35 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 11.26 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 18.13 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 26.47 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 25.37 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 19.95 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 21.72 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 22.06 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 24.15 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 21.54 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 17.02 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 21.23 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 13.27 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 20.44 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 35.96 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 26.53 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 20.77 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 21.79 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 33.34 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 26.28 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 26.48 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 20.82 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 3.13 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 1.55 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 4.03 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 5.08 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 3.43 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 2.85 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 1.94 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 3.62 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 3.33 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 4.01 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 1.99 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 2.42 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.13 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 1.99 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 3.48 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 2.24 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 2.16 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 3.92 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 1.62 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.27 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 3.49 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 3.42 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 3.27 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.88 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 2.13 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.64 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.41 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.23 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 3.69 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 3.61 | — | ✗ | ✗ |


## Chat: single_product_single_shipment_complex.json

### Ground truth (expected)

- **1 contract** (expected).

- **Contract 1:** 2025-11-28 — 10 bags KNM Coffee, $23.75/bags, $237.50 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | — | — | — | — | 6.24 | 6.02 | 6.70 |
| claude (claude-opus-4-6) | 10 | — | — | — | — | 6.35 | 5.97 | 7.40 |
| claude (claude-sonnet-4-5@20250929) | 10 | — | — | — | — | 6.80 | 6.27 | 7.45 |
| claude (claude-sonnet-4-6) | 10 | — | — | — | — | 5.66 | 5.26 | 6.57 |
| gemini (google/gemini-2.5-flash) | 10 | — | — | — | — | 15.68 | 12.00 | 22.77 |
| gemini (google/gemini-2.5-pro) | 10 | — | — | — | — | 17.82 | 12.81 | 23.97 |
| gemini (google/gemini-3-flash-preview) | 10 | — | — | — | — | 28.19 | 16.80 | 40.33 |
| openai (gpt-4.1-2025-04-14) | 10 | — | — | — | — | 2.45 | 1.41 | 4.22 |
| openai (gpt-4o-2024-08-06) | 10 | — | — | — | — | 2.02 | 1.71 | 2.93 |
| openai (gpt-5.2-2025-12-11) | 10 | — | — | — | — | 2.59 | 2.30 | 3.02 |

**Score:** 0–100 (25 pts: correct contract count; 75 pts: correct item/qty/total/date/address).
**Perfect:** run with score ≥ 99.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
| ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 6.17 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 6.19 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 6.25 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 6.28 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 6.05 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 6.24 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 6.02 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 6.24 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 6.30 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 6.70 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 7.40 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 5.97 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 6.09 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 6.78 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 6.09 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 6.13 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 6.43 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.99 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 6.30 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 6.34 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 6.66 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 6.82 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 6.74 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 7.17 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 6.88 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 6.64 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 7.45 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 6.97 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 6.27 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 6.39 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 5.68 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 5.26 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 6.57 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 5.74 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 5.61 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 5.57 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 5.59 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 5.40 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 5.75 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 5.41 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 12.29 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 14.59 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 22.77 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 12.21 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 15.12 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 16.35 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 18.72 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 12.00 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 18.00 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 14.74 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 15.67 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 19.44 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 14.84 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 13.00 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 20.20 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 23.97 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 19.69 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 15.44 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 23.17 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 12.81 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 25.70 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 36.45 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 24.73 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 20.89 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 23.03 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 25.69 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 40.33 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 16.80 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 39.64 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 28.59 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 4.22 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 3.05 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 3.28 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 1.41 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 3.05 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 1.82 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 2.18 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 2.23 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 1.68 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 1.62 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 1.92 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 1.93 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 1.88 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 1.73 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 2.93 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 2.13 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 1.80 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 2.28 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 1.71 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 1.86 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 2.73 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 2.61 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 2.51 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 3.02 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 2.30 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.66 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.50 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.78 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 2.48 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 2.35 | — | ✗ | ✗ |


## Chat: single_product_single_shipment_medium.json

### Ground truth (expected)

- **1 contract** (expected).

- **Contract 1:** 2025-11-28 — 8 bags KNM Coffee, $23.75/bags, $190.00 total → 100 Finance Ave Singapore 018989.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | — | — | — | — | 5.49 | 4.90 | 6.05 |
| claude (claude-opus-4-6) | 10 | — | — | — | — | 5.67 | 5.31 | 6.22 |
| claude (claude-sonnet-4-5@20250929) | 10 | — | — | — | — | 5.76 | 5.36 | 6.29 |
| claude (claude-sonnet-4-6) | 10 | — | — | — | — | 5.12 | 4.91 | 5.36 |
| gemini (google/gemini-2.5-flash) | 10 | — | — | — | — | 11.23 | 8.13 | 18.58 |
| gemini (google/gemini-2.5-pro) | 10 | — | — | — | — | 18.40 | 12.99 | 27.23 |
| gemini (google/gemini-3-flash-preview) | 10 | — | — | — | — | 19.83 | 13.13 | 28.62 |
| openai (gpt-4.1-2025-04-14) | 10 | — | — | — | — | 1.63 | 1.36 | 2.10 |
| openai (gpt-4o-2024-08-06) | 10 | — | — | — | — | 2.37 | 1.66 | 5.00 |
| openai (gpt-5.2-2025-12-11) | 10 | — | — | — | — | 2.41 | 2.18 | 2.77 |

**Score:** 0–100 (25 pts: correct contract count; 75 pts: correct item/qty/total/date/address).
**Perfect:** run with score ≥ 99.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
| ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 5.54 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 5.38 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 5.77 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 5.19 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 4.90 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 6.05 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 5.51 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 5.37 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 5.31 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 5.84 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 6.22 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 5.41 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 5.66 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 5.58 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 5.79 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 5.61 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 5.89 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.31 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 5.69 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 5.53 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 5.90 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 5.82 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 5.46 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 5.74 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 6.29 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 6.03 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 5.36 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 5.78 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 5.78 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 5.46 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 5.07 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 5.18 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 5.06 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 4.91 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 5.14 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 5.27 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 5.06 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 4.96 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 5.19 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 5.36 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 16.14 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 9.96 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 8.94 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 9.57 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 12.19 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 8.13 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 10.96 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 9.71 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 8.16 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 18.58 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 21.07 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 12.99 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 18.56 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 22.53 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 14.10 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 26.19 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 13.01 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 14.15 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 14.18 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 27.23 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 19.15 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 28.62 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 24.67 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 18.66 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 13.13 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 17.39 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 20.36 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 18.53 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 18.16 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 19.64 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 1.36 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 1.93 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 1.49 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 1.75 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 1.40 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 1.73 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 1.48 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 2.10 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 1.49 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 1.58 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.15 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 1.71 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.05 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 5.00 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 2.31 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 3.05 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 1.87 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 1.66 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 1.76 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.10 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 2.19 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 2.77 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 2.43 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.39 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 2.19 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.67 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.18 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.41 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 2.49 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 2.37 | — | ✗ | ✗ |


## Chat: single_product_single_shipment_simple.json

### Ground truth (expected)

- **1 contract** (expected).

- **Contract 1:** 2025-11-25 — 5 bags KNM Coffee, $25.00/bags, $125.00 total → 100 Finance Ave Singapore 018989.

---

### Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 10 | — | — | — | — | 5.55 | 5.11 | 6.22 |
| claude (claude-opus-4-6) | 10 | — | — | — | — | 5.68 | 5.03 | 6.63 |
| claude (claude-sonnet-4-5@20250929) | 10 | — | — | — | — | 5.65 | 5.39 | 6.03 |
| claude (claude-sonnet-4-6) | 10 | — | — | — | — | 4.96 | 4.64 | 5.15 |
| gemini (google/gemini-2.5-flash) | 10 | — | — | — | — | 10.00 | 6.64 | 16.93 |
| gemini (google/gemini-2.5-pro) | 10 | — | — | — | — | 14.30 | 11.90 | 20.21 |
| gemini (google/gemini-3-flash-preview) | 10 | — | — | — | — | 17.93 | 15.20 | 21.43 |
| openai (gpt-4.1-2025-04-14) | 10 | — | — | — | — | 3.46 | 1.52 | 4.81 |
| openai (gpt-4o-2024-08-06) | 10 | — | — | — | — | 2.00 | 1.49 | 2.44 |
| openai (gpt-5.2-2025-12-11) | 10 | — | — | — | — | 2.31 | 2.04 | 2.93 |

**Score:** 0–100 (25 pts: correct contract count; 75 pts: correct item/qty/total/date/address).
**Perfect:** run with score ≥ 99.

---

### Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
| ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_1 | 5.11 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_10 | 6.22 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_2 | 5.81 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_3 | 6.08 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_4 | 5.71 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_5 | 5.32 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_6 | 5.32 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_7 | 5.36 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_8 | 5.11 | — | ✗ | ✗ |
| claude (claude-opus-4-5@20251101) | claude_opus-4-5_run_9 | 5.47 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_1 | 5.92 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_10 | 6.63 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_2 | 6.30 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_3 | 5.52 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_4 | 5.56 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_5 | 5.49 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_6 | 5.33 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_7 | 5.50 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_8 | 5.53 | — | ✗ | ✗ |
| claude (claude-opus-4-6) | claude_opus-4-6_run_9 | 5.03 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 5.66 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 5.93 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 5.67 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 5.39 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 5.48 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 5.59 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 5.54 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 5.59 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8 | 5.57 | — | ✗ | ✗ |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9 | 6.03 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_1 | 4.93 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_10 | 4.86 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_2 | 5.08 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_3 | 4.97 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_4 | 5.15 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_5 | 4.64 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_6 | 4.95 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_7 | 5.05 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_8 | 4.95 | — | ✗ | ✗ |
| claude (claude-sonnet-4-6) | claude_sonnet-4-6_run_9 | 5.03 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 6.64 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 8.58 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 8.38 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 9.93 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 14.95 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 8.05 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 8.56 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 16.93 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 9.99 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 8.03 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 20.21 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 13.82 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 12.63 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 11.90 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 12.51 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 13.26 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 13.12 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 15.02 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 13.54 | — | ✗ | ✗ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 17.00 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 20.94 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 15.20 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 18.84 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 17.91 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 16.67 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 21.43 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 16.42 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 16.07 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 15.99 | — | ✗ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 19.80 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_1 | 3.41 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_10 | 3.66 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_2 | 3.49 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_3 | 1.52 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_4 | 3.04 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_5 | 3.07 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_6 | 4.81 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_7 | 4.22 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_8 | 3.81 | — | ✗ | ✗ |
| openai (gpt-4.1-2025-04-14) | openai_4_1_run_9 | 3.58 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_1 | 2.07 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_10 | 1.66 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_2 | 2.31 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_3 | 2.04 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_4 | 1.49 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_5 | 1.77 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_6 | 1.72 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_7 | 2.36 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_8 | 2.44 | — | ✗ | ✗ |
| openai (gpt-4o-2024-08-06) | openai_default_run_9 | 2.17 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_1 | 2.34 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_10 | 2.22 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_2 | 2.18 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_3 | 2.28 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_4 | 2.16 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_5 | 2.44 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_6 | 2.93 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_7 | 2.21 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_8 | 2.29 | — | ✗ | ✗ |
| openai (gpt-5.2-2025-12-11) | openai_5_2_run_9 | 2.04 | — | ✗ | ✗ |


---

## Overview

- **Chats:** 9 — `multiple_product_multiple_shipment_complex.json`, `multiple_product_multiple_shipment_medium.json`, `multiple_product_multiple_shipment_simple.json`, `single_product_multiple_shipment_complex.json`, `single_product_multiple_shipment_medium.json`, `single_product_multiple_shipment_simple.json`, `single_product_single_shipment_complex.json`, `single_product_single_shipment_medium.json`, `single_product_single_shipment_simple.json`
- **Models:** 10 — `claude (claude-opus-4-5@20251101)`, `claude (claude-opus-4-6)`, `claude (claude-sonnet-4-5@20250929)`, `claude (claude-sonnet-4-6)`, `gemini (google/gemini-2.5-flash)`, `gemini (google/gemini-2.5-pro)`, `gemini (google/gemini-3-flash-preview)`, `openai (gpt-4.1-2025-04-14)`, `openai (gpt-4o-2024-08-06)`, `openai (gpt-5.2-2025-12-11)`
- **Total runs:** 897
- **Correct:** 0 | **Incorrect:** 0 | **N/A:** 897
