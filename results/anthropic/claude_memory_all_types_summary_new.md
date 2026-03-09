# Model comparison — Total runs, accuracy & efficiency

Source: `claude_memory_all_types_results.md`

---

## Overview

- **Total runs:** 60
- **Chats:** 15 — `multiple_product_multiple_shipment_complex.json`, `multiple_product_multiple_shipment_medium.json`, `multiple_product_multiple_shipment_simple.json`, `multiple_products_multiple_shipments.json`, `real_world_msgs_test_v1.json`, `real_world_msgs_test_v2.json`, `real_world_msgs_test_v3.json`, `single_product_multiple_shipment_complex.json`, `single_product_multiple_shipment_medium.json`, `single_product_multiple_shipment_simple.json`, `single_product_multiple_shipments.json`, `single_product_single_shipment.json`, `single_product_single_shipment_complex.json`, `single_product_single_shipment_medium.json`, `single_product_single_shipment_simple.json`
- **Models:** 4 — `claude (claude-opus-4-5@20251101)`, `claude (claude-opus-4-6)`, `claude (claude-sonnet-4-5@20250929)`, `claude (claude-sonnet-4-6)`

- **Correct:** 31 | **Incorrect:** 29 | **N/A:** 0

---

## Total runs by model (accuracy & efficiency)

| Model | Total runs | Correct | Incorrect | Failed | N/A | Avg score | Min | Max | Perfect (≥95) | Avg time (s) | Min | Max |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| claude (claude-opus-4-5@20251101) | 15 | 7 | 8 | 0 | 0 | 74.9 | 19 | 100 | 8/15 | 8.72 | 6.57 | 14.82 |
| claude (claude-opus-4-6) | 15 | 8 | 7 | 0 | 0 | 69.9 | 15 | 100 | 8/15 | 8.56 | 6.61 | 13.10 |
| claude (claude-sonnet-4-5@20250929) | 15 | 6 | 9 | 0 | 0 | 87.0 | 26 | 100 | 11/15 | 9.35 | 7.00 | 15.98 |
| claude (claude-sonnet-4-6) | 15 | 10 | 5 | 0 | 0 | 83.7 | 12 | 99 | 10/15 | 8.50 | 6.35 | 12.88 |

**Score:** 0–100 by closeness to expected: 25 pts for correct contract count; 75 pts from per-field similarity (description, quantity, total, date, address). Partial credit for near matches. **Perfect:** score ≥ 95.

---

## Errors (model mistakes only)

### Incorrect runs (expected vs actual mismatches)

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_complex.json` (`claude_opus-4-5_run_1_new`):
  - Contract #3 items: expected 1, got 2
  - Contract #3 item #1 quantity: expected 3000.0, got 1500.0
  - Contract #3 item #1 total: expected 9000.0, got 4500.0

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_medium.json` (`claude_opus-4-5_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_1_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v1.json` (`claude_opus-4-5_run_1_new`):
  - Contract #1 item #1 total: expected 98400.0, got 100440.0

- **claude (claude-opus-4-5@20251101)** — `real_world_msgs_test_v3.json` (`claude_opus-4-5_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_medium.json` (`claude_opus-4-5_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-12-06'
  - Contract #2: missing in actual

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-5_run_1_new`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **claude (claude-opus-4-5@20251101)** — `single_product_multiple_shipments.json` (`claude_opus-4-5_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #2: missing in actual

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_opus-4-6_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 3
  - Contract #2: missing in actual

- **claude (claude-opus-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_1_new`):
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2 total: expected 240.0, got 4800.0

- **claude (claude-opus-4-6)** — `real_world_msgs_test_v3.json` (`claude_opus-4-6_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #2: missing in actual

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_complex.json` (`claude_opus-4-6_run_1_new`):
  - Contract count: expected 3, got 1
  - Contract #1 item #1 quantity: expected 14.0, got 32.0
  - Contract #1 item #1 total: expected 318.5, got 728.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2026-12-10'
  - Contract #2: missing in actual
  - Contract #3: missing in actual

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_medium.json` (`claude_opus-4-6_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #2: missing in actual

- **claude (claude-opus-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_opus-4-6_run_1_new`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **claude (claude-opus-4-6)** — `single_product_multiple_shipments.json` (`claude_opus-4-6_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2025-11-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2025-12-05'
  - Contract #3 do_date: expected one of '2026-12-12', got '2025-12-12'

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #1 item #1 total: expected 300.0, got 285.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2025-11-28'
  - Contract #2 item #1 total: expected 360.0, got 342.0
  - Contract #2 item #2 total: expected 200.0, got 190.0
  - Contract #2 do_date: expected one of '2026-12-05', got '2025-12-05'

- **claude (claude-sonnet-4-5@20250929)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `real_world_msgs_test_v1.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #1 items: expected 1, got 2
  - Contract #1 item #1 quantity: expected 24.0, got 12.0
  - Contract #1 item #1 total: expected 98400.0, got 49200.0

- **claude (claude-sonnet-4-5@20250929)** — `real_world_msgs_test_v3.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #1 items: expected 1, got 2

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_complex.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2024-11-28'
  - Contract #2 do_date: expected one of '2026-12-04', got '2024-12-04'
  - Contract #3 do_date: expected one of '2026-12-10', got '2024-12-10'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_multiple_shipment_medium.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 item #1 quantity: expected 12.0, got 20.0
  - Contract #1 item #1 total: expected 285.0, got 475.0
  - Contract #1 do_date: expected one of '2026-11-28', got '2025-11-28, 2025-12-06'
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2024-11-28'

- **claude (claude-sonnet-4-5@20250929)** — `single_product_single_shipment_simple.json` (`claude_sonnet-4-5_run_1_new`):
  - Contract #1 do_date: expected one of '2026-11-25', got '2024-11-25'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_medium.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2025-11-28'
  - Contract #2 do_date: expected one of '2026-12-05', got '2025-12-05'

- **claude (claude-sonnet-4-6)** — `multiple_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract count: expected 1, got 2
  - Contract #1 items: expected 2, got 1
  - Contract #1 item #1 total: expected 250.0, got 2500.0
  - Contract #1 item #2: missing in actual

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipment_simple.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract count: expected 1, got 2
  - Contract #1 item #1 quantity: expected 15.0, got 8.0
  - Contract #1 item #1 total: expected 375.0, got 200.0

- **claude (claude-sonnet-4-6)** — `single_product_multiple_shipments.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract count: expected 2, got 1
  - Contract #1 items: expected 1, got 2
  - Contract #2: missing in actual

- **claude (claude-sonnet-4-6)** — `single_product_single_shipment_complex.json` (`claude_sonnet-4-6_run_1_new`):
  - Contract #1 do_date: expected one of '2026-11-28', got '2024-11-28'

