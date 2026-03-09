# Model comparison — Accuracy & correctness

Source: `claude_memory_results.md`
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


| Model                               | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min   | Max   |
| ----------------------------------- | ---- | --------- | --- | --- | ------------- | ------------ | ----- | ----- |
| claude (claude-opus-4-5@20251101)   | 10   | 91.0      | 91  | 91  | 0/10          | 15.27        | 14.02 | 16.09 |
| claude (claude-opus-4-6)            | 10   | 90.6      | 15  | 99  | 9/10          | 14.42        | 12.28 | 15.60 |
| claude (claude-sonnet-4-5@20250929) | 10   | 97.0      | 97  | 97  | 10/10         | 16.52        | 15.66 | 17.10 |
| claude (claude-sonnet-4-6)          | 10   | 92.4      | 84  | 98  | 6/10          | 14.26        | 13.23 | 15.41 |


**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)


| Model                               | Run (user_id)            | Time (s) | Score | 3 contracts | C1 correct | C2 correct | C3 correct |
| ----------------------------------- | ------------------------ | -------- | ----- | ----------- | ---------- | ---------- | ---------- |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_1    | 15.16    | 91    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_10   | 15.03    | 91    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_2    | 15.25    | 91    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_3    | 15.60    | 91    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_4    | 16.09    | 91    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_5    | 14.02    | 91    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_6    | 15.37    | 91    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_7    | 14.78    | 91    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_8    | 15.58    | 91    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_9    | 15.85    | 91    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_1    | 14.08    | 99    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_10   | 14.07    | 99    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_2    | 14.56    | 99    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_3    | 14.69    | 99    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_4    | 15.60    | 99    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_5    | 14.61    | 99    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_6    | 15.12    | 99    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_7    | 14.56    | 99    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_8    | 12.28    | 15    | ✗           | ✗          | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_9    | 14.61    | 99    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1  | 16.35    | 97    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 16.12    | 97    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2  | 16.45    | 97    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3  | 16.56    | 97    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4  | 16.91    | 97    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5  | 16.51    | 97    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6  | 15.66    | 97    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7  | 16.48    | 97    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8  | 17.05    | 97    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9  | 17.10    | 97    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_1  | 14.73    | 98    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_10 | 15.02    | 84    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_2  | 14.04    | 98    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_3  | 14.49    | 98    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_4  | 13.78    | 84    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_5  | 13.23    | 98    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_6  | 14.68    | 84    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_7  | 13.58    | 84    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_8  | 13.59    | 98    | ✓           | ✗          | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_9  | 15.41    | 98    | ✓           | ✗          | ✗          | ✗          |


## Chat: multiple_product_multiple_shipment_medium.json

### Ground truth (expected)

- **2 contracts** (expected).
- **Contract 1:** 2025-11-28 — 12 bags KNM Coffee, $25.00/bags, $300.00 total → 100 Finance Ave.
- **Contract 2:** 2025-12-05 — 30 boxes Assam tea, $12.00/boxes, $360.00 total; 50 reams paper, $4.00/reams, $200.00 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)


| Model                               | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min   | Max   |
| ----------------------------------- | ---- | --------- | --- | --- | ------------- | ------------ | ----- | ----- |
| claude (claude-opus-4-5@20251101)   | 10   | 25.0      | 25  | 25  | 0/10          | 9.18         | 8.68  | 9.98  |
| claude (claude-opus-4-6)            | 10   | 23.0      | 23  | 23  | 0/10          | 9.44         | 8.95  | 9.88  |
| claude (claude-sonnet-4-5@20250929) | 10   | 97.4      | 97  | 98  | 10/10         | 10.95        | 10.20 | 11.50 |
| claude (claude-sonnet-4-6)          | 10   | 96.3      | 85  | 100 | 8/10          | 9.43         | 9.08  | 10.04 |


**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)


| Model                               | Run (user_id)            | Time (s) | Score | 2 contracts | C1 correct | C2 correct |
| ----------------------------------- | ------------------------ | -------- | ----- | ----------- | ---------- | ---------- |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_1    | 9.46     | 25    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_10   | 8.85     | 25    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_2    | 9.35     | 25    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_3    | 8.68     | 25    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_4    | 8.82     | 25    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_5    | 8.88     | 25    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_6    | 9.63     | 25    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_7    | 9.04     | 25    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_8    | 9.07     | 25    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_9    | 9.98     | 25    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_1    | 9.64     | 23    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_10   | 9.29     | 23    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_2    | 8.98     | 23    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_3    | 9.88     | 23    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_4    | 9.56     | 23    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_5    | 9.54     | 23    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_6    | 9.61     | 23    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_7    | 8.95     | 23    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_8    | 9.29     | 23    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_9    | 9.63     | 23    | ✗           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1  | 11.10    | 97    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 10.77    | 97    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2  | 11.01    | 97    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3  | 11.48    | 97    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4  | 11.50    | 98    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5  | 11.12    | 98    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6  | 10.20    | 97    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7  | 11.04    | 98    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8  | 10.77    | 98    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9  | 10.48    | 97    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_1  | 9.53     | 100   | ✓           | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_10 | 9.51     | 100   | ✓           | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_2  | 10.04    | 99    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_3  | 9.45     | 85    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_4  | 9.24     | 85    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_5  | 9.52     | 98    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_6  | 9.34     | 98    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_7  | 9.36     | 100   | ✓           | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_8  | 9.18     | 99    | ✓           | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_9  | 9.08     | 99    | ✓           | ✗          | ✗          |


## Chat: multiple_product_multiple_shipment_simple.json

### Ground truth (expected)

- **1 contract** (expected).
- **Contract 1:** 10 bags KNM Coffee, $25.00/bags, $250.00 total; 20 boxes Assam tea, $12.00/boxes, $240.00 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)


| Model                               | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min  | Max   |
| ----------------------------------- | ---- | --------- | --- | --- | ------------- | ------------ | ---- | ----- |
| Claude (opus-4-5)                   | 3    | —         | —   | —   | —             | —            | —    | —     |
| Claude (opus-4-6)                   | 3    | —         | —   | —   | —             | —            | —    | —     |
| Claude (sonnet-4-5)                 | 3    | —         | —   | —   | —             | —            | —    | —     |
| Claude (sonnet-4-6)                 | 2    | —         | —   | —   | —             | —            | —    | —     |
| claude (claude-opus-4-5@20251101)   | 7    | 83.0      | 83  | 83  | 0/7           | 7.79         | 7.25 | 8.44  |
| claude (claude-opus-4-6)            | 7    | 84.7      | 82  | 100 | 1/7           | 9.33         | 7.63 | 17.38 |
| claude (claude-sonnet-4-5@20250929) | 7    | 49.0      | 49  | 49  | 0/7           | 9.21         | 8.52 | 9.74  |
| claude (claude-sonnet-4-6)          | 8    | 41.0      | 41  | 41  | 0/8           | 8.51         | 8.14 | 9.02  |


**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)


| Model                               | Run (user_id)           | Time (s) | Score | 1 contract | C1 correct |
| ----------------------------------- | ----------------------- | -------- | ----- | ---------- | ---------- |
| Claude (opus-4-5)                   | (failed)                | —        | —     | ✗          | ✗          |
| Claude (opus-4-5)                   | (failed)                | —        | —     | ✗          | ✗          |
| Claude (opus-4-5)                   | (failed)                | —        | —     | ✗          | ✗          |
| Claude (opus-4-6)                   | (failed)                | —        | —     | ✗          | ✗          |
| Claude (opus-4-6)                   | (failed)                | —        | —     | ✗          | ✗          |
| Claude (opus-4-6)                   | (failed)                | —        | —     | ✗          | ✗          |
| Claude (sonnet-4-5)                 | (failed)                | —        | —     | ✗          | ✗          |
| Claude (sonnet-4-5)                 | (failed)                | —        | —     | ✗          | ✗          |
| Claude (sonnet-4-5)                 | (failed)                | —        | —     | ✗          | ✗          |
| Claude (sonnet-4-6)                 | (failed)                | —        | —     | ✗          | ✗          |
| Claude (sonnet-4-6)                 | (failed)                | —        | —     | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_1   | 7.94     | 83    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_2   | 7.91     | 83    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_3   | 7.25     | 83    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_4   | 7.58     | 83    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_5   | 7.84     | 83    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_6   | 7.60     | 83    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_7   | 8.44     | 83    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_1   | 8.42     | 82    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_2   | 17.38    | 100   | ✓          | ✓          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_3   | 8.02     | 82    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_4   | 8.03     | 82    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_5   | 7.78     | 82    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_6   | 8.03     | 82    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_7   | 7.63     | 83    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1 | 9.74     | 49    | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2 | 9.59     | 49    | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3 | 9.03     | 49    | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4 | 8.52     | 49    | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5 | 8.77     | 49    | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6 | 9.62     | 49    | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7 | 9.17     | 49    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_1 | 8.14     | 41    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_2 | 9.00     | 41    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_3 | 8.38     | 41    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_4 | 8.28     | 41    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_5 | 9.02     | 41    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_6 | 8.50     | 41    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_7 | 8.32     | 41    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_8 | 8.41     | 41    | ✗          | ✗          |


## Chat: single_product_multiple_shipment_complex.json

### Ground truth (expected)

- **3 contracts** (expected).
- **Contract 1:** 2025-11-28 — 14 bags KNM Coffee, $22.75/bags, $318.50 total → 100 Finance Ave.
- **Contract 2:** 2025-12-04 — 10 bags KNM Coffee, $22.75/bags, $227.50 total → 200 Warehouse Lane.
- **Contract 3:** 2025-12-10 — 8 bags KNM Coffee, $22.75/bags, $182.00 total → 15 New Branch Rd.

---

### Summary by model (accuracy & latency)


| Model               | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
| ------------------- | ---- | --------- | --- | --- | ------------- | ------------ | --- | --- |
| Claude (opus-4-5)   | 10   | —         | —   | —   | —             | —            | —   | —   |
| Claude (opus-4-6)   | 10   | —         | —   | —   | —             | —            | —   | —   |
| Claude (sonnet-4-5) | 10   | —         | —   | —   | —             | —            | —   | —   |
| Claude (sonnet-4-6) | 10   | —         | —   | —   | —             | —            | —   | —   |


**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)


| Model               | Run (user_id) | Time (s) | Score | 3 contracts | C1 correct | C2 correct | C3 correct |
| ------------------- | ------------- | -------- | ----- | ----------- | ---------- | ---------- | ---------- |
| Claude (opus-4-5)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-5)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-5)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-5)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-5)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-5)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-5)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-5)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-5)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-5)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-6)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-6)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-6)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-6)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-6)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-6)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-6)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-6)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-6)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (opus-4-6)   | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-5) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-5) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-5) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-5) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-5) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-5) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-5) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-5) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-5) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-5) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-6) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-6) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-6) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-6) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-6) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-6) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-6) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-6) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-6) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |
| Claude (sonnet-4-6) | (failed)      | —        | —     | ✗           | ✗          | ✗          | ✗          |


## Chat: single_product_multiple_shipment_medium.json

### Ground truth (expected)

- **2 contracts** (expected).
- **Contract 1:** 2025-11-28 — 12 bags KNM Coffee, $23.75/bags, $285.00 total → 100 Finance Ave.
- **Contract 2:** 2025-12-06 — 8 bags KNM Coffee, $23.75/bags, $190.00 total → 50 Changi Business Park.

---

### Summary by model (accuracy & latency)


| Model                               | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min  | Max   |
| ----------------------------------- | ---- | --------- | --- | --- | ------------- | ------------ | ---- | ----- |
| Claude (opus-4-5)                   | 4    | —         | —   | —   | —             | —            | —    | —     |
| Claude (opus-4-6)                   | 3    | —         | —   | —   | —             | —            | —    | —     |
| Claude (sonnet-4-5)                 | 4    | —         | —   | —   | —             | —            | —    | —     |
| Claude (sonnet-4-6)                 | 4    | —         | —   | —   | —             | —            | —    | —     |
| claude (claude-opus-4-5@20251101)   | 6    | 99.0      | 99  | 99  | 6/6           | 9.42         | 8.87 | 10.37 |
| claude (claude-opus-4-6)            | 7    | 28.0      | 28  | 28  | 0/7           | 9.17         | 8.63 | 10.78 |
| claude (claude-sonnet-4-5@20250929) | 6    | 26.0      | 26  | 26  | 0/6           | 8.03         | 7.15 | 9.32  |
| claude (claude-sonnet-4-6)          | 6    | 95.2      | 89  | 99  | 4/6           | 9.34         | 8.44 | 10.32 |


**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)


| Model                               | Run (user_id)            | Time (s) | Score | 2 contracts | C1 correct | C2 correct |
| ----------------------------------- | ------------------------ | -------- | ----- | ----------- | ---------- | ---------- |
| Claude (opus-4-5)                   | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (opus-4-5)                   | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (opus-4-5)                   | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (opus-4-5)                   | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (opus-4-6)                   | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (opus-4-6)                   | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (opus-4-6)                   | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (sonnet-4-5)                 | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (sonnet-4-5)                 | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (sonnet-4-5)                 | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (sonnet-4-5)                 | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (sonnet-4-6)                 | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (sonnet-4-6)                 | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (sonnet-4-6)                 | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| Claude (sonnet-4-6)                 | (failed)                 | —        | —     | ✗           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_10   | 9.52     | 99    | ✓           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_5    | 10.37    | 99    | ✓           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_6    | 8.98     | 99    | ✓           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_7    | 8.90     | 99    | ✓           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_8    | 9.88     | 99    | ✓           | ✗          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_9    | 8.87     | 99    | ✓           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_10   | 8.81     | 28    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_4    | 10.78    | 28    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_5    | 8.63     | 28    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_6    | 8.69     | 28    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_7    | 9.34     | 28    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_8    | 8.95     | 28    | ✗           | ✗          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_9    | 9.02     | 28    | ✗           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 8.58     | 26    | ✗           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5  | 9.32     | 26    | ✗           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6  | 7.15     | 26    | ✗           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7  | 7.29     | 26    | ✗           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8  | 7.88     | 26    | ✗           | ✗          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9  | 7.98     | 26    | ✗           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_10 | 8.80     | 98    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_5  | 10.32    | 89    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_6  | 8.91     | 99    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_7  | 9.35     | 98    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_8  | 10.21    | 89    | ✓           | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_9  | 8.44     | 98    | ✓           | ✗          | ✗          |


## Chat: single_product_multiple_shipment_simple.json

### Ground truth (expected)

- **1 contract** (expected).
- **Contract 1:** 15 bags KNM Coffee, $25.00/bags, $375.00 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)


| Model                               | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min  | Max   |
| ----------------------------------- | ---- | --------- | --- | --- | ------------- | ------------ | ---- | ----- |
| claude (claude-opus-4-5@20251101)   | 10   | 74.0      | 74  | 74  | 0/10          | 8.54         | 7.52 | 13.19 |
| claude (claude-opus-4-6)            | 10   | 100.0     | 100 | 100 | 10/10         | 8.39         | 7.12 | 13.21 |
| claude (claude-sonnet-4-5@20250929) | 10   | 99.0      | 99  | 99  | 10/10         | 7.77         | 7.11 | 8.56  |
| claude (claude-sonnet-4-6)          | 10   | 62.0      | 62  | 62  | 0/10          | 8.67         | 7.97 | 9.72  |


**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)


| Model                               | Run (user_id)            | Time (s) | Score | 1 contract | C1 correct |
| ----------------------------------- | ------------------------ | -------- | ----- | ---------- | ---------- |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_1    | 7.52     | 74    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_10   | 7.89     | 74    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_2    | 7.68     | 74    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_3    | 7.52     | 74    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_4    | 13.19    | 74    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_5    | 9.32     | 74    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_6    | 8.15     | 74    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_7    | 8.40     | 74    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_8    | 7.63     | 74    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_9    | 8.08     | 74    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_1    | 7.75     | 100   | ✓          | ✓          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_10   | 7.44     | 100   | ✓          | ✓          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_2    | 8.12     | 100   | ✓          | ✓          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_3    | 7.61     | 100   | ✓          | ✓          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_4    | 7.54     | 100   | ✓          | ✓          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_5    | 7.89     | 100   | ✓          | ✓          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_6    | 9.46     | 100   | ✓          | ✓          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_7    | 7.12     | 100   | ✓          | ✓          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_8    | 7.80     | 100   | ✓          | ✓          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_9    | 13.21    | 100   | ✓          | ✓          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1  | 7.62     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 7.11     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2  | 7.39     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3  | 8.41     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4  | 7.69     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5  | 8.56     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6  | 7.71     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7  | 7.29     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8  | 8.06     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9  | 7.86     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_1  | 8.24     | 62    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_10 | 9.23     | 62    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_2  | 8.86     | 62    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_3  | 8.37     | 62    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_4  | 7.97     | 62    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_5  | 8.41     | 62    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_6  | 8.65     | 62    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_7  | 9.22     | 62    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_8  | 9.72     | 62    | ✗          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_9  | 8.07     | 62    | ✗          | ✗          |


## Chat: single_product_single_shipment_complex.json

### Ground truth (expected)

- **1 contract** (expected).
- **Contract 1:** 2025-11-28 — 10 bags KNM Coffee, $23.75/bags, $237.50 total → 100 Finance Ave.

---

### Summary by model (accuracy & latency)


| Model                               | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min  | Max   |
| ----------------------------------- | ---- | --------- | --- | --- | ------------- | ------------ | ---- | ----- |
| claude (claude-opus-4-5@20251101)   | 10   | 99.0      | 99  | 99  | 10/10         | 9.38         | 7.65 | 10.37 |
| claude (claude-opus-4-6)            | 10   | 99.0      | 99  | 99  | 10/10         | 9.36         | 7.99 | 10.38 |
| claude (claude-sonnet-4-5@20250929) | 10   | 99.0      | 99  | 99  | 10/10         | 9.43         | 8.04 | 10.91 |
| claude (claude-sonnet-4-6)          | 10   | 98.0      | 98  | 98  | 10/10         | 9.17         | 7.35 | 13.98 |


**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)


| Model                               | Run (user_id)            | Time (s) | Score | 1 contract | C1 correct |
| ----------------------------------- | ------------------------ | -------- | ----- | ---------- | ---------- |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_1    | 7.77     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_10   | 10.37    | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_2    | 7.65     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_3    | 9.51     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_4    | 9.98     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_5    | 9.14     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_6    | 9.85     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_7    | 9.85     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_8    | 9.35     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_9    | 10.35    | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_1    | 8.01     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_10   | 10.09    | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_2    | 7.99     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_3    | 9.75     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_4    | 9.20     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_5    | 9.46     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_6    | 10.38    | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_7    | 9.22     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_8    | 9.68     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_9    | 9.79     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1  | 8.04     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 9.29     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2  | 8.04     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3  | 8.86     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4  | 9.76     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5  | 10.91    | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6  | 9.82     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7  | 10.02    | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8  | 9.57     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9  | 9.96     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_1  | 8.27     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_10 | 8.37     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_2  | 8.95     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_3  | 7.35     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_4  | 13.98    | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_5  | 9.56     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_6  | 8.12     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_7  | 9.08     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_8  | 8.46     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_9  | 9.58     | 98    | ✓          | ✗          |


## Chat: single_product_single_shipment_medium.json

### Ground truth (expected)

- **1 contract** (expected).
- **Contract 1:** 2025-11-28 — 8 bags KNM Coffee, $23.75/bags, $190.00 total → 100 Finance Ave Singapore 018989.

---

### Summary by model (accuracy & latency)


| Model                               | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min  | Max   |
| ----------------------------------- | ---- | --------- | --- | --- | ------------- | ------------ | ---- | ----- |
| claude (claude-opus-4-5@20251101)   | 10   | 99.0      | 99  | 99  | 10/10         | 7.91         | 6.84 | 12.50 |
| claude (claude-opus-4-6)            | 10   | 99.0      | 99  | 99  | 10/10         | 8.07         | 7.48 | 8.60  |
| claude (claude-sonnet-4-5@20250929) | 10   | 99.0      | 99  | 99  | 10/10         | 7.57         | 7.14 | 8.03  |
| claude (claude-sonnet-4-6)          | 10   | 98.5      | 98  | 99  | 10/10         | 7.48         | 6.50 | 12.46 |


**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)


| Model                               | Run (user_id)            | Time (s) | Score | 1 contract | C1 correct |
| ----------------------------------- | ------------------------ | -------- | ----- | ---------- | ---------- |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_1    | 7.44     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_10   | 7.76     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_2    | 7.03     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_3    | 7.48     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_4    | 7.25     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_5    | 12.50    | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_6    | 6.84     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_7    | 7.36     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_8    | 7.50     | 99    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_9    | 7.91     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_1    | 7.76     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_10   | 8.43     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_2    | 8.15     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_3    | 7.94     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_4    | 7.48     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_5    | 8.12     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_6    | 8.60     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_7    | 7.72     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_8    | 7.94     | 99    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_9    | 8.60     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1  | 7.90     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 7.19     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2  | 7.73     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3  | 7.34     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4  | 7.14     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5  | 7.40     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6  | 7.93     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7  | 7.45     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8  | 7.58     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9  | 8.03     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_1  | 6.97     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_10 | 7.28     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_2  | 6.78     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_3  | 12.46    | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_4  | 6.73     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_5  | 6.80     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_6  | 6.93     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_7  | 6.50     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_8  | 7.43     | 99    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_9  | 6.93     | 98    | ✓          | ✗          |


## Chat: single_product_single_shipment_simple.json

### Ground truth (expected)

- **1 contract** (expected).
- **Contract 1:** 2025-11-25 — 5 bags KNM Coffee, $25.00/bags, $125.00 total → 100 Finance Ave Singapore 018989.

---

### Summary by model (accuracy & latency)


| Model                               | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min  | Max   |
| ----------------------------------- | ---- | --------- | --- | --- | ------------- | ------------ | ---- | ----- |
| claude (claude-opus-4-5@20251101)   | 10   | 98.0      | 98  | 98  | 10/10         | 7.46         | 6.81 | 8.34  |
| claude (claude-opus-4-6)            | 10   | 98.0      | 98  | 98  | 10/10         | 7.27         | 7.15 | 7.47  |
| claude (claude-sonnet-4-5@20250929) | 10   | 98.0      | 98  | 98  | 10/10         | 7.27         | 6.78 | 7.69  |
| claude (claude-sonnet-4-6)          | 10   | 98.3      | 98  | 99  | 10/10         | 7.18         | 6.24 | 12.06 |


**Score:** 0–100 by **closeness** to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches (e.g. numeric within %, string similarity).
**Perfect:** run with score ≥ 95.

---

### Per-run correctness (all runs)


| Model                               | Run (user_id)            | Time (s) | Score | 1 contract | C1 correct |
| ----------------------------------- | ------------------------ | -------- | ----- | ---------- | ---------- |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_1    | 7.31     | 98    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_10   | 7.04     | 98    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_2    | 7.06     | 98    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_3    | 7.99     | 98    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_4    | 7.41     | 98    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_5    | 7.84     | 98    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_6    | 8.34     | 98    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_7    | 7.44     | 98    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_8    | 7.31     | 98    | ✓          | ✗          |
| claude (claude-opus-4-5@20251101)   | claude_opus-4-5_run_9    | 6.81     | 98    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_1    | 7.38     | 98    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_10   | 7.28     | 98    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_2    | 7.33     | 98    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_3    | 7.47     | 98    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_4    | 7.15     | 98    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_5    | 7.18     | 98    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_6    | 7.29     | 98    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_7    | 7.25     | 98    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_8    | 7.15     | 98    | ✓          | ✗          |
| claude (claude-opus-4-6)            | claude_opus-4-6_run_9    | 7.22     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_1  | 7.23     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_10 | 6.95     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_2  | 6.78     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_3  | 7.69     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_4  | 7.49     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_5  | 7.11     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_6  | 7.06     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_7  | 7.49     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_8  | 7.36     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-5@20250929) | claude_sonnet-4-5_run_9  | 7.54     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_1  | 6.81     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_10 | 6.27     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_2  | 6.35     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_3  | 6.24     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_4  | 7.85     | 99    | ✓          | ✓          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_5  | 6.47     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_6  | 6.48     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_7  | 6.65     | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_8  | 12.06    | 98    | ✓          | ✗          |
| claude (claude-sonnet-4-6)          | claude_sonnet-4-6_run_9  | 6.64     | 99    | ✓          | ✓          |


---

## Overview

- **Chats:** 9 — `multiple_product_multiple_shipment_complex.json`, `multiple_product_multiple_shipment_medium.json`, `multiple_product_multiple_shipment_simple.json`, `single_product_multiple_shipment_complex.json`, `single_product_multiple_shipment_medium.json`, `single_product_multiple_shipment_simple.json`, `single_product_single_shipment_complex.json`, `single_product_single_shipment_medium.json`, `single_product_single_shipment_simple.json`
- **Models:** 8 — `Claude (opus-4-5)`, `Claude (opus-4-6)`, `Claude (sonnet-4-5)`, `Claude (sonnet-4-6)`, `claude (claude-opus-4-5@20251101)`, `claude (claude-opus-4-6)`, `claude (claude-sonnet-4-5@20250929)`, `claude (claude-sonnet-4-6)`
- **Total runs:** 360
- **Correct:** 24 | **Incorrect:** 270 | **N/A:** 0
- **Failed (run_all):** 66

---

## Failed runs (run_all)

- **multiple_product_multiple_shipment_simple.json** — **Claude (opus-4-5)**
- **multiple_product_multiple_shipment_simple.json** — **Claude (opus-4-5)**
- **multiple_product_multiple_shipment_simple.json** — **Claude (opus-4-5)**
- **multiple_product_multiple_shipment_simple.json** — **Claude (opus-4-6)**
- **multiple_product_multiple_shipment_simple.json** — **Claude (opus-4-6)**
- **multiple_product_multiple_shipment_simple.json** — **Claude (opus-4-6)**
- **multiple_product_multiple_shipment_simple.json** — **Claude (sonnet-4-5)**
- **multiple_product_multiple_shipment_simple.json** — **Claude (sonnet-4-5)**
- **multiple_product_multiple_shipment_simple.json** — **Claude (sonnet-4-5)**
- **multiple_product_multiple_shipment_simple.json** — **Claude (sonnet-4-6)**
- **multiple_product_multiple_shipment_simple.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_complex.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_medium.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_medium.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_medium.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_medium.json** — **Claude (opus-4-5)**
- **single_product_multiple_shipment_medium.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_medium.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_medium.json** — **Claude (opus-4-6)**
- **single_product_multiple_shipment_medium.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_medium.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_medium.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_medium.json** — **Claude (sonnet-4-5)**
- **single_product_multiple_shipment_medium.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_medium.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_medium.json** — **Claude (sonnet-4-6)**
- **single_product_multiple_shipment_medium.json** — **Claude (sonnet-4-6)**

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
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_8`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 4
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-12'
  - Contract #2: missing in actual
  - Contract #3: missing in actual
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2024-12-12'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
  - Contract #3 shipping_address: expected one of ['Changi Hospital Way Singapore 700339', 'Changi Hospital Wars 24 Singapore 700339'], got 'Changi Hospital Way, Singapore 700339'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
- **multiple_product_multiple_shipment_complex.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 red, 1500 white)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
  - Contract #3 shipping_address: expected one of ['Changi Hospital Way Singapore 700339', 'Changi Hospital Wars 24 Singapore 700339'], got 'Changi Hospital Way, Singapore 700339, +65 9876 5432'
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
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
  - Contract #3 item #1 description: expected 'Red Balloons', got 'Red Balloons (1500 Red, 1500 White)'
  - Contract #3 do_date: expected one of '2025-12-12', got '2026-12-12'
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
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2: missing in actual
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
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
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-05'
  - Contract #2: missing in actual
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_10`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-12-05'
  - Contract #2: missing in actual
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_2`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-05'
  - Contract #2: missing in actual
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_3`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-05'
  - Contract #2: missing in actual
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_4`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-05'
  - Contract #2: missing in actual
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_5`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-05'
  - Contract #2: missing in actual
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_6`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-05'
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
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_3`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_4`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
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
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 description: expected 'paper', got 'copy paper'
  - Contract #2 item #2 total: expected 200.0, got 190.0
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
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_4`):
  - Contract #1 item #1 total: expected 300.0, got 3600.0
  - Contract #2 item #1 total: expected 360.0, got 10800.0
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 item #2 total: expected 200.0, got 10000.0
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2024-12-05'
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
- **multiple_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 item #2 description: expected 'paper', got 'Copy Paper'
  - Contract #2 do_date: expected one of '2025-12-05', got '2026-12-05'
- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
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
- **multiple_product_multiple_shipment_simple.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_1`):
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
- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_1`):
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
- **multiple_product_multiple_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_1`):
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
- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-opus-4-6)** (`claude_opus-4-6_run_10`):
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
- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_10`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-06'
  - Contract #2: missing in actual
- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-5@20250929)** (`claude_sonnet-4-5_run_5`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-12-06'
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
- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
- **single_product_multiple_shipment_medium.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
  - Contract #2 do_date: expected one of '2025-12-06', got '2026-12-06'
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
- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_complex.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
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
- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_1`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_10`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_2`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_3`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_4`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_5`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_6`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_7`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_8`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2026-11-28'
- **single_product_single_shipment_medium.json** — **claude (claude-opus-4-5@20251101)** (`claude_opus-4-5_run_9`):
  - Contract #1 do_date: expected one of '2025-11-28', got '2024-11-28'
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
- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_10`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'
- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_2`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'
- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_3`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'
- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_5`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'
- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_6`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'
- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_7`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'
- **single_product_single_shipment_simple.json** — **claude (claude-sonnet-4-6)** (`claude_sonnet-4-6_run_8`):
  - Contract #1 do_date: expected one of '2025-11-25', got '2026-11-25'

