# Copyright (c) 2026, penvise and contributors
# For license information, please see license.txt

# import frappe
# apps/nambatech/nambatech/doctype/device_model/device_model.py

import re
import frappe
from frappe.model.document import Document
from frappe.model.naming import getseries

def _norm(value: str) -> str:
    """Normalize to A-Z0-9 and hyphens."""
    value = (value or "").strip().upper()
    value = re.sub(r"[^A-Z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value

def _get_brand_code(brand: str) -> str:
    """
    brand is Link -> Device Brand (brand docname).
    We try to read brand_code field from Device Brand.
    If your Device Brand 'name' is already the code (APPLE), this still works.
    """
    if not brand:
        return ""

    brand_code = frappe.db.get_value("Device Brand", brand, "brand_code")
    if brand_code:
        return _norm(brand_code)

    # fallback: if brand_code field missing/not set, use the linked docname
    return _norm(brand)

class DeviceModel(Document):
    def autoname(self):
        # Expected fieldnames (per our design):
        # brand (Link -> Device Brand)
        # model_code (Data)
        # model_name (Data)

        if not self.brand:
            frappe.throw("Brand is required.")

        brand_code = _get_brand_code(self.brand)

        # Use model_code if provided; fallback to model_name
        mcode = _norm(self.model_code)
        if not mcode:
            mcode = _norm(self.model_name)

        if not brand_code:
            frappe.throw("Brand Code could not be resolved from Device Brand.")
        if not mcode:
            frappe.throw("Model Code or Model Name is required.")

        base = f"{brand_code}-{mcode}"

        # Use base if unique, else append series
        if not frappe.db.exists(self.doctype, base):
            self.name = base
            # Backfill model_code if empty, so it becomes stable for future
            if not (self.model_code or "").strip():
                self.model_code = mcode
            return

        suffix = getseries(f"{base}-", 3)  # e.g. 001
        self.name = f"{base}-{suffix}"
        if not (self.model_code or "").strip():
            self.model_code = mcode

    def validate(self):
        """
        Optional but strongly recommended:
        keep identity stable after creation.
        """
        # Normalize model_code on every save (keeps data clean)
        if self.model_code:
            self.model_code = _norm(self.model_code)

        # Prevent identity drift after insert
        if not self.is_new():
            old = frappe.get_doc(self.doctype, self.name)

            if (old.brand or "") != (self.brand or ""):
                frappe.throw("Brand cannot be changed after creation (ID stability).")

            if (old.model_code or "") != (self.model_code or ""):
                frappe.throw("Model Code cannot be changed after creation (ID stability). Create a new Device Model.")
