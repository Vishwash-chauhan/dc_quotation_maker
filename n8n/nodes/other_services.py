# n8n Code node: Other Services & GST (Dahi Cheeni)
body = _input.all()[0].json.get("body", {})


def extract_number(val):
    if not val or isinstance(val, (int, float)):
        return val or 0
    import re
    match = re.search(r"[\d.]+", str(val).strip())
    if not match:
        return 0
    try:
        return float(match.group())
    except Exception:
        return 0


items = body.get("Items", [])
if items and isinstance(items, list):
    sub_val = sum(extract_number(it.get("Amount", 0)) for it in items)
else:
    sub_val = extract_number(body.get("Total", 0))

chef_val = extract_number(body.get("ChefServers", 0))
decor_val = extract_number(body.get("TableDecor", 0))
cutlery_val = extract_number(body.get("Cutlery", 0))
chaffing_val = extract_number(body.get("Chaffing", 0))
conv_val = extract_number(body.get("Conveyance", 0))
venue_val = extract_number(body.get("VenueCharges", 0))

subtotal_with_services = sub_val + chef_val + decor_val + cutlery_val + chaffing_val + conv_val + venue_val
gst_amount = subtotal_with_services * 0.05
total_amount = subtotal_with_services + gst_amount

return [
    {"Other Services": "Subtotal (Items)", "Amount": sub_val},
    {"Other Services": "Chef + Servers + Helper", "Amount": body.get("ChefServers", 0)},
    {"Other Services": "Table Décor (As Per Theme)", "Amount": body.get("TableDecor", 0)},
    {"Other Services": "Cutlery & Crockery", "Amount": body.get("Cutlery", 0)},
    {"Other Services": "Chaffing Dishes & Snack Warmers", "Amount": body.get("Chaffing", 0)},
    {"Other Services": "Conveyance", "Amount": body.get("Conveyance", 0)},
    {"Other Services": "Venue Charges", "Amount": body.get("VenueCharges", 0)},
    {"Other Services": "Subtotal (With Services)", "Amount": subtotal_with_services},
    {"Other Services": "GST 5%", "Amount": round(gst_amount, 2)},
    {"Other Services": "TOTAL AMOUNT", "Amount": round(total_amount, 2)},
]
