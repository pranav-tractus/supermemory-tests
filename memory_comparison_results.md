# Memory Test Results — 10 runs per model

**Chat file:** `chats/short_multi_shipment_multi_product.json`

**Model combinations:**
- **OpenAI:** default, 4.1, 5.2, 5-mini
- **Gemini:** gemini-2.5-pro, gemini-2.5-flash, gemini-2.0-flash

---


## short_multi_shipment_multi_product.json — openai (gpt-4o-2024-08-06) (no memory)

- **USER_ID**: `openai_default_run_1`
- **Time taken**: 5.14s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 UNITS
      Unit price: 3.0 USD
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339

--- Contract #2 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave
```


## short_multi_shipment_multi_product.json — openai (gpt-4o-2024-08-06) (no memory)

- **USER_ID**: `openai_default_run_2`
- **Time taken**: 4.89s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2025-11-28
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2025-12-05
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 —
      Unit price: 9.0 k
      Total: 27000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2025-12-12
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4o-2024-08-06) (no memory)

- **USER_ID**: `openai_default_run_3`
- **Time taken**: 4.21s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2025-11-28
    PO date: —
    PO ref no: SO-2024-1300
    Vendor: flamingos
    Payment date: NET 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam Tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy Paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2025-12-05
    PO date: —
    PO ref no: SO-2024-1300
    Vendor: flamingos
    Payment date: NET 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 3.0 USD/BALLOON
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2025-12-12
    PO date: —
    PO ref no: SO-2024-1300
    Vendor: flamingos
    Payment date: NET 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4o-2024-08-06) (no memory)

- **USER_ID**: `openai_default_run_4`
- **Time taken**: 4.40s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2025-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Red Balloons
      Quantity: 3000.0 —
      Unit price: 3.0 USD
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2025-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4o-2024-08-06) (no memory)

- **USER_ID**: `openai_default_run_5`
- **Time taken**: 2.96s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 —
      Unit price: 9.0 USD/BALLOON
      Total: 27000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-31
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: —
```


## short_multi_shipment_multi_product.json — openai (gpt-4o-2024-08-06) (no memory)

- **USER_ID**: `openai_default_run_6`
- **Time taken**: 2.11s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: —
      Loading: —
  Item 3: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2025-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave
```


## short_multi_shipment_multi_product.json — openai (gpt-4o-2024-08-06) (no memory)

- **USER_ID**: `openai_default_run_7`
- **Time taken**: 7.43s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam Tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: —
      Loading: —
  Item 3: Copy Paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PIECES
      Unit price: 9.0 USD
      Total: 27000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave, Singapore
    Shipping method: —
    Shipping address: 100 Finance Ave, Singapore

--- Contract #2 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam Tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy Paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PIECES
      Unit price: 9.0 USD
      Total: 27000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: SO-2024-1300
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave, Singapore
    Shipping method: —
    Shipping address: 100 Finance Ave, Singapore

--- Contract #3 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam Tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy Paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PIECES
      Unit price: 9.0 USD
      Total: 27000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: SO-2024-1300
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave, Singapore
    Shipping method: —
    Shipping address: 100 Finance Ave, Singapore

--- Contract #4 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam Tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy Paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PIECES
      Unit price: 9.0 USD
      Total: 27000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: SO-2024-1300
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave, Singapore
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4o-2024-08-06) (no memory)

- **USER_ID**: `openai_default_run_8`
- **Time taken**: 6.27s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 UNITS
      Unit price: 3.0 USD
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-11-30
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: NET 30 DAYS
    Delivery terms: —
    Billing address: Test Customer 100 Finance Ave, Singapore
    Shipping method: —
    Shipping address: 100 Finance Ave, Singapore

--- Contract #2 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 UNITS
      Unit price: 3.0 USD
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: NET 30 DAYS
    Delivery terms: —
    Billing address: Test Customer 100 Finance Ave, Singapore
    Shipping method: —
    Shipping address: 100 Finance Ave, Singapore

--- Contract #3 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 UNITS
      Unit price: 3.0 USD
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: NET 30 DAYS
    Delivery terms: —
    Billing address: Test Customer 100 Finance Ave, Singapore
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4o-2024-08-06) (no memory)

- **USER_ID**: `openai_default_run_9`
- **Time taken**: 2.97s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 Bags
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam Tea
      Quantity: 30.0 Boxes
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy Paper
      Quantity: 50.0 Reams
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 Items
      Unit price: 9000.0 USD
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2026-12-31
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave
```


## short_multi_shipment_multi_product.json — openai (gpt-4o-2024-08-06) (no memory)

- **USER_ID**: `openai_default_run_10`
- **Time taken**: 2.33s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: —
      Packing: —
      Loading: —
  Item 3: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 UNITS
      Unit price: 3.0 USD
      Total: 9000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: 2026-10-01
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4.1-2025-04-14) (no memory)

- **USER_ID**: `openai_4_1_run_1`
- **Time taken**: 3.63s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PC
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4.1-2025-04-14) (no memory)

- **USER_ID**: `openai_4_1_run_2`
- **Time taken**: 4.63s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PC
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box (3 boxes of 1000)
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PC
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box (3 boxes of 1000)
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4.1-2025-04-14) (no memory)

- **USER_ID**: `openai_4_1_run_3`
- **Time taken**: 4.74s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAG
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOX
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: copy paper
      Quantity: 50.0 REAM
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOX
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAM
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 EACH
      Unit price: 3.0 USD/EACH
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4.1-2025-04-14) (no memory)

- **USER_ID**: `openai_4_1_run_4`
- **Time taken**: 4.36s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PCS
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PCS
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4.1-2025-04-14) (no memory)

- **USER_ID**: `openai_4_1_run_5`
- **Time taken**: 3.47s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/30 BOXES
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/50 REAMS
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/1000 PCS
      Total: 9000.0
      Ship term: —
      Packing: 1000 per box
      Loading: —
  Key details:
    DO date: —
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: —
```


## short_multi_shipment_multi_product.json — openai (gpt-4.1-2025-04-14) (no memory)

- **USER_ID**: `openai_4_1_run_6`
- **Time taken**: 5.25s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PC
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PC
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4.1-2025-04-14) (no memory)

- **USER_ID**: `openai_4_1_run_7`
- **Time taken**: 10.20s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PCS
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PCS
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4.1-2025-04-14) (no memory)

- **USER_ID**: `openai_4_1_run_8`
- **Time taken**: 4.67s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PCS
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PCS
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4.1-2025-04-14) (no memory)

- **USER_ID**: `openai_4_1_run_9`
- **Time taken**: 4.95s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PC
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-4.1-2025-04-14) (no memory)

- **USER_ID**: `openai_4_1_run_10`
- **Time taken**: 4.47s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD/BAG
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 3: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Item 4: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PC
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD/BOX
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD/REAM
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: 3.0 USD/PC
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5.2-2025-12-11) (no memory)

- **USER_ID**: `openai_5_2_run_1`
- **Time taken**: 5.74s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 1000-per-box packaging (3 boxes of 1000)
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5.2-2025-12-11) (no memory)

- **USER_ID**: `openai_5_2_run_2`
- **Time taken**: 7.34s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339.
```


## short_multi_shipment_multi_product.json — openai (gpt-5.2-2025-12-11) (no memory)

- **USER_ID**: `openai_5_2_run_3`
- **Time taken**: 6.76s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339.
```


## short_multi_shipment_multi_product.json — openai (gpt-5.2-2025-12-11) (no memory)

- **USER_ID**: `openai_5_2_run_4`
- **Time taken**: 10.56s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339.
```


## short_multi_shipment_multi_product.json — openai (gpt-5.2-2025-12-11) (no memory)

- **USER_ID**: `openai_5_2_run_5`
- **Time taken**: 5.69s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339.
```


## short_multi_shipment_multi_product.json — openai (gpt-5.2-2025-12-11) (no memory)

- **USER_ID**: `openai_5_2_run_6`
- **Time taken**: 6.18s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5.2-2025-12-11) (no memory)

- **USER_ID**: `openai_5_2_run_7`
- **Time taken**: 6.50s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 —
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 1000-per-box (3 boxes of 1000)
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5.2-2025-12-11) (no memory)

- **USER_ID**: `openai_5_2_run_8`
- **Time taken**: 6.32s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5.2-2025-12-11) (no memory)

- **USER_ID**: `openai_5_2_run_9`
- **Time taken**: 5.54s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2025-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2025-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 1000-per-box; 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2025-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5.2-2025-12-11) (no memory)

- **USER_ID**: `openai_5_2_run_10`
- **Time taken**: 6.18s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5-mini-2025-08-07) (no memory)

- **USER_ID**: `openai_5-mini_run_1`
- **Time taken**: 30.88s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: — —
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: — —
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: — —
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: — —
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000 (1000-per-box)
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5-mini-2025-08-07) (no memory)

- **USER_ID**: `openai_5-mini_run_2`
- **Time taken**: 35.29s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: — $
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: — $
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: — $
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: — $
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5-mini-2025-08-07) (no memory)

- **USER_ID**: `openai_5-mini_run_3`
- **Time taken**: 32.32s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: — —
      Total: —
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: — —
      Total: —
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: — —
      Total: —
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: — —
      Total: —
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5-mini-2025-08-07) (no memory)

- **USER_ID**: `openai_5-mini_run_4`
- **Time taken**: 48.90s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: — USD
      Total: 250.0
      Ship term: —
      Packing: bags
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: — USD
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: copy paper
      Quantity: 50.0 reams
      Unit price: — USD
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #4 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: — USD
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5-mini-2025-08-07) (no memory)

- **USER_ID**: `openai_5-mini_run_5`
- **Time taken**: 40.35s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: — —
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: — —
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy paper (A4 80gsm)
      Quantity: 50.0 REAMS
      Unit price: — —
      Total: 200.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 PCS
      Unit price: — —
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box (3 boxes)
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5-mini-2025-08-07) (no memory)

- **USER_ID**: `openai_5-mini_run_6`
- **Time taken**: 38.97s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: — $
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: — $
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy paper (A4 80gsm)
      Quantity: 50.0 reams
      Unit price: — $
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: — $
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000 (1000-per-box)
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5-mini-2025-08-07) (no memory)

- **USER_ID**: `openai_5-mini_run_7`
- **Time taken**: 21.84s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper (A4 80gsm)
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 200.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 9000.0 $
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5-mini-2025-08-07) (no memory)

- **USER_ID**: `openai_5-mini_run_8`
- **Time taken**: 29.19s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: — —
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: — —
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: — —
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: — —
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5-mini-2025-08-07) (no memory)

- **USER_ID**: `openai_5-mini_run_9`
- **Time taken**: 29.25s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: — —
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: — —
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: — —
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: — —
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000 (1000-per-box)
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — openai (gpt-5-mini-2025-08-07) (no memory)

- **USER_ID**: `openai_5-mini_run_10`
- **Time taken**: 39.56s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: — —
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: — —
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper (A4 80gsm)
      Quantity: 50.0 REAMS
      Unit price: — —
      Total: 200.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: — —
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box (3 boxes)
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `gemini_gemini-2_5-pro_run_1`
- **Time taken**: 28.42s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 20.42 USD
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 11.76 USD
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 3.92 USD
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 2.94 USD
      Total: 8820.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `gemini_gemini-2_5-pro_run_2`
- **Time taken**: 27.44s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 20.42 USD/BAG
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 11.76 USD/BOX
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 3.92 USD/REAM
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 2.94 USD/BALLOON
      Total: 8820.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `gemini_gemini-2_5-pro_run_3`
- **Time taken**: 28.41s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 20.42 —
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 11.76 —
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 3.92 —
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 2.94 —
      Total: 8820.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `gemini_gemini-2_5-pro_run_4`
- **Time taken**: 27.30s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: — —
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: — —
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: — —
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: — —
      Total: 8820.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `gemini_gemini-2_5-pro_run_5`
- **Time taken**: 27.63s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 20.42 USD
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 11.76 USD
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 3.92 USD
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 2.94 USD
      Total: 8820.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `gemini_gemini-2_5-pro_run_6`
- **Time taken**: 28.76s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: — USD
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: One order, three shipments
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: — USD
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: — USD
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: One order, three shipments
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: — USD
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: One order, three shipments
    Billing address: Test Customer, Changi Hospital Wars 24 Singapore 700339
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `gemini_gemini-2_5-pro_run_7`
- **Time taken**: 28.98s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 20.42 USD
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 11.76 USD
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 3.92 USD
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 2.94 USD
      Total: 8820.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `gemini_gemini-2_5-pro_run_8`
- **Time taken**: 27.22s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 20.83 USD/BAGS
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 12.0 USD/BOXES
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 4.0 USD/REAMS
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 3.0 USD/BALLOONS
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `gemini_gemini-2_5-pro_run_9`
- **Time taken**: 36.47s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 20.42 USD/BAGS
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 11.76 USD/BOXES
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 3.92 USD/REAMS
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 UNITS
      Unit price: 2.94 USD/UNITS
      Total: 8820.0
      Ship term: —
      Packing: 1000 per box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `gemini_gemini-2_5-pro_run_10`
- **Time taken**: 32.61s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 20.42 —
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 11.76 —
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 3.92 —
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 —
      Unit price: 2.94 —
      Total: 8820.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_5-flash_run_1`
- **Time taken**: 17.24s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 20.83 USD/BAG
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 12.0 USD/BOX
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: Copy paper
      Quantity: 50.0 REAMS
      Unit price: 4.0 USD/REAM
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 3.0 USD/BALLOON
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_5-flash_run_2`
- **Time taken**: 27.21s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 20.83 USD/BAG
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 12.0 USD/BOX
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 4.0 USD/REAM
      Total: 200.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 3.0 USD/BALLOON
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_5-flash_run_3`
- **Time taken**: 29.54s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 20.42 USD/bag
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: multiple shipments
    Billing address: —
    Shipping method: —
    Shipping address: —

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 11.76 USD/box
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 3.92 USD/ream
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: multiple shipments
    Billing address: —
    Shipping method: —
    Shipping address: —

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3.0 boxes
      Unit price: 2940.0 USD/box
      Total: 8820.0
      Ship term: —
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: multiple shipments
    Billing address: —
    Shipping method: —
    Shipping address: —
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_5-flash_run_4`
- **Time taken**: 22.42s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 20.416666666666668 USD/bag
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 11.76 USD/box
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 3.92 USD/ream
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 2.94 USD/balloons
      Total: 8820.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_5-flash_run_5`
- **Time taken**: 32.38s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 20.83 USD/BAG
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: —

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 12.0 USD/BOX
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 4.0 USD/REAM
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: —

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 3.0 USD/BALLOON
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: —
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_5-flash_run_6`
- **Time taken**: 23.76s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 BAGS
      Unit price: 20.83 USD/BAG
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: 2027-01-11
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 BOXES
      Unit price: 12.0 USD/BOX
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 REAMS
      Unit price: 4.0 USD/REAM
      Total: 200.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: 2027-01-11
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 3.0 USD/BALLOON
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box
      Loading: 3 boxes
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: 2027-01-11
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_5-flash_run_7`
- **Time taken**: 19.65s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 20.83 USD/BAG
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 12.0 USD/BOX
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 4.0 USD/REAM
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 3.0 USD/BALLOON
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_5-flash_run_8`
- **Time taken**: 17.37s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 USD/bag
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 USD/box
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 200.0 USD/ream
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 3.0 USD/balloon
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_5-flash_run_9`
- **Time taken**: 25.03s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 20.416666666666668 USD/bag
      Total: 245.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: 2027-01-11
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 11.76 USD/box
      Total: 352.8
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 3.92 USD/ream
      Total: 196.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: 2027-01-11
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 2.94 USD/balloon
      Total: 8820.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: 2027-01-11
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_5-flash_run_10`
- **Time taken**: 19.21s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 20.83 USD/bag
      Total: 250.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 12.0 USD/box
      Total: 360.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 4.0 USD/ream
      Total: 200.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 3.0 USD/balloon
      Total: 9000.0
      Ship term: —
      Packing: 3 boxes of 1000
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.0-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_0-flash_run_1`
- **Time taken**: 4.37s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: —

--- Contract #2 ---
  Item 1: tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: paper
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: —

--- Contract #3 ---
  Item 1: balloons
      Quantity: 3000.0 —
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: —
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.0-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_0-flash_run_2`
- **Time taken**: 6.10s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-30
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 432eef62-3867-46b7-abf0-cdb2a09183d6

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-31
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 432eef62-3867-46b7-abf0-cdb2a09183d6

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-31
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 432eef62-3867-46b7-abf0-cdb2a09183d6
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.0-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_0-flash_run_3`
- **Time taken**: 4.64s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 3.0 $
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.0-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_0-flash_run_4`
- **Time taken**: 4.64s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.0-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_0-flash_run_5`
- **Time taken**: 4.60s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.0-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_0-flash_run_6`
- **Time taken**: 4.92s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: —

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: —

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 3.0 $
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: —
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.0-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_0-flash_run_7`
- **Time taken**: 4.99s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.0-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_0-flash_run_8`
- **Time taken**: 4.79s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 3.0 $
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.0-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_0-flash_run_9`
- **Time taken**: 4.53s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 3.0 $
      Total: 9000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: 2024-11-30
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.0-flash) (no memory)

- **USER_ID**: `gemini_gemini-2_0-flash_run_10`
- **Time taken**: 5.12s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 12.0 bags
      Unit price: 250.0 $
      Total: 3000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: 2024-11-301
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Assam tea
      Quantity: 30.0 boxes
      Unit price: 360.0 $
      Total: 10800.0
      Ship term: —
      Packing: 50 sachets/box
      Loading: —
  Item 2: copy paper
      Quantity: 50.0 reams
      Unit price: 200.0 $
      Total: 10000.0
      Ship term: —
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: 2024-11-301
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
      Unit price: 9000.0 $
      Total: 27000000.0
      Ship term: —
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: 2024-11-301
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```

