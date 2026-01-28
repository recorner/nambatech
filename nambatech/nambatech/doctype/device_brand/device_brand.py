# Copyright (c) 2026, penvise and contributors
# For license information, please see license.txt

# import frappe
import re
import frappe
from frappe.model.document import Document
from frappe.model.naming import getseries

def _normalize_code(value: str) -> str:
    value = (value or "").strip().upper()
    value = re.sub(r"[^A-Z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value

class DeviceBrand(Document):
    def autoname(self):
        base = _normalize_code(self.brand_code)

        if not base:
            base = _normalize_code(self.brand_name)

        if not base:
            frappe.throw("Brand Code or Brand Name is required.")

        if not frappe.db.exists(self.doctype, base):
            self.name = base
            if not self.brand_code:
                self.brand_code = base
            return

        suffix = getseries(f"{base}-", 3)
        self.name = f"{base}-{suffix}"

        if not self.brand_code:
            self.brand_code = base
