import re

def parse_receipt_text(text: str) -> list[dict]:
    items = []
    pattern = re.compile(r"([A-Za-zÀ-ÿ0-9\s]+)\s+(\d+[\.,]?\d*)\s+x\s+(\d+[\.,]?\d*)\s*=\s*(\d+[\.,]?\d*)")
    for line in text.splitlines():
        m = pattern.search(line)
        if m:
            items.append({
                "product_name": m.group(1).strip(),
                "quantity": float(m.group(2).replace(',', '.')),
                "unit_price": float(m.group(3).replace(',', '.')),
                "total_price": float(m.group(4).replace(',', '.')),
            })
    return items
