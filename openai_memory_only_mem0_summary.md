# Model comparison — Total runs, accuracy & efficiency

Source: `openai_memory_only_mem0.md`

---

## Overview

- **Total runs:** 36
- **Chats:** 12 — `multiple_product_multiple_shipment_complex.json`, `multiple_product_multiple_shipment_medium.json`, `multiple_product_multiple_shipment_simple.json`, `real_world_msgs_test_v1.json`, `real_world_msgs_test_v2.json`, `real_world_msgs_test_v3.json`, `single_product_multiple_shipment_complex.json`, `single_product_multiple_shipment_medium.json`, `single_product_multiple_shipment_simple.json`, `single_product_single_shipment_complex.json`, `single_product_single_shipment_medium.json`, `single_product_single_shipment_simple.json`
- **Models:** 3 — `openai (gpt-4.1-2025-04-14)`, `openai (gpt-4o-2024-08-06)`, `openai (gpt-5.2-2025-12-11)`
- **Correct:** 6 | **Incorrect:** 30 | **N/A:** 0

---

## Total runs by model (accuracy & efficiency)


| Model                       | Total runs | Correct | Incorrect | Failed | N/A | Avg score | Min | Max | Perfect (≥95) | Avg time (s) | Min  | Max  |
| --------------------------- | ---------- | ------- | --------- | ------ | --- | --------- | --- | --- | ------------- | ------------ | ---- | ---- |
| openai (gpt-4.1-2025-04-14) | 12         | 1       | 11        | 0      | 0   | 68.6      | 16  | 99  | 3/12          | 5.59         | 4.24 | 9.79 |
| openai (gpt-4o-2024-08-06)  | 12         | 1       | 11        | 0      | 0   | 46.2      | 9   | 99  | 2/12          | 5.61         | 3.94 | 8.59 |
| openai (gpt-5.2-2025-12-11) | 12         | 4       | 8         | 0      | 0   | 52.5      | 11  | 99  | 4/12          | 5.61         | 4.51 | 7.42 |


**Score:** 0–100 by closeness to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches. **Perfect:** score ≥ 95.

---

## Errors (model mistakes only)

### Incorrect runs (expected vs actual mismatches)

- **openai (gpt-4.1-2025-04-14)** — `multiple_product_multiple_shipment_complex.json` (`openai_4_1_run_1_new`):
  - Contract #1 items: expected 1, got 5
  - Contract #1 item #1 total: expected 276.0, got 3312.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 total: expected 331.2, got 9936.0
  - Contract #2 item #2 total: expected 184.0, got 9200.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-05'
  - Contract #3 item #1 total: expected 8280.0, got 24840.0
- **openai (gpt-4.1-2025-04-14)** — `multiple_product_multiple_shipment_medium.json` (`openai_4_1_run_1_new`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2025-02-28'
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0
  - Contract #2 do_date: expected one of '2026-03-05', got '2025-03-05'
- **openai (gpt-4.1-2025-04-14)** — `multiple_product_multiple_shipment_simple.json` (`openai_4_1_run_1_new`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-02-29'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
- **openai (gpt-4.1-2025-04-14)** — `real_world_msgs_test_v2.json` (`openai_4_1_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-02-29'
  - Contract #2: missing in actual
- **openai (gpt-4.1-2025-04-14)** — `real_world_msgs_test_v3.json` (`openai_4_1_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #2: missing in actual
- **openai (gpt-4.1-2025-04-14)** — `single_product_multiple_shipment_complex.json` (`openai_4_1_run_1_new`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #2: missing in actual
  - Contract #3: missing in actual
- **openai (gpt-4.1-2025-04-14)** — `single_product_multiple_shipment_medium.json` (`openai_4_1_run_1_new`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-02-29'
- **openai (gpt-4.1-2025-04-14)** — `single_product_multiple_shipment_simple.json` (`openai_4_1_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 8.0, got 15.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2: missing in actual
- **openai (gpt-4.1-2025-04-14)** — `single_product_single_shipment_complex.json` (`openai_4_1_run_1_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'
- **openai (gpt-4.1-2025-04-14)** — `single_product_single_shipment_medium.json` (`openai_4_1_run_1_new`):
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-02-29'
- **openai (gpt-4.1-2025-04-14)** — `single_product_single_shipment_simple.json` (`openai_4_1_run_1_new`):
  - Contract #1 do_date: expected one of '2026-11-25', got '2025-11-25'
- **openai (gpt-4o-2024-08-06)** — `multiple_product_multiple_shipment_complex.json` (`openai_default_run_1_new`):
  - Contract count: expected 3, got 2
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 276.0, got 3600.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-02-28'
  - Contract #2 item #1 description: expected 'Assam tea', got 'Red Balloons'
  - Contract #2 item #1 quantity: expected 30.0, got 3000.0
  - Contract #2 item #1 total: expected 331.2, got 27000.0
  - Contract #2 item #2 description: expected 'paper', got 'Sanitizer'
  - Contract #2 item #2 quantity: expected 50.0, got 100.0
  - Contract #2 item #2 total: expected 184.0, got 1000.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2026-03-12'
  - Contract #2 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got 'Changi Hospital Way Singapore 700339'
  - Contract #3: missing in actual
- **openai (gpt-4o-2024-08-06)** — `multiple_product_multiple_shipment_medium.json` (`openai_default_run_1_new`):
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 285.0, got 300.0
  - Contract #2 item #1 total: expected 342.0, got 360.0
  - Contract #2 item #2 total: expected 190.0, got 200.0
- **openai (gpt-4o-2024-08-06)** — `multiple_product_multiple_shipment_simple.json` (`openai_default_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual
- **openai (gpt-4o-2024-08-06)** — `real_world_msgs_test_v1.json` (`openai_default_run_1_new`):
  - Contract #1 item #1 description: expected 'one of ['soy lecithin powder', 'Soy lecithin powder']', got 'KNM Coffee'
  - Contract #1 item #1 quantity: expected 24.0, got 5.0
  - Contract #1 shipping_address: expected one of ['CIF Busan', 'Busan'], got '100 Finance Ave Singapore 018989'
- **openai (gpt-4o-2024-08-06)** — `real_world_msgs_test_v2.json` (`openai_default_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 description: expected 'one of ['BP102']', got 'KNM Coffee'
  - Contract #1 item #1 quantity: expected 23.0, got 5.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-11-25'
  - Contract #1 shipping_address: expected one of ['CIF Busan', 'Busan'], got '100 Finance Ave Singapore 018989'
  - Contract #2: missing in actual
- **openai (gpt-4o-2024-08-06)** — `real_world_msgs_test_v3.json` (`openai_default_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 description: expected 'one of ['lecithin fat powder', 'Lecithin fat powder']', got 'KNM Coffee'
  - Contract #1 item #1 quantity: expected 8.0, got 5.0
  - Contract #1 do_date: expected one of '2026-03-31', got '2026-11-25'
  - Contract #2: missing in actual
- **openai (gpt-4o-2024-08-06)** — `single_product_multiple_shipment_complex.json` (`openai_default_run_1_new`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual
- **openai (gpt-4o-2024-08-06)** — `single_product_multiple_shipment_medium.json` (`openai_default_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 5.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-11-25'
  - Contract #2: missing in actual
- **openai (gpt-4o-2024-08-06)** — `single_product_multiple_shipment_simple.json` (`openai_default_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 8.0, got 5.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-11-25'
  - Contract #2: missing in actual
- **openai (gpt-4o-2024-08-06)** — `single_product_single_shipment_complex.json` (`openai_default_run_1_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'
- **openai (gpt-4o-2024-08-06)** — `single_product_single_shipment_medium.json` (`openai_default_run_1_new`):
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-02-29'
- **openai (gpt-5.2-2025-12-11)** — `multiple_product_multiple_shipment_complex.json` (`openai_5_2_run_1_new`):
  - Contract count: expected 3, got 1
  - Contract #1 items: expected 1, got 5
  - Contract #1 item #1 total: expected 276.0, got 3600.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-03-12'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got 'Changi Hospital Way Singapore 700339'
  - Contract #2: missing in actual
  - Contract #3: missing in actual
- **openai (gpt-5.2-2025-12-11)** — `multiple_product_multiple_shipment_medium.json` (`openai_5_2_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #1 item #1 total: expected 285.0, got 3600.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-05'
  - Contract #2: missing in actual
- **openai (gpt-5.2-2025-12-11)** — `multiple_product_multiple_shipment_simple.json` (`openai_5_2_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-200', got 'PO-2025-11-200'
  - Contract #2: missing in actual
- **openai (gpt-5.2-2025-12-11)** — `real_world_msgs_test_v3.json` (`openai_5_2_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 8.0, got 20.0
  - Contract #1 item #1 total: expected 96000.0, got 240000.0
  - Contract #2: missing in actual
- **openai (gpt-5.2-2025-12-11)** — `single_product_multiple_shipment_complex.json` (`openai_5_2_run_1_new`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual
- **openai (gpt-5.2-2025-12-11)** — `single_product_multiple_shipment_medium.json` (`openai_5_2_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2026-02-28', got '2026-03-31'
  - Contract #2: missing in actual
- **openai (gpt-5.2-2025-12-11)** — `single_product_multiple_shipment_simple.json` (`openai_5_2_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 8.0, got 15.0
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-150', got 'PO-2025-11-150'
  - Contract #2: missing in actual
- **openai (gpt-5.2-2025-12-11)** — `single_product_single_shipment_complex.json` (`openai_5_2_run_1_new`):
  - Contract #1 po_ref_no: expected one of 'PO-2024-11-501', got 'PO-2025-11-501'
  - Contract #1 shipping_address: expected one of ['100 Finance Ave', '100 Finance Ave Singapore 018989'], got '352 Indiana Jones St.'

