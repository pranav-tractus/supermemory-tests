# LLM comparison — Gemini models, one product one shipment

Source: `llm_comparison_one_product_one_shipment_gemini.md`  
Chat: `long_single_product_single_shipment.json` (1 shipment: 10 bags KNM Coffee).  
Models: Gemini only (2.5-pro, 2.5-flash, 3-flash-preview).

## Ground truth (expected)

- **1 contract** (one shipment).
- **Contract 1:** Nov 28 — 10 bags KNM Coffee, $23.75/bag (5% off), $237.50 total → 100 Finance Ave.

---

## Summary by model (accuracy & latency)

| Model | Runs | Avg score | Min | Max | Perfect (100) | Avg time (s) | Min | Max |
|-------|------|-----------|-----|-----|---------------|--------------|-----|-----|
| gemini (google/gemini-2.5-pro) | 10 | 100.0 | 100 | 100 | 10/10 | 23.65 | 13.27 | 39.71 |
| gemini (google/gemini-2.5-flash) | 10 | 70.0 | 25 | 100 | 6/10 | 16.63 | 13.22 | 21.38 |
| gemini (google/gemini-3-flash-preview) | 10 | 55.0 | 25 | 100 | 4/10 | 25.02 | 16.39 | 42.66 |

**Score:** 0–100 (25 pts: 1 contract; 75 pts: correct item/qty/total/date/address).  
**Perfect:** run with score ≥ 99.

---

## Per-run correctness (all runs)

| Model | Run (user_id) | Time (s) | Score | 1 contract | C1 correct |
|-------|---------------|----------|-------|------------|------------|
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_1 | 15.03 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_10 | 16.25 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_2 | 17.06 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_3 | 20.74 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_4 | 16.44 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_5 | 21.38 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_6 | 16.21 | 25 | ✓ | ✗ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_7 | 13.22 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_8 | 15.61 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-flash) | gemini_gemini-2_5-flash_run_9 | 14.34 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_1 | 17.08 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_10 | 22.68 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_2 | 23.41 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_3 | 39.71 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_4 | 20.55 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_5 | 13.27 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_6 | 13.94 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_7 | 15.96 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_8 | 32.13 | 100 | ✓ | ✓ |
| gemini (google/gemini-2.5-pro) | gemini_gemini-2_5-pro_run_9 | 37.75 | 100 | ✓ | ✓ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_1 | 20.22 | 25 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_10 | 30.60 | 100 | ✓ | ✓ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_2 | 25.09 | 25 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_3 | 42.66 | 25 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_4 | 16.39 | 100 | ✓ | ✓ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_5 | 18.34 | 25 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_6 | 24.64 | 100 | ✓ | ✓ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_7 | 24.47 | 25 | ✓ | ✗ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_8 | 28.49 | 100 | ✓ | ✓ |
| gemini (google/gemini-3-flash-preview) | gemini_gemini-3-flash-preview_run_9 | 19.26 | 25 | ✓ | ✗ |
