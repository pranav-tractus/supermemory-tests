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

