# Memory test results

Each section: chat file, mode, USER_ID, and contract summary.


## long_multi_product_single_shipment.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `010000`
- **Time taken**: 15.84s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 10.0 bags
      Unit price: 25.0 USD/bag
      Total: 250.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 2: tea
      Quantity: 15.0 boxes
      Unit price: 12.0 USD/box
      Total: 180.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 3: paper
      Quantity: 40.0 reams
      Unit price: 4.0 USD/ream
      Total: 160.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 4: sanitizer
      Quantity: 24.0 bottles
      Unit price: 8.0 USD/bottle
      Total: 192.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: SO-2024-1204
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: truck
    Shipping address: 100 Finance Ave.
```


## long_multi_product_single_shipment.json — gemini (google/gemini-2.5-flash) + memory (supermemory, batched)

- **USER_ID**: `010100`
- **Time taken**: 20.31s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 10.0 bags
      Unit price: 25.0 USD/bag
      Total: 250.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 2: tea
      Quantity: 15.0 boxes
      Unit price: 12.0 USD/box
      Total: 180.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 3: paper
      Quantity: 40.0 reams
      Unit price: 4.0 USD/ream
      Total: 160.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 4: sanitizer
      Quantity: 24.0 bottles
      Unit price: 8.0 USD/bottle
      Total: 192.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-12-102
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: truck
    Shipping address: —
```


## long_multi_product_single_shipment.json — gemini (google/gemini-2.5-flash) + memory (mem0, batched)

- **USER_ID**: `010200`
- **Time taken**: 18.89s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 10.0 BAGS
      Unit price: 25.0 USD/BAG
      Total: 250.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 2: tea
      Quantity: 15.0 BOXES
      Unit price: 12.0 USD/BOX
      Total: 180.0
      Ship term: FOB Singapore
      Packing: 50 sachets per box
      Loading: —
  Item 3: paper
      Quantity: 40.0 REAMS
      Unit price: 4.0 USD/REAM
      Total: 160.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 4: sanitizer
      Quantity: 24.0 BOTTLES
      Unit price: 8.0 USD/BOTTLE
      Total: 192.0
      Ship term: FOB Singapore
      Packing: 500ml pump bottle
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-12-102
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: truck
    Shipping address: 100 Finance Ave.
```


## long_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `020000`
- **Time taken**: 22.13s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 12.0 BAG
      Unit price: 25.0 USD/BAG
      Total: 300.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: tea
      Quantity: 30.0 BOX
      Unit price: 12.0 USD/BOX
      Total: 360.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: paper
      Quantity: 50.0 REAM
      Unit price: 4.0 USD/REAM
      Total: 200.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: balloons
      Quantity: 4000.0 1000
      Unit price: 3000.0 USD/1000
      Total: 12000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) + memory (supermemory, batched)

- **USER_ID**: `020100`
- **Time taken**: 22.00s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 12.0 bags
      Unit price: 25.0 USD/bag
      Total: 300.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: tea
      Quantity: 30.0 boxes
      Unit price: 12.0 USD/box
      Total: 360.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: 2024-11-30
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: paper
      Quantity: 50.0 reams
      Unit price: 4.0 USD/ream
      Total: 200.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: 2024-11-30
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: balloons
      Quantity: 4000.0 balloons
      Unit price: 3000.0 USD/1000
      Total: 12000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: 2024-11-30
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) + memory (mem0, batched)

- **USER_ID**: `020200`
- **Time taken**: 19.31s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 12.0 BAGS
      Unit price: 25.0 USD/BAG
      Total: 300.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: tea
      Quantity: 30.0 BOXES
      Unit price: 12.0 USD/BOX
      Total: 360.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: Net 30 from last delivery — Dec 12
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: paper
      Quantity: 50.0 REAMS
      Unit price: 4.0 USD/REAM
      Total: 200.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: Net 30 from last delivery — Dec 12
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: balloons
      Quantity: 4000.0 PCS
      Unit price: 3.0 USD/PCS
      Total: 12000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: Net 30 from last delivery — Dec 12
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_single_product_same.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `030000`
- **Time taken**: 17.37s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 bags
      Unit price: 23.5 USD/Bag
      Total: 117.5
      Ship term: —
      Packing: 1kg bags, one carton of 5
      Loading: —
  Key details:
    DO date: 2024-12-03
    PO date: —
    PO ref no: PO-2024-12-202
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: —
```


## long_single_product_same.json — gemini (google/gemini-2.5-flash) + memory (supermemory, batched)

- **USER_ID**: `030100`
- **Time taken**: 17.89s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 bags
      Unit price: 23.5 USD/BAG
      Total: 117.5
      Ship term: —
      Packing: 1kg bags, one carton of 5
      Loading: —
  Key details:
    DO date: 2026-12-03
    PO date: —
    PO ref no: PO-2024-12-202
    Vendor: flamingos
    Payment date: —
    Delivery terms: Gate A, +65 8765 4321 Stores
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_single_product_same.json — gemini (google/gemini-2.5-flash) + memory (mem0, batched)

- **USER_ID**: `030200`
- **Time taken**: 15.96s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 bags
      Unit price: 23.5 USD/BAG
      Total: 117.5
      Ship term: DDP Changi
      Packing: reinforced 1kg bags, one carton of 5
      Loading: —
  Key details:
    DO date: 2024-12-03
    PO date: —
    PO ref no: PO-2024-12-202
    Vendor: flamingos
    Payment date: —
    Delivery terms: Changi, Gate A, +65 8765 4321 Stores
    Billing address: —
    Shipping method: —
    Shipping address: —
```


## long_single_product_single_shipment.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `040000`
- **Time taken**: 15.44s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 10.0 bags
      Unit price: 23.75 $/bag
      Total: 237.5
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-501
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: —
```


## long_single_product_single_shipment.json — gemini (google/gemini-2.5-flash) + memory (supermemory, batched)

- **USER_ID**: `040100`
- **Time taken**: 11.43s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 10.0 bags
      Unit price: 23.75 USD/bag
      Total: 237.5
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-501
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave.
```


## long_single_product_single_shipment.json — gemini (google/gemini-2.5-flash) + memory (mem0, batched)

- **USER_ID**: `040200`
- **Time taken**: 15.06s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 10.0 bags
      Unit price: 23.75 $/bag
      Total: 237.5
      Ship term: FOB Singapore
      Packing: careful packaging
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-501
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: —
```


## short_multi_product_single_shipment.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `050000`
- **Time taken**: 16.20s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 8.0 bags
      Unit price: 25.0 USD/bag
      Total: 200.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 20.0 boxes
      Unit price: 12.0 USD/box
      Total: 240.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 3: copy paper
      Quantity: 40.0 reams
      Unit price: 4.0 USD/ream
      Total: 160.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 4: hand sanitizer
      Quantity: 24.0 bottles
      Unit price: 8.0 USD/bottle
      Total: 192.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-12-002
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```


## short_multi_product_single_shipment.json — gemini (google/gemini-2.5-flash) + memory (supermemory, batched)

- **USER_ID**: `050100`
- **Time taken**: 14.90s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 8.0 bags
      Unit price: 25.0 USD/bag
      Total: 200.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 20.0 boxes
      Unit price: 12.0 USD/box
      Total: 240.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 3: copy paper
      Quantity: 40.0 reams
      Unit price: 4.0 USD/ream
      Total: 160.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 4: hand sanitizer
      Quantity: 24.0 bottles
      Unit price: 8.0 USD/bottle
      Total: 192.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: 2024-12-05
    PO ref no: PO-2024-12-002
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: Single delivery
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989.
```


## short_multi_product_single_shipment.json — gemini (google/gemini-2.5-flash) + memory (mem0, batched)

- **USER_ID**: `050200`
- **Time taken**: 17.04s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 8.0 BAG
      Unit price: 25.0 USD/BAG
      Total: 200.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 20.0 BOX
      Unit price: 12.0 USD/BOX
      Total: 240.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 3: copy paper
      Quantity: 40.0 REAM
      Unit price: 4.0 USD/REAM
      Total: 160.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 4: hand sanitizer
      Quantity: 24.0 BOTTLE
      Unit price: 8.0 USD/BOTTLE
      Total: 192.0
      Ship term: FOB Singapore
      Packing: 500ml pump
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-12-002
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: —
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `060000`
- **Time taken**: 21.41s

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
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: 2025-01-11
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
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: 2025-01-11
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
      Packing: 1000 per box
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: 2025-01-11
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) + memory (supermemory, batched)

- **USER_ID**: `060100`
- **Time taken**: 27.68s

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
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: —

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
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: —

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 balloons
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
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: —
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-flash) + memory (mem0, batched)

- **USER_ID**: `060200`
- **Time taken**: 45.76s

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
      Quantity: 3000.0 BALLOONS
      Unit price: 3.0 USD/BALLOONS
      Total: 9000.0
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


## short_single_product_same.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `070000`
- **Time taken**: 9.82s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 bags
      Unit price: 25.0 USD/BAG
      Total: 125.0
      Ship term: —
      Packing: 1kg bags, carton of 10
      Loading: —
  Key details:
    DO date: 2024-11-30
    PO date: —
    PO ref no: PO-2024-11-401
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_single_product_same.json — gemini (google/gemini-2.5-flash) + memory (supermemory, batched)

- **USER_ID**: `070100`
- **Time taken**: 15.14s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 bags
      Unit price: 25.0 USD/BAG
      Total: 125.0
      Ship term: —
      Packing: 1kg bags, carton of 10
      Loading: —
  Key details:
    DO date: 2026-11-30
    PO date: —
    PO ref no: PO-2024-11-401
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_single_product_same.json — gemini (google/gemini-2.5-flash) + memory (mem0, batched)

- **USER_ID**: `070200`
- **Time taken**: 12.46s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 bags
      Unit price: 25.0 USD/BAG
      Total: 125.0
      Ship term: —
      Packing: 1kg bags, carton of 10
      Loading: —
  Key details:
    DO date: 2026-11-30
    PO date: —
    PO ref no: PO-2024-11-401
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: —
```


## short_single_product_single_shipment.json — gemini (google/gemini-2.5-flash) (no memory)

- **USER_ID**: `080000`
- **Time taken**: 8.87s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 6.0 BAG
      Unit price: 25.0 USD/BAG
      Total: 150.0
      Ship term: —
      Packing: standard 1kg bags, carton of 10
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-101
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: —
```


## short_single_product_single_shipment.json — gemini (google/gemini-2.5-flash) + memory (supermemory, batched)

- **USER_ID**: `080100`
- **Time taken**: 9.89s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 6.0 BAG
      Unit price: 25.0 USD/BAG
      Total: 150.0
      Ship term: —
      Packing: standard 1kg bags, carton of 10
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-101
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```


## short_single_product_single_shipment.json — gemini (google/gemini-2.5-flash) + memory (mem0, batched)

- **USER_ID**: `080200`
- **Time taken**: 14.63s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 6.0 bags
      Unit price: 25.0 $/bag
      Total: 150.0
      Ship term: —
      Packing: standard 1kg bags, carton of 10
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-101
    Vendor: flamingos
    Payment date: —
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: —
```

