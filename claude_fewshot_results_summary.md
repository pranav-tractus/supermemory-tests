# Model comparison — Total runs, accuracy & efficiency

Source: `claude_fewshot_results.md`

---

## Overview

- **Total runs:** 596
- **Chats:** 15 — `multiple_product_multiple_shipment_complex.json`, `multiple_product_multiple_shipment_medium.json`, `multiple_product_multiple_shipment_simple.json`, `multiple_products_multiple_shipments.json`, `real_world_msgs_test_v1.json`, `real_world_msgs_test_v2.json`, `real_world_msgs_test_v3.json`, `single_product_multiple_shipment_complex.json`, `single_product_multiple_shipment_medium.json`, `single_product_multiple_shipment_simple.json`, `single_product_multiple_shipments.json`, `single_product_single_shipment.json`, `single_product_single_shipment_complex.json`, `single_product_single_shipment_medium.json`, `single_product_single_shipment_simple.json`
- **Models:** 4 — `claude (claude-opus-4-5@20251101)`, `claude (claude-opus-4-6)`, `claude (claude-sonnet-4-5@20250929)`, `claude (claude-sonnet-4-6)`

- **Correct:** 308 | **Incorrect:** 288 | **N/A:** 0

---

## Total runs by model (accuracy & efficiency)

| Model | Total runs | Correct | Incorrect | Failed | N/A | Avg score | Min | Max | Perfect (≥95) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 150 | 82 | 68 | 0 | 0 | 92.7 | 26 | 100 | 110/150 | 7.85 | 4.44 | 48.74 |
| claude (claude-opus-4-6) | 150 | 80 | 70 | 0 | 0 | 92.4 | 26 | 100 | 105/150 | 8.55 | 5.00 | 20.90 |
| claude (claude-sonnet-4-5@20250929) | 147 | 77 | 70 | 0 | 0 | 87.5 | 14 | 100 | 99/147 | 7.40 | 4.05 | 14.51 |
| claude (claude-sonnet-4-6) | 149 | 69 | 80 | 0 | 0 | 92.6 | 24 | 100 | 109/149 | 7.02 | 4.19 | 16.54 |

**Score:** 0–100 by closeness to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches. **Perfect:** score ≥ 95.

---

## Errors (model mistakes only)

### Incorrect runs (expected vs actual mismatches)

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_10_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_1_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_2_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_3_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4140.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4140.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_4_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_5_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_6_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_7_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_8_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_9_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_medium.json` (`claude_opus-4-5_run_10_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_medium.json` (`claude_opus-4-5_run_1_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_medium.json` (`claude_opus-4-5_run_2_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_medium.json` (`claude_opus-4-5_run_3_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_medium.json` (`claude_opus-4-5_run_6_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_medium.json` (`claude_opus-4-5_run_7_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_medium.json` (`claude_opus-4-5_run_8_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_medium.json` (`claude_opus-4-5_run_9_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_10_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_2_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_3_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_4_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_5_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_6_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_7_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_8_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_9_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_10_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_1_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_2_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_3_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_4_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_5_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_6_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_7_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_8_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_9_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_10_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_1_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_2_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_3_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_4_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_5_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_6_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_7_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_8_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_9_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_10_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_1_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_2_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_3_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_4_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_5_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_6_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_7_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_8_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_9_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-5@20251101)** — `single_product_single_shipment_complex.json` (`claude_opus-4-5_run_10_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-5@20251101)** — `single_product_single_shipment_complex.json` (`claude_opus-4-5_run_1_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-5@20251101)** — `single_product_single_shipment_complex.json` (`claude_opus-4-5_run_2_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-5@20251101)** — `single_product_single_shipment_complex.json` (`claude_opus-4-5_run_3_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-5@20251101)** — `single_product_single_shipment_complex.json` (`claude_opus-4-5_run_4_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-5@20251101)** — `single_product_single_shipment_complex.json` (`claude_opus-4-5_run_5_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-5@20251101)** — `single_product_single_shipment_complex.json` (`claude_opus-4-5_run_6_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-5@20251101)** — `single_product_single_shipment_complex.json` (`claude_opus-4-5_run_7_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-5@20251101)** — `single_product_single_shipment_complex.json` (`claude_opus-4-5_run_8_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-5@20251101)** — `single_product_single_shipment_complex.json` (`claude_opus-4-5_run_9_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_10_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_1_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_2_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_3_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_4_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_5_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_6_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_7_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_8_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_9_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_10_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_1_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_2_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_3_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_4_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_5_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_6_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_7_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_8_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_9_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-opus-4-6)** — `multiple_products_multiple_shipments.json` (`claude_opus-4-6_run_10_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `multiple_products_multiple_shipments.json` (`claude_opus-4-6_run_1_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `multiple_products_multiple_shipments.json` (`claude_opus-4-6_run_2_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `multiple_products_multiple_shipments.json` (`claude_opus-4-6_run_3_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `multiple_products_multiple_shipments.json` (`claude_opus-4-6_run_4_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `multiple_products_multiple_shipments.json` (`claude_opus-4-6_run_5_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `multiple_products_multiple_shipments.json` (`claude_opus-4-6_run_6_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `multiple_products_multiple_shipments.json` (`claude_opus-4-6_run_7_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `multiple_products_multiple_shipments.json` (`claude_opus-4-6_run_8_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `multiple_products_multiple_shipments.json` (`claude_opus-4-6_run_9_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_10_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_1_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_2_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_3_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_4_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_5_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_6_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_7_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_8_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_9_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_10_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_1_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_2_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_3_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_4_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_5_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_6_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_7_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_8_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_9_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_10_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_1_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_2_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_3_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_4_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_5_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_6_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_7_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_8_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_9_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-opus-4-6)** — `single_product_single_shipment_complex.json` (`claude_opus-4-6_run_10_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-6)** — `single_product_single_shipment_complex.json` (`claude_opus-4-6_run_1_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-6)** — `single_product_single_shipment_complex.json` (`claude_opus-4-6_run_2_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-6)** — `single_product_single_shipment_complex.json` (`claude_opus-4-6_run_3_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-6)** — `single_product_single_shipment_complex.json` (`claude_opus-4-6_run_4_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-6)** — `single_product_single_shipment_complex.json` (`claude_opus-4-6_run_5_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-6)** — `single_product_single_shipment_complex.json` (`claude_opus-4-6_run_6_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-6)** — `single_product_single_shipment_complex.json` (`claude_opus-4-6_run_7_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-6)** — `single_product_single_shipment_complex.json` (`claude_opus-4-6_run_8_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-opus-4-6)** — `single_product_single_shipment_complex.json` (`claude_opus-4-6_run_9_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_10_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 item #1 total: expected 8280.0, got 9000.0
  - Contract #3 item #2 total: expected 920.0, got 1000.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_2_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_3_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_4_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 item #1 total: expected 8280.0, got 9000.0
  - Contract #3 item #2 total: expected 920.0, got 1000.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_5_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_6_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_7_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 items: expected 2, got 3
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 8280.0, got 4500.0
  - Contract #3 item #2 description: expected 'Sanitizer', got 'White Balloons'
  - Contract #3 item #2 quantity: expected 100.0, got 1500.0
  - Contract #3 item #2 total: expected 920.0, got 4500.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_8_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 item #1 total: expected 8280.0, got 9000.0
  - Contract #3 item #2 total: expected 920.0, got 1000.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_9_new`):
  - Contract #1 item #1 total: expected 276.0, got 300.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 360.0
  - Contract #2 item #2 total: expected 184.0, got 200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 item #1 total: expected 8280.0, got 9000.0
  - Contract #3 item #2 total: expected 920.0, got 1000.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-5_run_10_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-5_run_2_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-5_run_3_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-5_run_4_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-5_run_5_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-5_run_7_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-5_run_8_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_10_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_2_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_3_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_4_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_5_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_6_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_7_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_8_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_9_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-5_run_10_new`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2026-03-31', got '2026-11-30'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-5_run_2_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-5_run_4_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-5_run_5_new`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2026-03-31', got '2026-11-30'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-5_run_6_new`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 do_date: expected one of '2026-03-31', got '2026-11-30'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-5_run_8_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-5_run_9_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `real_world_msgs_test_v1.json` (`claude_sonnet-4-5_run_3_new`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 24.0, got 12.0
  - Contract #1 item #1 total: expected 98400.0, got 49200.0

- **claude (claude-sonnet-4-5@20250929)** — `real_world_msgs_test_v1.json` (`claude_sonnet-4-5_run_4_new`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 24.0, got 12.0
  - Contract #1 item #1 total: expected 98400.0, got 49200.0

- **claude (claude-sonnet-4-5@20250929)** — `real_world_msgs_test_v1.json` (`claude_sonnet-4-5_run_6_new`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 24.0, got 12.0
  - Contract #1 item #1 total: expected 98400.0, got 49200.0

- **claude (claude-sonnet-4-5@20250929)** — `real_world_msgs_test_v1.json` (`claude_sonnet-4-5_run_7_new`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 24.0, got 12.0
  - Contract #1 item #1 total: expected 98400.0, got 49200.0

- **claude (claude-sonnet-4-5@20250929)** — `real_world_msgs_test_v1.json` (`claude_sonnet-4-5_run_9_new`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 24.0, got 12.0
  - Contract #1 item #1 total: expected 98400.0, got 49200.0

- **claude (claude-sonnet-4-5@20250929)** — `real_world_msgs_test_v2.json` (`claude_sonnet-4-5_run_8_new`):
  - Contract #1 shipping_address: expected one of ['CIF Busan', 'Busan'], got 'Test Customer'
  - Contract #2 shipping_address: expected one of ['CIF Busan', 'Busan'], got 'Test Customer'

- **claude (claude-sonnet-4-5@20250929)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_10_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_2_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_3_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_4_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_5_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_6_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_7_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_8_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_9_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_10_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_2_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_3_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_4_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_5_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_7_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_8_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_9_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_10_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_2_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_3_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_4_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_5_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St., Gate B, Contact: +65 9123 4567'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_6_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_7_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_8_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_9_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_10_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_2_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_3_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_4_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_5_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_6_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_7_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_8_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_9_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-6_run_2_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-6_run_3_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-6_run_4_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-6_run_5_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-6_run_6_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-6_run_7_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-6_run_8_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-6_run_9_new`):
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_10_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-02-25'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_2_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_3_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_4_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_5_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_6_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-02-25'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_7_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_8_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_9_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 item #1 total: expected 240.0, got 4800.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'

- **claude (claude-sonnet-4-6)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-6_run_10_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-6_run_2_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-6_run_3_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-6_run_4_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-6_run_5_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-6_run_6_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-6_run_7_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-6_run_8_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-6)** — `multiple_products_multiple_shipments.json` (`claude_sonnet-4-6_run_9_new`):
  - Contract count: expected 3, got 2
  - Contract #2 items: expected 1, got 2
  - Contract #3: missing in actual

- **claude (claude-sonnet-4-6)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-6_run_10_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-6)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-6)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-6_run_2_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-6)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-6_run_3_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-6)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-6_run_4_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-6)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-6_run_5_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-6)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-6_run_6_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-6)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-6_run_7_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-6)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-6_run_8_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-6)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-6_run_9_new`):
  - Contract #2 do_date: expected one of '2026-05-31', got '2027-05-31'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_10_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_2_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_3_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_4_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_5_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_6_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_7_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_8_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-6_run_9_new`):
  - Contract #2 do_date: expected one of '2026-03-12', got '2026-03-04'
  - Contract #3 do_date: expected one of '2026-03-18', got '2026-03-10'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_10_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_2_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_3_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_4_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_5_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_6_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_7_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_8_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_9_new`):
  - Contract #1 item #1 total: expected 375.0, got 200.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2 item #1 total: expected 375.0, got 175.0
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_10_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_2_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_3_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_4_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_5_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_6_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_7_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_8_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_9_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_medium.json` (`claude_sonnet-4-6_run_4_new`):
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-02-25'

