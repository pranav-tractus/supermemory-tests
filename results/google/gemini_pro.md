# Memory test results

Each section: chat file, mode, USER_ID, and contract summary.


## long_multi_product_single_shipment.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `010000`
- **Time taken**: 30.90s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 10.0 BAG
      Unit price: 25.0 USD/BAG
      Total: 250.0
      Ship term: FOB Singapore
      Packing: bag
      Loading: —
  Item 2: tea
      Quantity: 15.0 BOX
      Unit price: 12.0 USD/BOX
      Total: 180.0
      Ship term: FOB Singapore
      Packing: box
      Loading: —
  Item 3: paper
      Quantity: 40.0 REAM
      Unit price: 4.0 USD/REAM
      Total: 160.0
      Ship term: FOB Singapore
      Packing: ream
      Loading: —
  Item 4: sanitizer
      Quantity: 24.0 BOTTLE
      Unit price: 8.0 USD/BOTTLE
      Total: 192.0
      Ship term: FOB Singapore
      Packing: 500ml pump bottle
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-12-102
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: Gate B, morning slot.
    Billing address: Test Customer
    Shipping method: by truck
    Shipping address: 100 Finance Ave
```


## long_multi_product_single_shipment.json — gemini (google/gemini-2.5-pro) + memory (supermemory, batched)

- **USER_ID**: `010100`
- **Time taken**: 37.16s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 10.0 BAGS
      Unit price: 25.0 USD/BAG
      Total: 250.0
      Ship term: FOB Singapore
      Packing: bags
      Loading: —
  Item 2: tea
      Quantity: 15.0 BOXES
      Unit price: 12.0 USD/BOX
      Total: 180.0
      Ship term: FOB Singapore
      Packing: boxes
      Loading: —
  Item 3: paper
      Quantity: 40.0 REAMS
      Unit price: 4.0 USD/REAM
      Total: 160.0
      Ship term: FOB Singapore
      Packing: reams
      Loading: —
  Item 4: sanitizer
      Quantity: 24.0 BOTTLE
      Unit price: 8.0 USD/BOTTLE
      Total: 192.0
      Ship term: FOB Singapore
      Packing: bottle
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: 2026-02-16
    PO ref no: PO-2024-12-102
    Vendor: flamingos
    Payment date: —
    Delivery terms: Gate B, morning slot. contact: +65 9123 4567
    Billing address: Test Customer
    Shipping method: by truck
    Shipping address: 100 Finance Ave
```


## long_multi_product_single_shipment.json — gemini (google/gemini-2.5-pro) + memory (mem0, batched)

- **USER_ID**: `010200`
- **Time taken**: 33.00s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 10.0 BAG
      Unit price: 25.0 USD/BAG
      Total: 250.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 2: tea
      Quantity: 15.0 BOX
      Unit price: 12.0 USD/BOX
      Total: 180.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 3: paper
      Quantity: 40.0 REAM
      Unit price: 4.0 USD/REAM
      Total: 160.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 4: sanitizer
      Quantity: 24.0 BOTTLE
      Unit price: 8.0 USD/BOTTLE
      Total: 192.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-12-102
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: Gate B, morning slot.
    Billing address: Test Customer,
    Shipping method: by truck
    Shipping address: 100 Finance Ave
```


## long_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `020000`
- **Time taken**: 17.40s

### Contract summary

```
--- Contract #1 ---
  Item 1: Coffee
      Quantity: 12.0 BAGS
      Unit price: 25.0 USD/BAG
      Total: 300.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: Tea
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
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Paper
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
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Balloons
      Quantity: 4000.0 —
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
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer, Changi Hospital Wars 24 Singapore 700339
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) + memory (supermemory, batched)

- **USER_ID**: `020100`
- **Time taken**: 39.49s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 12.0 BAGS
      Unit price: 24.0 USD/BAG
      Total: 288.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: tea
      Quantity: 30.0 BOXES
      Unit price: 11.52 USD/BOX
      Total: 345.6
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: Net 30 from last delivery — Dec 12.
    Delivery terms: We'll send separate delivery reminders 48 hours before each date. Each DO is picked and checked separately.
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: paper
      Quantity: 50.0 REAMS
      Unit price: 3.84 USD/REAM
      Total: 192.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: Net 30 from last delivery — Dec 12.
    Delivery terms: We'll send separate delivery reminders 48 hours before each date. Each DO is picked and checked separately.
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: balloons
      Quantity: 4000.0 UNITS
      Unit price: 2.88 USD/UNIT
      Total: 11520.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: Net 30 from last delivery — Dec 12.
    Delivery terms: We'll send separate delivery reminders 48 hours before each date. Each DO is picked and checked separately.
    Billing address: Test Customer, Changi Hospital Wars 24 Singapore 700339
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) + memory (mem0, batched)

- **USER_ID**: `020200`
- **Time taken**: 51.71s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 12.0 BAGS
      Unit price: 25.0 USD/BAG
      Total: 288.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: tea
      Quantity: 30.0 BOXES
      Unit price: 12.0 USD/BOX
      Total: 345.6
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: —
    Delivery terms: The third shipment of balloons is provisional and must be confirmed or cancelled by December 5th. A minimum of 5 business days' notice is required for any changes to the delivery schedule. A single invoice for all confirmed shipments will be issued after the final delivery.
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: paper
      Quantity: 50.0 REAMS
      Unit price: 4.0 USD/REAM
      Total: 192.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: —
    Delivery terms: The third shipment of balloons is provisional and must be confirmed or cancelled by December 5th. A minimum of 5 business days' notice is required for any changes to the delivery schedule. A single invoice for all confirmed shipments will be issued after the final delivery.
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: balloons
      Quantity: 4000.0 PIECES
      Unit price: 3.0 USD/PIECE
      Total: 11520.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: —
    Delivery terms: The third shipment of balloons is provisional and must be confirmed or cancelled by December 5th. A minimum of 5 business days' notice is required for any changes to the delivery schedule. A single invoice for all confirmed shipments will be issued after the final delivery.
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_single_product_same.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `030000`
- **Time taken**: 10.34s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 BAGS
      Unit price: 23.5 USD/BAG
      Total: 117.5
      Ship term: —
      Packing: 1kg bags, one carton of 5
      Loading: —
  Key details:
    DO date: 2024-12-03
    PO date: —
    PO ref no: PO-2024-12-202
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: —
    Billing address: Test Customer, Changi Hospital Wars 24 Singapore 700339
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_single_product_same.json — gemini (google/gemini-2.5-pro) + memory (supermemory, batched)

- **USER_ID**: `030100`
- **Time taken**: 26.65s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 BAGS
      Unit price: 23.5 USD/BAG
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
    Delivery terms: Gate A, +65 8765 4321 Stores.
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_single_product_same.json — gemini (google/gemini-2.5-pro) + memory (mem0, batched)

- **USER_ID**: `030200`
- **Time taken**: 17.75s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 BAGS
      Unit price: 23.5 USD/BAG
      Total: 117.5
      Ship term: —
      Packing: one carton of 5
      Loading: —
  Key details:
    DO date: 2024-12-03
    PO date: —
    PO ref no: PO-2024-12-202
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: Gate A, +65 8765 4321 Stores. Electronic delivery note.
    Billing address: Test Customer, accounts@hospital.sg
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_single_product_single_shipment.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `040000`
- **Time taken**: 20.54s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 10.0 BAGS
      Unit price: 23.75 USD/BAG
      Total: 237.5
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-501
    Vendor: flamingos
    Payment date: —
    Delivery terms: Receiving contact is +65 9123 4567. Gate B.
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: 100 Finance Ave
```


## long_single_product_single_shipment.json — gemini (google/gemini-2.5-pro) + memory (supermemory, batched)

- **USER_ID**: `040100`
- **Time taken**: 34.35s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 10.0 BAGS
      Unit price: 23.75 USD/BAG
      Total: 237.5
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-501
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: Contact +65 9123 4567 at Gate B. Driver will call one hour before arrival.
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave
```


## long_single_product_single_shipment.json — gemini (google/gemini-2.5-pro) + memory (mem0, batched)

- **USER_ID**: `040200`
- **Time taken**: 19.62s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 10.0 BAGS
      Unit price: 23.75 USD/BAG
      Total: 237.5
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-501, CC-101
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: Receiving contact is +65 9123 4567. Gate B. The driver will call an hour before arrival. 48 hours notice is required for rescheduling.
    Billing address: Test Customer, 100 Finance Ave
    Shipping method: —
    Shipping address: Test Customer, 100 Finance Ave
```


## short_multi_product_single_shipment.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `050000`
- **Time taken**: 16.50s

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
      Packing: 50 sachets per box
      Loading: —
  Item 3: copy paper
      Quantity: 40.0 reams
      Unit price: 4.0 USD/ream
      Total: 160.0
      Ship term: FOB Singapore
      Packing: A4 80gsm
      Loading: —
  Item 4: hand sanitizer 500ml
      Quantity: 24.0 bottles
      Unit price: 8.0 USD/bottle
      Total: 192.0
      Ship term: FOB Singapore
      Packing: 500ml pump
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-12-002
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: Single delivery for all four products.
    Billing address: Test Customer, 100 Finance Ave Singapore 018989
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```


## short_multi_product_single_shipment.json — gemini (google/gemini-2.5-pro) + memory (supermemory, batched)

- **USER_ID**: `050100`
- **Time taken**: 35.38s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 8.0 BAGS
      Unit price: 25.0 USD/BAG
      Total: 200.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 20.0 BOXES
      Unit price: 12.0 USD/BOX
      Total: 240.0
      Ship term: FOB Singapore
      Packing: 50 sachets per box
      Loading: —
  Item 3: copy paper
      Quantity: 40.0 REAMS
      Unit price: 4.0 USD/REAM
      Total: 160.0
      Ship term: FOB Singapore
      Packing: A4 80gsm
      Loading: —
  Item 4: hand sanitizer
      Quantity: 24.0 BOTTLES
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
    Payment date: Net 30 from delivery
    Delivery terms: Morning slot 9-12. We'll confirm 48 hours before.
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```


## short_multi_product_single_shipment.json — gemini (google/gemini-2.5-pro) + memory (mem0, batched)

- **USER_ID**: `050200`
- **Time taken**: 30.45s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 8.0 BAG
      Unit price: 25.0 USD/BAG
      Total: 194.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 2: Assam tea
      Quantity: 20.0 BOX
      Unit price: 12.0 USD/BOX
      Total: 232.8
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 3: copy paper
      Quantity: 40.0 REAM
      Unit price: 4.0 USD/REAM
      Total: 155.2
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 4: hand sanitizer
      Quantity: 24.0 BOTTLE
      Unit price: 8.0 USD/BOTTLE
      Total: 186.24
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-12-002
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: Morning slot 9-12. We'll confirm 48 hours before.
    Billing address: Test Customer, 100 Finance Ave Singapore 018989
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `060000`
- **Time taken**: 42.79s

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
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer,
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
    DO date: 2024-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 BALLOONS
      Unit price: 2.94 USD/BALLOONS
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
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) + memory (supermemory, batched)

- **USER_ID**: `060100`
- **Time taken**: 25.50s

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
    Payment date: Net 30 from last delivery -- Dec 12
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
    Payment date: Net 30 from last delivery -- Dec 12
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
      Packing: 1000-per-box
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from last delivery -- Dec 12
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — gemini (google/gemini-2.5-pro) + memory (mem0, batched)

- **USER_ID**: `060200`
- **Time taken**: 28.70s

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
    Payment date: Net 30
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
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Red Balloons
      Quantity: 3000.0 —
      Unit price: 2.94 USD
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


## short_single_product_same.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `070000`
- **Time taken**: 13.55s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 BAGS
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
    Payment date: Net 30
    Delivery terms: Receiving dock, Gate A
    Billing address: Test Customer,Changi Hospital Wars 24 Singapore 700339
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_single_product_same.json — gemini (google/gemini-2.5-pro) + memory (supermemory, batched)

- **USER_ID**: `070100`
- **Time taken**: 25.01s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 BAGS
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
    Payment date: Net 30
    Delivery terms: Receiving dock, Gate A. Morning slot as usual.
    Billing address: Test Customer,Changi Hospital Wars 24 Singapore 700339
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_single_product_same.json — gemini (google/gemini-2.5-pro) + memory (mem0, batched)

- **USER_ID**: `070200`
- **Time taken**: 13.55s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 BAGS
      Unit price: 25.0 USD
      Total: 125.0
      Ship term: —
      Packing: 1kg bags, carton of 10
      Loading: —
  Key details:
    DO date: 2024-11-30
    PO date: —
    PO ref no: PO-2024-11-401
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: Receiving dock, Gate A
    Billing address: Test Customer, Changi Hospital Wars 24 Singapore 700339
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_single_product_single_shipment.json — gemini (google/gemini-2.5-pro) (no memory)

- **USER_ID**: `080000`
- **Time taken**: 14.27s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 6.0 BAGS
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
    Payment date: Net 30 from delivery
    Delivery terms: Main loading bay, Gate B. Security will have the pass.
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```


## short_single_product_single_shipment.json — gemini (google/gemini-2.5-pro) + memory (supermemory, batched)

- **USER_ID**: `080100`
- **Time taken**: 21.35s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 6.0 BAGS
      Unit price: 25.0 USD/BAG
      Total: 150.0
      Ship term: —
      Packing: 1kg bags
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-101
    Vendor: flamingos
    Payment date: Net 30 from delivery date
    Delivery terms: Main loading bay, Gate B. Security will have the pass.
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```


## short_single_product_single_shipment.json — gemini (google/gemini-2.5-pro) + memory (mem0, batched)

- **USER_ID**: `080200`
- **Time taken**: 14.86s

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
    Payment date: Net 30 from delivery
    Delivery terms: Delivery is scheduled for Nov 28, morning slot. Main loading bay, Gate B.
    Billing address: Test Customer, 100 Finance Ave Singapore 018989
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```

