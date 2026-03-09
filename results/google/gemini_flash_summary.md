# Model x Chat comparison - Summary

Generated from the raw results file. Correctness is compared to expected results (see `expected_results.py`).

---

## Overview

- **Chats used:** 8 — `long_multi_product_single_shipment.json`, `long_multi_shipment_multi_product.json`, `long_single_product_same.json`, `long_single_product_single_shipment.json`, `short_multi_product_single_shipment.json`, `short_multi_shipment_multi_product.json`, `short_single_product_same.json`, `short_single_product_single_shipment.json`
- **Models used:** 1 — `gemini (google/gemini-2.5-flash)`
- **Total runs:** 24
- **Correct (vs expected):** 0 | **Incorrect:** 21 | **N/A (no expected):** 3

---

## By model

| Model | Runs | Chats | Avg time (s) | Min | Max |
|-------|------|-------|--------------|-----|-----|
| gemini (google/gemini-2.5-flash) | 24 | long_multi_product_single_shipment.json, long_multi_shipment_multi_product.json, long_single_product_same.json, long_single_product_single_shipment.json, short_multi_product_single_shipment.json, short_multi_shipment_multi_product.json, short_single_product_same.json, short_single_product_single_shipment.json | 17.73 | 8.87 | 45.76 |

---

## By chat

| Chat | Runs | Models | Avg time (s) | Min | Max |
|------|------|--------|--------------|-----|-----|
| long_multi_product_single_shipment.json | 3 | 1 | 18.35 | 15.84 | 20.31 |
| long_multi_shipment_multi_product.json | 3 | 1 | 21.15 | 19.31 | 22.13 |
| long_single_product_same.json | 3 | 1 | 17.07 | 15.96 | 17.89 |
| long_single_product_single_shipment.json | 3 | 1 | 13.98 | 11.43 | 15.44 |
| short_multi_product_single_shipment.json | 3 | 1 | 16.05 | 14.90 | 17.04 |
| short_multi_shipment_multi_product.json | 3 | 1 | 31.62 | 21.41 | 45.76 |
| short_single_product_same.json | 3 | 1 | 12.47 | 9.82 | 15.14 |
| short_single_product_single_shipment.json | 3 | 1 | 11.13 | 8.87 | 14.63 |

---

## Per-run times and correctness (all runs)

| Chat | Model | USER_ID | Time (s) | Correct |
|------|-------|---------|----------|---------|
| long_multi_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `010000` | 15.84 | N |
| long_multi_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `010100` | 20.31 | N |
| long_multi_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `010200` | 18.89 | N |
| long_multi_shipment_multi_product.json | gemini (google/gemini-2.5-flash) | `020000` | 22.13 | N |
| long_multi_shipment_multi_product.json | gemini (google/gemini-2.5-flash) | `020100` | 22.00 | N |
| long_multi_shipment_multi_product.json | gemini (google/gemini-2.5-flash) | `020200` | 19.31 | N |
| long_single_product_same.json | gemini (google/gemini-2.5-flash) | `030000` | 17.37 | N |
| long_single_product_same.json | gemini (google/gemini-2.5-flash) | `030100` | 17.89 | N |
| long_single_product_same.json | gemini (google/gemini-2.5-flash) | `030200` | 15.96 | N |
| long_single_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `040000` | 15.44 | N |
| long_single_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `040100` | 11.43 | N |
| long_single_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `040200` | 15.06 | N |
| short_multi_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `050000` | 16.20 | N |
| short_multi_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `050100` | 14.90 | N |
| short_multi_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `050200` | 17.04 | N |
| short_multi_shipment_multi_product.json | gemini (google/gemini-2.5-flash) | `060000` | 21.41 | N/A |
| short_multi_shipment_multi_product.json | gemini (google/gemini-2.5-flash) | `060100` | 27.68 | N/A |
| short_multi_shipment_multi_product.json | gemini (google/gemini-2.5-flash) | `060200` | 45.76 | N/A |
| short_single_product_same.json | gemini (google/gemini-2.5-flash) | `070000` | 9.82 | N |
| short_single_product_same.json | gemini (google/gemini-2.5-flash) | `070100` | 15.14 | N |
| short_single_product_same.json | gemini (google/gemini-2.5-flash) | `070200` | 12.46 | N |
| short_single_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `080000` | 8.87 | N |
| short_single_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `080100` | 9.89 | N |
| short_single_product_single_shipment.json | gemini (google/gemini-2.5-flash) | `080200` | 14.63 | N |

---

## Incorrect runs (expected vs actual)

- **long_multi_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`010000`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_multi_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`010100`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_multi_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`010200`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_multi_shipment_multi_product.json** — **gemini (google/gemini-2.5-flash)** (`020000`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_multi_shipment_multi_product.json** — **gemini (google/gemini-2.5-flash)** (`020100`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_multi_shipment_multi_product.json** — **gemini (google/gemini-2.5-flash)** (`020200`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_single_product_same.json** — **gemini (google/gemini-2.5-flash)** (`030000`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_single_product_same.json** — **gemini (google/gemini-2.5-flash)** (`030100`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_single_product_same.json** — **gemini (google/gemini-2.5-flash)** (`030200`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_single_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`040000`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_single_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`040100`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **long_single_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`040200`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **short_multi_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`050000`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **short_multi_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`050100`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **short_multi_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`050200`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **short_single_product_same.json** — **gemini (google/gemini-2.5-flash)** (`070000`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **short_single_product_same.json** — **gemini (google/gemini-2.5-flash)** (`070100`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **short_single_product_same.json** — **gemini (google/gemini-2.5-flash)** (`070200`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **short_single_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`080000`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **short_single_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`080100`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)

- **short_single_product_single_shipment.json** — **gemini (google/gemini-2.5-flash)** (`080200`):
  - No contract JSON in results (run test_memory with results-file that includes JSON block)
