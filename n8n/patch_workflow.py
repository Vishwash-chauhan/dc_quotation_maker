#!/usr/bin/env python3
"""Inject Dahi Cheeni node code into quotation-workflow.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / "quotation-workflow.json"
NODES = ROOT / "nodes"

NODE_FILES = {
    "Menu Item Transformation": "menu_transform.py",
    "Code in Python (Beta)": "other_services.py",
    "Customer Details": "customer_details.py",
    "JSON TO HTML": "json_to_html.py",
}


def main():
    with WORKFLOW.open(encoding="utf-8") as f:
        wf = json.load(f)

    for node in wf["nodes"]:
        name = node.get("name")
        if name not in NODE_FILES:
            continue
        code = (NODES / NODE_FILES[name]).read_text(encoding="utf-8")
        node.setdefault("parameters", {})["pythonCode"] = code
        print(f"Updated: {name}")

    # Host-info node no longer used in PDF — return empty list
    for node in wf["nodes"]:
        if node.get("name") == "Code in Python (Beta)13":
            node["parameters"]["pythonCode"] = "return []"

    sticky = next((n for n in wf["nodes"] if n.get("name") == "Sticky Note"), None)
    if sticky:
        sticky["parameters"]["content"] = (
            "Dahi Cheeni quotation workflow\n"
            "Form: form.html\n"
            "Pricing: Qty × Rate\n"
            "Re-import this JSON after edits, then activate workflow."
        )

    with WORKFLOW.open("w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)
    print(f"Wrote {WORKFLOW}")


if __name__ == "__main__":
    main()
