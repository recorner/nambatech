# Copyright (c) 2026, penvise and contributors
# For license information, please see license.txt

# import frappe
# apps/nambatech/nambatech/doctype/device_spec_profile/device_spec_profile.py

import re
import frappe
from frappe.model.document import Document
from frappe.model.naming import getseries

def _norm(value: str) -> str:
    """Uppercase, safe token (A-Z0-9 + hyphen)."""
    value = (value or "").strip().upper()
    value = re.sub(r"[^A-Z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value

def _gb(value) -> str:
    """Format integer GB fields consistently."""
    if value is None or value == "":
        return ""
    try:
        v = int(value)
    except Exception:
        return ""
    return f"{v}GB"

class DeviceSpecProfile(Document):
    def autoname(self):
        """
        Naming format:
        {DEVICE_MODEL_NAME}-{STORAGE}{-COLOR}{-NETWORK}{-REGION_LOCK}

        Example:
        APPLE-IP13-128GB-BLUE-5G-UNLOCKED
        """

        if not self.device_model:
            frappe.throw("Device Model is required to generate Device Spec Profile ID.")

        # Device Model name is already a stable code like APPLE-IP13
        base = _norm(self.device_model)

        parts = []

        storage = _gb(self.storage_gb)
        if storage:
            parts.append(storage)

        # Optional: RAM if you care for laptops/Android
        ram = _gb(self.ram_gb)
        if ram:
            parts.append(f"RAM-{ram}")

        color = _norm(self.color)
        if color:
            parts.append(color)

        network = _norm(self.network)
        if network and network != "N-A":
            # Handle "N/A" normalization edge
            parts.append(network)

        region_lock = _norm(self.region_lock)
        if region_lock and region_lock != "UNKNOWN":
            parts.append(region_lock)

        # If no spec parts, keep it minimal but still valid
        candidate = base if not parts else f"{base}-" + "-".join(parts)

        # Try direct name if available
        if not frappe.db.exists(self.doctype, candidate):
            self.name = candidate
            return

        # Collision-safe suffix
        suffix = getseries(f"{candidate}-", 3)  # e.g. 001
        self.name = f"{candidate}-{suffix}"

    def validate(self):
        """
        Optional hardening:
        - Normalize fields consistently.
        - Prevent changing identity fields after creation (keeps references stable).
        """
        # Normalize user input
        if self.color:
            self.color = self.color.strip()
        if self.network:
            self.network = self.network.strip()
        if self.region_lock:
            self.region_lock = self.region_lock.strip()

        # Identity immutability (recommended)
        if not self.is_new():
            old = frappe.get_doc(self.doctype, self.name)

            identity_fields = ["device_model", "storage_gb", "ram_gb", "color", "network", "region_lock"]
            for f in identity_fields:
                if (old.get(f) or "") != (self.get(f) or ""):
                    frappe.throw(
                        f"{f.replace('_',' ').title()} cannot be changed after creation (ID stability). "
                        "Create a new Spec Profile instead."
                    )
