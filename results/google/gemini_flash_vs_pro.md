# Gemini Flash vs Pro — Memory Test Comparison

Comparison of memory test results for **google/gemini-2.5-flash** and **google/gemini-2.5-pro** across the same chat files and modes.

---

## Time comparison (seconds)

| Test scenario | Mode | Flash | Pro | Δ (Pro − Flash) |
|---------------|------|------:|----:|----------------:|
| long_multi_product_single_shipment | no memory | 15.84 | 30.90 | +15.06 |
| long_multi_product_single_shipment | supermemory, batched | 20.31 | 37.16 | +16.85 |
| long_multi_product_single_shipment | mem0, batched | 18.89 | 33.00 | +14.11 |
| long_multi_shipment_multi_product | no memory | 22.13 | 17.40 | −4.73 |
| long_multi_shipment_multi_product | supermemory, batched | 22.00 | 39.49 | +17.49 |
| long_multi_shipment_multi_product | mem0, batched | 19.31 | 51.71 | +32.40 |
| long_single_product_same | no memory | 17.37 | 10.34 | −7.03 |
| long_single_product_same | supermemory, batched | 17.89 | 26.65 | +8.76 |
| long_single_product_same | mem0, batched | 15.96 | 17.75 | +1.79 |
| long_single_product_single_shipment | no memory | 15.44 | 20.54 | +5.10 |
| long_single_product_single_shipment | supermemory, batched | 11.43 | 34.35 | +22.92 |
| long_single_product_single_shipment | mem0, batched | 15.06 | 19.62 | +4.56 |
| short_multi_product_single_shipment | no memory | 16.20 | 16.50 | +0.30 |
| short_multi_product_single_shipment | supermemory, batched | 14.90 | 35.38 | +20.48 |
| short_multi_product_single_shipment | mem0, batched | 17.04 | 30.45 | +13.41 |
| short_multi_shipment_multi_product | no memory | 21.41 | 42.79 | +21.38 |
| short_multi_shipment_multi_product | supermemory, batched | 27.68 | 25.50 | −2.18 |
| short_multi_shipment_multi_product | mem0, batched | 45.76  | 28.70 | −17.06 |
| short_single_product_same | no memory | 9.82 | 13.55 | +3.73 |
| short_single_product_same | supermemory, batched | 15.14 | 25.01 | +9.87 |
| short_single_product_same | mem0, batched | 12.46 | 13.55 | +1.09 |
| short_single_product_single_shipment | no memory | 8.87 | 14.27 | +5.40 |
| short_single_product_single_shipment | supermemory, batched | 9.89 | 21.35 | +11.46 |
| short_single_product_single_shipment | mem0, batched | 14.63 | 14.86 | +0.23 |

---

## Summary statistics

| Metric | Flash | Pro |
|--------|------:|----:|
| **Total time (all 24 tests)** | 309.08s | 622.55s |
| **Mean time per test** | 15.38s | 25.94s |
| **Min** | 8.87s | 10.34s |
| **Max** | 45.76 | 51.71s |
| **Median (approx)** | ~14s | ~26s |


---

## Observations

### Speed
- **Flash** is faster on most runs: Pro is slower in 20 of 24 scenarios, often by ~10–20s when using memory (supermemory/mem0).
- **Pro** is faster in 4 cases: `long_multi_shipment_multi_product` (no memory), `long_single_product_same` (no memory), `short_multi_shipment_multi_product` (supermemory), and `short_multi_shipment_multi_product` (mem0).

### Output quality (from sampled contract summaries)
- **Pro** tends to fill more key-detail fields: e.g. Packing (bag/box/ream/bottle), Delivery terms (“Gate B, morning slot”), Billing address (“Test Customer”), Payment date (“Net 30 from delivery”), and sometimes PO date.
- **Flash** often leaves more fields as “—” but can still capture specifics (e.g. “50 sachets per box”, “500ml pump bottle”) when memory is used (e.g. mem0).
- **Pro** (no memory) corrected DO date to 2024-12-05 in one run; Flash (no memory) used 2026-12-05 and a different PO ref (SO-2024-1204 vs PO-2024-12-102). So Pro may be slightly better at date/ref consistency in some no-memory runs.

### When to prefer which
- **Flash**: Lower latency and cost; good when speed and throughput matter and some missing optional fields are acceptable.
- **Pro**: Better for richer, more consistent contract fields and when the outlier slow run.

---

## Source files

- Flash results: `gemini_flash.md`
- Pro results: `gemini_pro.md`
