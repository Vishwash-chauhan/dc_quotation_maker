# n8n Code node: Menu Item Transformation (Dahi Cheeni — qty × rate)
input_data = _input.all()[0].json
items_list = input_data.get("body", {}).get("Items", [])

output = []
for item in items_list:
    qty = item.get("Qty", item.get("Portions", 1))
    rate = item.get("Rate", 0)
    try:
        amount = float(item.get("Amount", 0))
    except (TypeError, ValueError):
        try:
            amount = float(qty or 0) * float(rate or 0)
        except (TypeError, ValueError):
            amount = 0
    output.append({
        "Name": item.get("Name"),
        "Description": item.get("Description"),
        "Qty": qty,
        "Rate": rate,
        "Category": item.get("Category", ""),
        "Veg/Non Veg": item.get("VegNonVeg", ""),
        "Amount": amount,
    })

return output
