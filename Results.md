# Memory test results

Each section: chat file, mode, and contract summary.

---




## Comparison by chat

### long_multi_product_single_shipment.json

| Mode | Time taken | Result |
|------|------------|--------|
| only llm no memory | 3.10s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: Coffee&#10;      Quantity: 10.0 BAGS&#10;      Unit price: 25.0 USD/BAG&#10;      Total: 250.0&#10;      Ship term: FOB Singapore&#10;      Packing: —&#10;      Loading: —&#10;  Item 2: Tea&#10;      Quantity: 15.0 BOXES&#10;      Unit price: 12.0 USD/BOX&#10;      Total: 180.0&#10;      Ship term: FOB Singapore&#10;      Packing: 50 sachets per box&#10;      Loading: —&#10;  Item 3: Paper&#10;      Quantity: 40.0 REAMS&#10;      Unit price: 4.0 USD/REAM&#10;      Total: 160.0&#10;      Ship term: FOB Singapore&#10;      Packing: —&#10;      Loading: —&#10;  Item 4: Sanitizer&#10;      Quantity: 24.0 BOTTLES&#10;      Unit price: 8.0 USD/BOTTLE&#10;      Total: 192.0&#10;      Ship term: FOB Singapore&#10;      Packing: 500ml pump bottle&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-12-05&#10;    PO date: —&#10;    PO ref no: PO-2024-12-102&#10;    Vendor: flamingos&#10;    Payment date: Net 30 from delivery&#10;    Delivery terms: FOB Singapore&#10;    Billing address: —&#10;    Shipping method: Truck&#10;    Shipping address: 100 Finance Ave</pre></details> |
| use memory with batching | 10.35s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: Coffee&#10;      Quantity: 10.0 BAG&#10;      Unit price: 25.0 USD/BAG&#10;      Total: 250.0&#10;      Ship term: FOB SINGAPORE&#10;      Packing: —&#10;      Loading: —&#10;  Item 2: Tea&#10;      Quantity: 15.0 BOX&#10;      Unit price: 12.0 USD/BOX&#10;      Total: 180.0&#10;      Ship term: FOB SINGAPORE&#10;      Packing: 50 sachets per box&#10;      Loading: —&#10;  Item 3: Sanitizer&#10;      Quantity: 24.0 BOTTLE&#10;      Unit price: 8.0 USD/BOTTLE&#10;      Total: 192.0&#10;      Ship term: FOB SINGAPORE&#10;      Packing: 500ml pump bottle&#10;      Loading: —&#10;  Item 4: Paper&#10;      Quantity: 40.0 REAM&#10;      Unit price: 4.0 USD/REAM&#10;      Total: 160.0&#10;      Ship term: FOB SINGAPORE&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-12-05&#10;    PO date: —&#10;    PO ref no: —&#10;    Vendor: flamingos&#10;    Payment date: Net 30 Days&#10;    Delivery terms: —&#10;    Billing address: —&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave</pre></details> |


### long_multi_shipment_multi_product.json

| Mode | Time taken | Result |
|------|------------|--------|
| only llm no memory | 3.56s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: coffee&#10;      Quantity: 12.0 BAG&#10;      Unit price: 25.0 $&#10;      Total: 300.0&#10;      Ship term: —&#10;      Packing: —&#10;      Loading: —&#10;  Item 2: tea&#10;      Quantity: 30.0 BOX&#10;      Unit price: 12.0 $&#10;      Total: 360.0&#10;      Ship term: —&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2025-11-28&#10;    PO date: —&#10;    PO ref no: —&#10;    Vendor: flamingos&#10;    Payment date: NET 30&#10;    Delivery terms: —&#10;    Billing address: —&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave&#10;&#10;--- Contract #2 ---&#10;  Item 1: paper&#10;      Quantity: 50.0 REAM&#10;      Unit price: 4.0 $&#10;      Total: 200.0&#10;      Ship term: —&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2025-12-05&#10;    PO date: —&#10;    PO ref no: —&#10;    Vendor: flamingos&#10;    Payment date: NET 30&#10;    Delivery terms: —&#10;    Billing address: —&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave&#10;&#10;--- Contract #3 ---&#10;  Item 1: balloons&#10;      Quantity: 4000.0 —&#10;      Unit price: 3.0 $&#10;      Total: 12000.0&#10;      Ship term: —&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2025-12-12&#10;    PO date: —&#10;    PO ref no: —&#10;    Vendor: flamingos&#10;    Payment date: NET 30&#10;    Delivery terms: —&#10;    Billing address: —&#10;    Shipping method: —&#10;    Shipping address: Changi Hospital Wars 24 Singapore 700339</pre></details> |
| use memory with batching | 13.26s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: coffee&#10;      Quantity: 12.0 BAG&#10;      Unit price: 25.0 USD/BAG&#10;      Total: 300.0&#10;      Ship term: —&#10;      Packing: —&#10;      Loading: —&#10;  Item 2: tea&#10;      Quantity: 30.0 BOX&#10;      Unit price: 12.0 USD/BOX&#10;      Total: 360.0&#10;      Ship term: —&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-11-28&#10;    PO date: —&#10;    PO ref no: PO-2024-11-602&#10;    Vendor: flamingos&#10;    Payment date: Net 30 Days&#10;    Delivery terms: —&#10;    Billing address: Test Customer&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave&#10;&#10;--- Contract #2 ---&#10;  Item 1: paper&#10;      Quantity: 50.0 REAM&#10;      Unit price: 4.0 USD/REAM&#10;      Total: 200.0&#10;      Ship term: —&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-12-05&#10;    PO date: —&#10;    PO ref no: PO-2024-11-602&#10;    Vendor: flamingos&#10;    Payment date: Net 30 Days&#10;    Delivery terms: —&#10;    Billing address: Test Customer&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave&#10;&#10;--- Contract #3 ---&#10;  Item 1: balloons&#10;      Quantity: 4000.0 UNITS&#10;      Unit price: 3.0 USD/UNIT&#10;      Total: 12000.0&#10;      Ship term: —&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-12-12&#10;    PO date: —&#10;    PO ref no: PO-2024-11-602&#10;    Vendor: flamingos&#10;    Payment date: Net 30 Days&#10;    Delivery terms: —&#10;    Billing address: Test Customer&#10;    Shipping method: —&#10;    Shipping address: Changi Hospital Wars 24 Singapore 700339</pre></details> |


### long_single_product_same.json

| Mode | Time taken | Result |
|------|------------|--------|
| only llm no memory | 2.05s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 5.0 BAGS&#10;      Unit price: 23.5 USD/BAG&#10;      Total: 117.5&#10;      Ship term: —&#10;      Packing: 1kg bags, one carton of 5&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-02-10&#10;    PO date: —&#10;    PO ref no: PO-2024-12-202&#10;    Vendor: flamingos&#10;    Payment date: Net 30 Days&#10;    Delivery terms: —&#10;    Billing address: Test Customer&#10;    Shipping method: —&#10;    Shipping address: Changi Hospital Wars 24 Singapore 700339</pre></details> |
| use memory with batching | 8.66s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 5.0 BAGS&#10;      Unit price: 23.5 $&#10;      Total: 117.5&#10;      Ship term: —&#10;      Packing: 1kg bags, one carton of 5&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2025-12-31&#10;    PO date: —&#10;    PO ref no: PO-2024-12-202&#10;    Vendor: flamingos&#10;    Payment date: Net 30 from delivery&#10;    Delivery terms: —&#10;    Billing address: —&#10;    Shipping method: —&#10;    Shipping address: Changi Hospital Wars 24 Singapore 700339</pre></details> |


### long_single_product_single_shipment.json

| Mode | Time taken | Result |
|------|------------|--------|
| only llm no memory | 2.21s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 10.0 BAGS&#10;      Unit price: 23.75 USD/BAG&#10;      Total: 237.5&#10;      Ship term: FOB SINGAPORE&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-11-28&#10;    PO date: —&#10;    PO ref no: PO-2024-11-501&#10;    Vendor: flamingos&#10;    Payment date: Net 30&#10;    Delivery terms: —&#10;    Billing address: —&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave</pre></details> |
| use memory with batching | 9.76s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 10.0 BAGS&#10;      Unit price: 23.75 USD/BAG&#10;      Total: 237.5&#10;      Ship term: FOB Singapore&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-11-28&#10;    PO date: —&#10;    PO ref no: PO-2024-11-501&#10;    Vendor: flamingos&#10;    Payment date: Net 30 from delivery&#10;    Delivery terms: —&#10;    Billing address: Test Customer&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave.</pre></details> |


### short_multi_product_single_shipment.json

| Mode | Time taken | Result |
|------|------------|--------|
| only llm no memory | 4.45s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 8.0 BAG&#10;      Unit price: 25.0 USD/BAG&#10;      Total: 200.0&#10;      Ship term: FOB Singapore&#10;      Packing: —&#10;      Loading: —&#10;  Item 2: Assam tea&#10;      Quantity: 20.0 BOX&#10;      Unit price: 12.0 USD/BOX&#10;      Total: 240.0&#10;      Ship term: FOB Singapore&#10;      Packing: 50 sachets per box&#10;      Loading: —&#10;  Item 3: Copy paper&#10;      Quantity: 40.0 REAM&#10;      Unit price: 4.0 USD/REAM&#10;      Total: 160.0&#10;      Ship term: FOB Singapore&#10;      Packing: A4 80gsm&#10;      Loading: —&#10;  Item 4: Hand sanitizer&#10;      Quantity: 24.0 BOTTLE&#10;      Unit price: 8.0 USD/BOTTLE&#10;      Total: 192.0&#10;      Ship term: FOB Singapore&#10;      Packing: 500ml pump&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2025-12-05&#10;    PO date: —&#10;    PO ref no: PO-2024-12-002&#10;    Vendor: flamingos&#10;    Payment date: Net 30 from delivery&#10;    Delivery terms: —&#10;    Billing address: Test Customer&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave Singapore 018989</pre></details> |
| use memory with batching | 9.08s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 8.0 BAGS&#10;      Unit price: 25.0 $/BAG&#10;      Total: 200.0&#10;      Ship term: FOB SINGAPORE&#10;      Packing: —&#10;      Loading: —&#10;  Item 2: Assam Tea&#10;      Quantity: 20.0 BOXES&#10;      Unit price: 12.0 $/BOX&#10;      Total: 240.0&#10;      Ship term: FOB SINGAPORE&#10;      Packing: —&#10;      Loading: —&#10;  Item 3: Copy Paper&#10;      Quantity: 40.0 REAMS&#10;      Unit price: 4.0 $/REAM&#10;      Total: 160.0&#10;      Ship term: FOB SINGAPORE&#10;      Packing: —&#10;      Loading: —&#10;  Item 4: Hand Sanitizer&#10;      Quantity: 24.0 BOTTLES&#10;      Unit price: 8.0 $/BOTTLE&#10;      Total: 192.0&#10;      Ship term: FOB SINGAPORE&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2025-12-05&#10;    PO date: —&#10;    PO ref no: PO-2024-12-002&#10;    Vendor: flamingos&#10;    Payment date: Net 30 from delivery&#10;    Delivery terms: FOB Singapore&#10;    Billing address: Test Customer&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave Singapore 018989</pre></details> |


### short_multi_shipment_multi_product.json

| Mode | Time taken | Result |
|------|------------|--------|
| only llm no memory | 3.41s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 12.0 BAGS&#10;      Unit price: 250.0 USD&#10;      Total: 3000.0&#10;      Ship term: —&#10;      Packing: —&#10;      Loading: —&#10;  Item 2: Assam tea&#10;      Quantity: 30.0 BOXES&#10;      Unit price: 360.0 USD&#10;      Total: 10800.0&#10;      Ship term: —&#10;      Packing: 50 sachets/box&#10;      Loading: —&#10;  Item 3: copy paper&#10;      Quantity: 50.0 REAMS&#10;      Unit price: 200.0 USD&#10;      Total: 10000.0&#10;      Ship term: —&#10;      Packing: A4 80gsm&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2024-11-28&#10;    PO date: —&#10;    PO ref no: PO-2024-11-301&#10;    Vendor: flamingos&#10;    Payment date: Net 30 Days&#10;    Delivery terms: —&#10;    Billing address: 100 Finance Ave&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave&#10;&#10;--- Contract #2 ---&#10;  Item 1: Red Balloons&#10;      Quantity: 3000.0 UNITS&#10;      Unit price: 3.0 USD/K&#10;      Total: 9000.0&#10;      Ship term: —&#10;      Packing: 1000 per box&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2024-12-12&#10;    PO date: —&#10;    PO ref no: PO-2024-11-301&#10;    Vendor: flamingos&#10;    Payment date: Net 30 Days&#10;    Delivery terms: —&#10;    Billing address: 100 Finance Ave&#10;    Shipping method: —&#10;    Shipping address: Changi Hospital Wars 24 Singapore 700339</pre></details> |
| use memory with batching | 9.09s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: Coffee&#10;      Quantity: 12.0 BAGS&#10;      Unit price: 250.0 USD&#10;      Total: 3000.0&#10;      Ship term: EXW&#10;      Packing: —&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-11-28&#10;    PO date: —&#10;    PO ref no: PO-2024-11-301&#10;    Vendor: flamingos&#10;    Payment date: Net 30 from Dec 12&#10;    Delivery terms: —&#10;    Billing address: —&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave&#10;&#10;--- Contract #2 ---&#10;  Item 1: Tea&#10;      Quantity: 30.0 BOXES&#10;      Unit price: 360.0 USD&#10;      Total: 10800.0&#10;      Ship term: EXW&#10;      Packing: 50 sachets/box&#10;      Loading: —&#10;  Item 2: Paper&#10;      Quantity: 50.0 REAMS&#10;      Unit price: 200.0 USD&#10;      Total: 10000.0&#10;      Ship term: EXW&#10;      Packing: A4 80gsm&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-12-05&#10;    PO date: —&#10;    PO ref no: PO-2024-11-301&#10;    Vendor: flamingos&#10;    Payment date: Net 30 from Dec 12&#10;    Delivery terms: —&#10;    Billing address: —&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave&#10;&#10;--- Contract #3 ---&#10;  Item 1: Balloons&#10;      Quantity: 3000.0 PIECES&#10;      Unit price: 9.0 USD&#10;      Total: 27000.0&#10;      Ship term: EXW&#10;      Packing: 1000-per-box packaging&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-12-12&#10;    PO date: —&#10;    PO ref no: PO-2024-11-301&#10;    Vendor: flamingos&#10;    Payment date: Net 30 from Dec 12&#10;    Delivery terms: —&#10;    Billing address: —&#10;    Shipping method: —&#10;    Shipping address: Changi Hospital Wars 24 Singapore 700339</pre></details> |


### short_single_product_same.json

| Mode | Time taken | Result |
|------|------------|--------|
| only llm no memory | 2.05s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 5.0 BAGS&#10;      Unit price: 25.0 USD/EACH&#10;      Total: 125.0&#10;      Ship term: —&#10;      Packing: 1kg bags, carton of 10&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2025-11-30&#10;    PO date: —&#10;    PO ref no: PO-2024-11-401&#10;    Vendor: flamingos&#10;    Payment date: Net 30&#10;    Delivery terms: —&#10;    Billing address: Test Customer,&#10;    Shipping method: —&#10;    Shipping address: Changi Hospital Wars 24 Singapore 700339</pre></details> |
| use memory with batching | 7.51s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 5.0 BAGS&#10;      Unit price: 25.0 USD/EACH&#10;      Total: 125.0&#10;      Ship term: —&#10;      Packing: 1kg bags, carton of 10&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-11-30&#10;    PO date: —&#10;    PO ref no: PO-2024-11-401&#10;    Vendor: flamingos&#10;    Payment date: Net 30&#10;    Delivery terms: —&#10;    Billing address: —&#10;    Shipping method: —&#10;    Shipping address: Changi Hospital Wars 24 Singapore 700339</pre></details> |


### short_single_product_single_shipment.json

| Mode | Time taken | Result |
|------|------------|--------|
| only llm no memory | 2.46s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 6.0 BAGS&#10;      Unit price: 25.0 USD/BAG&#10;      Total: 150.0&#10;      Ship term: EXW SINGAPORE&#10;      Packing: Standard 1kg bags, carton of 10&#10;      Loading: Main loading bay, Gate B&#10;  Key details:&#10;    DO date: 2026-11-28&#10;    PO date: —&#10;    PO ref no: PO-2024-11-101&#10;    Vendor: flamingos&#10;    Payment date: Net 30&#10;    Delivery terms: —&#10;    Billing address: Test Customer, 100 Finance Ave Singapore 018989&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave Singapore 018989</pre></details> |
| use memory with batching | 7.76s | <details><summary>View contract summary</summary><pre>--- Contract #1 ---&#10;  Item 1: KNM Coffee&#10;      Quantity: 6.0 BAGS&#10;      Unit price: 25.0 USD/BAG&#10;      Total: 150.0&#10;      Ship term: —&#10;      Packing: STANDARD 1KG BAGS, CARTON OF 10&#10;      Loading: —&#10;  Key details:&#10;    DO date: 2026-11-28&#10;    PO date: —&#10;    PO ref no: PO-2024-11-101&#10;    Vendor: flamingos&#10;    Payment date: Net 30&#10;    Delivery terms: —&#10;    Billing address: Test Customer, 100 Finance Ave Singapore 018989&#10;    Shipping method: —&#10;    Shipping address: 100 Finance Ave Singapore 018989</pre></details> |


---

---

## long_multi_product_single_shipment.json — only llm no memory

- **USER_ID**: `010000`
- **Time taken**: 3.10s

### Contract summary

```
--- Contract #1 ---
  Item 1: Coffee
      Quantity: 10.0 BAGS
      Unit price: 25.0 USD/BAG
      Total: 250.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 2: Tea
      Quantity: 15.0 BOXES
      Unit price: 12.0 USD/BOX
      Total: 180.0
      Ship term: FOB Singapore
      Packing: 50 sachets per box
      Loading: —
  Item 3: Paper
      Quantity: 40.0 REAMS
      Unit price: 4.0 USD/REAM
      Total: 160.0
      Ship term: FOB Singapore
      Packing: —
      Loading: —
  Item 4: Sanitizer
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
    Payment date: Net 30 from delivery
    Delivery terms: FOB Singapore
    Billing address: —
    Shipping method: Truck
    Shipping address: 100 Finance Ave
```


## long_multi_product_single_shipment.json — use memory with batching

- **USER_ID**: `010100`
- **Time taken**: 10.35s

### Contract summary

```
--- Contract #1 ---
  Item 1: Coffee
      Quantity: 10.0 BAG
      Unit price: 25.0 USD/BAG
      Total: 250.0
      Ship term: FOB SINGAPORE
      Packing: —
      Loading: —
  Item 2: Tea
      Quantity: 15.0 BOX
      Unit price: 12.0 USD/BOX
      Total: 180.0
      Ship term: FOB SINGAPORE
      Packing: 50 sachets per box
      Loading: —
  Item 3: Sanitizer
      Quantity: 24.0 BOTTLE
      Unit price: 8.0 USD/BOTTLE
      Total: 192.0
      Ship term: FOB SINGAPORE
      Packing: 500ml pump bottle
      Loading: —
  Item 4: Paper
      Quantity: 40.0 REAM
      Unit price: 4.0 USD/REAM
      Total: 160.0
      Ship term: FOB SINGAPORE
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave
```


## long_multi_shipment_multi_product.json — only llm no memory

- **USER_ID**: `020000`
- **Time taken**: 3.56s

### Contract summary

```
--- Contract #1 ---
  Item 1: coffee
      Quantity: 12.0 BAG
      Unit price: 25.0 $
      Total: 300.0
      Ship term: —
      Packing: —
      Loading: —
  Item 2: tea
      Quantity: 30.0 BOX
      Unit price: 12.0 $
      Total: 360.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2025-11-28
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: NET 30
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: paper
      Quantity: 50.0 REAM
      Unit price: 4.0 $
      Total: 200.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2025-12-05
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: NET 30
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: balloons
      Quantity: 4000.0 —
      Unit price: 3.0 $
      Total: 12000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2025-12-12
    PO date: —
    PO ref no: —
    Vendor: flamingos
    Payment date: NET 30
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_multi_shipment_multi_product.json — use memory with batching

- **USER_ID**: `020100`
- **Time taken**: 13.26s

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
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
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
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: balloons
      Quantity: 4000.0 UNITS
      Unit price: 3.0 USD/UNIT
      Total: 12000.0
      Ship term: —
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-602
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_single_product_same.json — only llm no memory

- **USER_ID**: `030000`
- **Time taken**: 2.05s

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
    DO date: 2026-02-10
    PO date: —
    PO ref no: PO-2024-12-202
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_single_product_same.json — use memory with batching

- **USER_ID**: `030100`
- **Time taken**: 8.66s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 BAGS
      Unit price: 23.5 $
      Total: 117.5
      Ship term: —
      Packing: 1kg bags, one carton of 5
      Loading: —
  Key details:
    DO date: 2025-12-31
    PO date: —
    PO ref no: PO-2024-12-202
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## long_single_product_single_shipment.json — only llm no memory

- **USER_ID**: `040000`
- **Time taken**: 2.21s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 10.0 BAGS
      Unit price: 23.75 USD/BAG
      Total: 237.5
      Ship term: FOB SINGAPORE
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-501
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave
```


## long_single_product_single_shipment.json — use memory with batching

- **USER_ID**: `040100`
- **Time taken**: 9.76s

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
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-501
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave.
```


## short_multi_product_single_shipment.json — only llm no memory

- **USER_ID**: `050000`
- **Time taken**: 4.45s

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
      Packing: 50 sachets per box
      Loading: —
  Item 3: Copy paper
      Quantity: 40.0 REAM
      Unit price: 4.0 USD/REAM
      Total: 160.0
      Ship term: FOB Singapore
      Packing: A4 80gsm
      Loading: —
  Item 4: Hand sanitizer
      Quantity: 24.0 BOTTLE
      Unit price: 8.0 USD/BOTTLE
      Total: 192.0
      Ship term: FOB Singapore
      Packing: 500ml pump
      Loading: —
  Key details:
    DO date: 2025-12-05
    PO date: —
    PO ref no: PO-2024-12-002
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: —
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```


## short_multi_product_single_shipment.json — use memory with batching

- **USER_ID**: `050100`
- **Time taken**: 9.08s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 8.0 BAGS
      Unit price: 25.0 $/BAG
      Total: 200.0
      Ship term: FOB SINGAPORE
      Packing: —
      Loading: —
  Item 2: Assam Tea
      Quantity: 20.0 BOXES
      Unit price: 12.0 $/BOX
      Total: 240.0
      Ship term: FOB SINGAPORE
      Packing: —
      Loading: —
  Item 3: Copy Paper
      Quantity: 40.0 REAMS
      Unit price: 4.0 $/REAM
      Total: 160.0
      Ship term: FOB SINGAPORE
      Packing: —
      Loading: —
  Item 4: Hand Sanitizer
      Quantity: 24.0 BOTTLES
      Unit price: 8.0 $/BOTTLE
      Total: 192.0
      Ship term: FOB SINGAPORE
      Packing: —
      Loading: —
  Key details:
    DO date: 2025-12-05
    PO date: —
    PO ref no: PO-2024-12-002
    Vendor: flamingos
    Payment date: Net 30 from delivery
    Delivery terms: FOB Singapore
    Billing address: Test Customer
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```


## short_multi_shipment_multi_product.json — only llm no memory

- **USER_ID**: `060000`
- **Time taken**: 3.41s

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
    DO date: 2024-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: 100 Finance Ave
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Red Balloons
      Quantity: 3000.0 UNITS
      Unit price: 3.0 USD/K
      Total: 9000.0
      Ship term: —
      Packing: 1000 per box
      Loading: —
  Key details:
    DO date: 2024-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 Days
    Delivery terms: —
    Billing address: 100 Finance Ave
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_multi_shipment_multi_product.json — use memory with batching

- **USER_ID**: `060100`
- **Time taken**: 9.09s

### Contract summary

```
--- Contract #1 ---
  Item 1: Coffee
      Quantity: 12.0 BAGS
      Unit price: 250.0 USD
      Total: 3000.0
      Ship term: EXW
      Packing: —
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #2 ---
  Item 1: Tea
      Quantity: 30.0 BOXES
      Unit price: 360.0 USD
      Total: 10800.0
      Ship term: EXW
      Packing: 50 sachets/box
      Loading: —
  Item 2: Paper
      Quantity: 50.0 REAMS
      Unit price: 200.0 USD
      Total: 10000.0
      Ship term: EXW
      Packing: A4 80gsm
      Loading: —
  Key details:
    DO date: 2026-12-05
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: 100 Finance Ave

--- Contract #3 ---
  Item 1: Balloons
      Quantity: 3000.0 PIECES
      Unit price: 9.0 USD
      Total: 27000.0
      Ship term: EXW
      Packing: 1000-per-box packaging
      Loading: —
  Key details:
    DO date: 2026-12-12
    PO date: —
    PO ref no: PO-2024-11-301
    Vendor: flamingos
    Payment date: Net 30 from Dec 12
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_single_product_same.json — only llm no memory

- **USER_ID**: `070000`
- **Time taken**: 2.05s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 BAGS
      Unit price: 25.0 USD/EACH
      Total: 125.0
      Ship term: —
      Packing: 1kg bags, carton of 10
      Loading: —
  Key details:
    DO date: 2025-11-30
    PO date: —
    PO ref no: PO-2024-11-401
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer,
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_single_product_same.json — use memory with batching

- **USER_ID**: `070100`
- **Time taken**: 7.51s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 5.0 BAGS
      Unit price: 25.0 USD/EACH
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
    Delivery terms: —
    Billing address: —
    Shipping method: —
    Shipping address: Changi Hospital Wars 24 Singapore 700339
```


## short_single_product_single_shipment.json — only llm no memory

- **USER_ID**: `080000`
- **Time taken**: 2.46s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 6.0 BAGS
      Unit price: 25.0 USD/BAG
      Total: 150.0
      Ship term: EXW SINGAPORE
      Packing: Standard 1kg bags, carton of 10
      Loading: Main loading bay, Gate B
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-101
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave Singapore 018989
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```


## short_single_product_single_shipment.json — use memory with batching

- **USER_ID**: `080100`
- **Time taken**: 7.76s

### Contract summary

```
--- Contract #1 ---
  Item 1: KNM Coffee
      Quantity: 6.0 BAGS
      Unit price: 25.0 USD/BAG
      Total: 150.0
      Ship term: —
      Packing: STANDARD 1KG BAGS, CARTON OF 10
      Loading: —
  Key details:
    DO date: 2026-11-28
    PO date: —
    PO ref no: PO-2024-11-101
    Vendor: flamingos
    Payment date: Net 30
    Delivery terms: —
    Billing address: Test Customer, 100 Finance Ave Singapore 018989
    Shipping method: —
    Shipping address: 100 Finance Ave Singapore 018989
```

