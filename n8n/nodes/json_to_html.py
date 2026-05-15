# n8n Code node: JSON TO HTML (Dahi Cheeni)
# LOGO_DATA_URI is replaced by patch_workflow.py

LOGO_DATA_URI = "__LOGO_DATA_URI__"

try:
    cust_list = _input.all("Customer Details")
    cust = cust_list[0].json if cust_list else {}
except Exception:
    cust = {}

menu_items = _input.all("Proposed Menu")
services = _input.all("Other Services")

logo_url = LOGO_DATA_URI
brand = "#5c1a1a"
cream = "#f5ebe0"
gold = "#c9a227"


def fmt_money(val):
    if val is None or val == "":
        return ""
    try:
        s = str(val).replace(",", "").strip()
        v = float(s)
        return f"₹{int(v):,}" if v == int(v) else f"₹{v:,.2f}"
    except Exception:
        return str(val)


html = f"""<!DOCTYPE html>
<html>
<head>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&display=swap');
  @page {{ margin: 14mm; }}
  body {{ font-family: 'Source Sans 3', sans-serif; color: #222; margin: 0; line-height: 1.55; padding-bottom: 20mm; }}
  .footer {{ position: fixed; bottom: 0; left: 0; right: 0; text-align: center; font-size: 9px; color: #555; border-top: 1px solid #ddd; padding-top: 6px; }}
  h1, h2, h3 {{ font-family: 'Cormorant Garamond', serif; color: {brand}; }}
  .logo-wrap {{ text-align: center; padding: 6px 0 14px; }}
  .main-logo {{ max-width: 240px; height: auto; }}
  .intro-box {{ background: {brand}; color: {cream}; padding: 20px 22px; border-radius: 10px; margin-bottom: 18px; }}
  .intro-box p {{ margin: 0 0 10px; font-size: 13px; }}
  .intro-box strong {{ color: {gold}; }}
  .header-banner {{ background: {brand}; color: {cream}; padding: 14px 18px; border-radius: 8px; margin-bottom: 14px; }}
  .header-banner h1 {{ color: {cream} !important; text-align: center; font-size: 26px; margin: 0; }}
  .header-details {{ margin-top: 10px; font-size: 12px; border-top: 1px solid rgba(255,255,255,0.25); padding-top: 8px; }}
  .detail-row {{ display: table; width: 100%; }}
  .detail-row > div {{ display: table-cell; width: 50%; padding: 3px 0; }}
  h2 {{ font-size: 18px; border-bottom: 2px solid {brand}; padding-bottom: 4px; margin-top: 16px; text-transform: uppercase; letter-spacing: 0.5px; }}
  .data-table {{ width: 100%; border-collapse: collapse; margin-top: 8px; table-layout: fixed; }}
  .data-table th {{ background: {brand}; color: {cream}; padding: 8px; border: 1px solid {brand}; font-size: 11px; }}
  .data-table th.num {{ text-align: center; }}
  .data-table td {{ padding: 8px; border: 1px solid #ccc; font-size: 12px; vertical-align: top; word-wrap: break-word; }}
  .data-table td.num {{ text-align: center; }}
  .cat-row td {{ background: #f3ebe8; font-weight: 700; color: {brand}; font-family: 'Cormorant Garamond', serif; font-size: 14px; }}
  .description {{ font-size: 10px; color: #555; font-style: italic; display: block; margin-top: 4px; }}
  .badge {{ font-size: 9px; padding: 2px 6px; border-radius: 10px; background: #eee; margin-left: 6px; font-weight: 600; }}
  .total-row td {{ font-weight: 700; background: #faf6f4; }}
  .note-list {{ font-size: 12px; padding-left: 18px; }}
  .note-list li {{ margin-bottom: 8px; }}
</style>
</head>
<body>

<div class="footer">
  <strong>Dahi Cheeni — Home-Style Catering</strong><br>
  For intimate gatherings
</div>

<div class="logo-wrap">
  <img src="{logo_url}" class="main-logo" alt="Dahi Cheeni">
</div>

<div class="intro-box">
  <p><strong>Welcome to Dahi Cheeni</strong></p>
  <p>Thank you for considering us for your gathering. This quotation outlines our <strong>home-style catering</strong> menu — thoughtfully prepared for intimate celebrations.</p>
  <p>Every dish is priced as <strong>quantity × rate</strong>. We look forward to being part of your event.</p>
  <p><strong>Warm regards,<br>Team Dahi Cheeni</strong></p>
</div>

<div style="page-break-before: always;"></div>

<div class="logo-wrap">
  <img src="{logo_url}" class="main-logo" alt="Dahi Cheeni">
</div>

<div class="header-banner">
  <h1>EVENT QUOTATION</h1>
  <div class="header-details">
    <div class="detail-row">
      <div><strong>HOST:</strong> {cust.get('Host Name', 'N/A')}</div>
      <div><strong>MOBILE:</strong> {cust.get('Mobile No', 'N/A')}</div>
    </div>
    <div class="detail-row">
      <div><strong>DATE:</strong> {cust.get('Event Date', 'N/A')}</div>
      <div><strong>TIME:</strong> {cust.get('Time', 'N/A')}</div>
    </div>
    <div class="detail-row">
      <div><strong>LOCATION:</strong> {cust.get('Location', 'N/A')}</div>
      <div><strong>PAX:</strong> {cust.get('Pax', 'N/A')}</div>
    </div>
  </div>
</div>

<h2>Proposed Menu</h2>
"""

from collections import OrderedDict

categories = OrderedDict()
for item in menu_items:
    d = item.json
    name = (d.get("Name") or "").strip()
    if not name:
        continue
    cat = d.get("Category") or "Other"
    categories.setdefault(cat, []).append(d)

for cat, items in categories.items():
    html += f"""
<table class="data-table">
  <colgroup>
    <col style="width:52%" />
    <col style="width:12%" />
    <col style="width:18%" />
    <col style="width:18%" />
  </colgroup>
  <thead>
    <tr class="cat-row"><td colspan="4">{cat.upper()}</td></tr>
    <tr>
      <th>ITEM</th>
      <th class="num">QTY</th>
      <th class="num">RATE</th>
      <th class="num">AMOUNT</th>
    </tr>
  </thead>
  <tbody>
"""
    for d in items:
        qty = d.get("Qty", d.get("Portions", ""))
        veg = (d.get("Veg/Non Veg") or d.get("VegNonVeg") or "").strip()
        badge = f'<span class="badge">{veg}</span>' if veg else ""
        html += f"""
    <tr>
      <td><strong>{d.get('Name', '')}</strong>{badge}
        <span class="description">{d.get('Description', '')}</span>
      </td>
      <td class="num">{qty}</td>
      <td class="num">{fmt_money(d.get('Rate', ''))}</td>
      <td class="num">{fmt_money(d.get('Amount', ''))}</td>
    </tr>
"""
    html += "</tbody></table>"

html += """
<h2>Other Services &amp; Summary</h2>
<table class="data-table">
  <tbody>
"""

for s in services:
    sd = s.json
    label = (sd.get("Other Services") or "").strip()
    if not label:
        continue
    amount = fmt_money(sd.get("Amount", ""))
    row_class = "total-row" if any(x in label.upper() for x in ("TOTAL", "SUBTOTAL", "GST")) else ""
    html += f'<tr class="{row_class}"><td colspan="3">{label}</td><td class="num">{amount}</td></tr>'

html += f"""
  </tbody>
</table>

<div style="page-break-before: always; margin-top: 20px;">
  <div class="logo-wrap">
    <img src="{logo_url}" class="main-logo" alt="Dahi Cheeni">
  </div>
  <h3 style="text-decoration: underline;">Please Note</h3>
  <ul class="note-list">
    <li><strong>Pricing:</strong> Menu amounts are calculated as quantity × rate.</li>
    <li><strong>GST:</strong> 5% GST is applied on the subtotal including additional services.</li>
    <li><strong>Menu confirmation:</strong> Please confirm the final menu 4–5 days before the event.</li>
    <li><strong>Booking:</strong> Bookings are subject to availability.</li>
    <li><strong>Kitchen access:</strong> A working kitchen or agreed setup space should be available where applicable.</li>
  </ul>
</div>

</body>
</html>
"""

return [{"html_content": html}]
