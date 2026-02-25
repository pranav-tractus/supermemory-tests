import orjson
from datetime import date
from typing import Any
from base_utils import add_seq_numbers
from model import (
    LLMExtractContractProductItem,
    SalesOrderExtractContractKeyDetails,
    SOExtractContractList,
)

today = date.today()
iso_date = today.isoformat()

team_info = {
    "name": "flamingos",
    "email": "somesh@tractuslabs.com",
    "phone": "+000000000000",
    "contact_point": "Somesh Harsh",
}
customer_info = {
    "name": "Test Customer",
    "email": "client@example.com",
    "id": "432eef62-3867-46b7-abf0-cdb2a09183d6",
}

generic_deal_terms = (
    "deal agreement order purchase sale delivery quantity price terms "
    "contract shipment address date product item confirm change cancel "
    "payment invoice due date buyer seller vendor customer client "
    "units kg tons metric warranty guarantee condition discount rate total amount "
    "schedule timeline deadline specification specs quality grade "
    "purchase order PO sales order confirmation accepted approval "
    "amendment revision update dispute claim complaint "
    "fulfillment dispatch shipping warehouse storage "
    "tax GST customs currency USD INR incoterms FOB CIF "
    "quantity confirmed lead time ETA ETD"
)


def get_contract_generation_prompt(
    messages: list[dict], organization_info: dict, customer_info: dict
) -> str:
    return f"""
# ROLE
You are a specialized Contract Data Extraction Agent. Your goal is to convert unstructured business chat logs into a precise, structured JSON contract object.

# CONTEXT & DATA
- **Current Date (ISO):** {iso_date}
- **Vendor Information (Team 1):** {orjson.dumps(organization_info, option=orjson.OPT_INDENT_2).decode("utf-8")}
- **Counterparty Information (Team 2):** {orjson.dumps(customer_info, option=orjson.OPT_INDENT_2).decode("utf-8")}

# INPUT CHAT LOGS
{orjson.dumps(add_seq_numbers(messages), option=orjson.OPT_INDENT_2).decode("utf-8")}

# EXTRACTION RULES
1. **The Agreement Principle:** Only extract data where both Team 1 and Team 2 have reached an explicit consensus. If one team proposes a price and the other counters or remains silent, do NOT extract that value.
2. **Sequential Priority:** Use the `seq` integer to track the conversation flow. If a value (like price) is updated later in the chat, the highest `seq` number representing agreement takes precedence.
3. **Date Logic:** - Use `{iso_date}` as the reference point.
   - For "Delivery Date" or "DO Date": If a specific day is missing (e.g., "Jan 2026"), default to the **last day of that month** (e.g., "2026-01-31").
   - All the dates should be considered in the same year as the current date, unless mentioned otherwise.
4. **Conditional Defaults (Packing/Loading):**
   - If packing/loading info is missing from the chat:
     - If Product is "Fat Powder": Set loading to "23MT/40'FCL".
     - If Product is "Feeds": Set loading to "12MT/20'FCL".
   - "Packing" refers to the physical container (e.g., "25kg paper bags").
5. **Shipping Terms:** Must follow the format: `[INCOTERM] [PORT NAME]`. 
   - Valid Incoterms: EXW, FOB, CIF, DDP. 
   - Example: "FOB Busan".
6. **Strictness:** You are not allowed to add anything else in the outputs, except the fields and the values mentioned in the messages. If a field is not mentioned or agreed upon, return `null` or omit based on the schema.
7. **Pricing and Total:** The pricing and total should be the final agreed upon price and total, not the initial proposal.

# OUTPUT REQUIREMENTS
- Output must be **valid JSON**.
- No conversational filler or markdown outside of the JSON block.
- Keep all units and currencies exactly as they appear in the text (e.g., "$500/MT").

"""


def _fmt(val: Any) -> str:
    """Format value for display; empty/None becomes placeholder."""
    if val is None or val == "":
        return "—"
    return str(val).strip()


def _format_item(item: LLMExtractContractProductItem, idx: int) -> list[str]:
    """Format a single product line item (all fields shown, empty as —)."""
    desc = _fmt(item.description)
    lines = [f"  Item {idx}: {desc if desc != '—' else '(no description)'}"]
    lines.append(f"      Quantity: {_fmt(item.quantity)} {_fmt(item.quantity_unit)}")
    lines.append(f"      Unit price: {_fmt(item.unit_price)} {_fmt(item.pricing_unit)}")
    lines.append(f"      Total: {_fmt(item.total)}")
    for label, key in [
        ("Ship term", "ship_term"),
        ("Packing", "packing"),
        ("Loading", "loading"),
    ]:
        lines.append(f"      {label}: {_fmt(getattr(item, key, ''))}")
    return lines


def _format_contract(
    contract: SalesOrderExtractContractKeyDetails, contract_idx: int
) -> list[str]:
    """Format one contract (header + items + key details)."""
    lines = [f"--- Contract #{contract_idx} ---"]
    for i, item in enumerate(contract.items, start=1):
        lines.extend(_format_item(item, i))
    # Key details (all fields shown, empty as —)
    details = [
        ("DO date", contract.do_date),
        ("PO date", contract.po_date),
        ("PO ref no", contract.po_ref_no),
        ("Vendor", contract.vendor_name),
        ("Payment date", contract.payment_date),
        ("Delivery terms", contract.delivery_terms),
        ("Billing address", contract.billing_address),
        ("Shipping method", contract.shipping_method),
        ("Shipping address", contract.shipping_address),
    ]
    lines.append("  Key details:")
    for label, val in details:
        lines.append(f"    {label}: {_fmt(val)}")
    return lines


def format_contract_summary(summary: SOExtractContractList) -> str:
    """Pretty-print contract summary for console."""
    if not summary or not getattr(summary, "data", None):
        return "(No contract data)"
    lines = []
    for idx, contract in enumerate(summary.data, start=1):
        lines.extend(_format_contract(contract, idx))
        lines.append("")
    return "\n".join(lines).rstrip()
