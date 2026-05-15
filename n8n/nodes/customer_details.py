# n8n Code node: Customer Details (Dahi Cheeni)
body = _input.all()[0].json.get("body", {})

return [{
    "Event Date": body.get("EventDate", "N/A"),
    "Host Name": body.get("HostName", "N/A"),
    "Mobile No": body.get("MobileNo", "N/A"),
    "Time": body.get("Time", "N/A"),
    "Pax": body.get("Pax", "N/A"),
    "Location": body.get("Location", "N/A"),
    "Quote ID": body.get("QuotationId", ""),
}]
