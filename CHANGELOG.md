# Changelog

All notable changes to NambaTech will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-01-28 - Artemis

### Added

#### Device Management Module
- **Device Brand** - Master data for device manufacturers (Apple, Samsung, etc.)
  - Fields: brand_name, brand_code, is_active
  - Custom autoname logic with normalized brand codes (uppercase, hyphen-separated)
  - Collision-safe naming with automatic suffix generation

- **Device Model** - Device model registry linked to brands
  - Fields: brand (Link), model_name, model_code, category, release_year, is_active
  - Categories: Phones, TV, Console, Accessory, Laptop
  - Custom autoname: `{BRAND_CODE}-{MODEL_CODE}` format
  - Identity immutability enforcement after creation

- **Device Spec Profile** - SKU-level device specifications
  - Fields: device_model, storage_gb, ram_gb, color, network, region_lock, notes
  - Network options: 4G, 5G, WiFi-only, N/A
  - Region lock options: Unlocked, Carrier Locked, Unknown
  - Composite naming: `{MODEL}-{STORAGE}-{COLOR}-{NETWORK}-{REGION}`

#### Quality Assurance Module
- **QA Checklist Template** - Reusable inspection templates by category
  - Fields: template_name, category, is_active, checklist_items (child table)
  - Naming series: `QA-TPL-.#####`
  - Track changes enabled

- **QA Checklist Item** (Child Table) - Individual test definitions
  - Fields: test_code, test_name, test_type, is_required, weight
  - Test types: Pass/Fail, Numeric, Text
  - Editable grid enabled

- **QA Inspection** - Actual inspection records with results
  - Fields: serial_no, item_code, device_model, template, inspector, warehouse
  - Results: overall_result (PASS/REWORK/FAIL), grade (A/B/C/D)
  - Notes: cosmetic_notes, functional_notes
  - Naming series: `QI-.YYYY.-.#####`
  - Links to Serial No and Employee (inspector)

- **QA Inspection Result** (Child Table) - Individual test results
  - Fields: test_code, test_name, test_type, result_pass, result_value, result_text, notes
  - Editable grid for rapid data entry

#### Refurbishment Module
- **Refurb Intake** - Device intake tracking for refurbishment pipeline
  - Fields: intake_date, source_type, supplier/customer, intake_warehouse, item_code
  - Device identifiers: serial_no, imei_1, imei_2
  - Assessment: initial_cosmetic, purchase_cost, expected_sell_band
  - Source types: Supplier, Customer, Trade-in, Internal Return
  - Status workflow: RECEIVED, SERIAL CAPTURED, IN QA, READY, DEFECTIVE
  - Naming series: `RI-.MM.YY.DD.-`

- **Refurb Work Order** - Technician work tracking
  - Fields: serial_no, item_code, intake (Link), priority, assigned_technician
  - Work data: parts_stock_entry, labor_minutes, diagnosis, actions_taken
  - Priority levels: Low, Normal, High
  - Status workflow: OPEN, IN PROGRESS, DONE, CANCELED
  - Naming series: `RWO-.MM.YY.DD.-`

#### Warranty Module
- **Warranty Policy** - Configurable warranty terms
  - Fields: policy_name, category, warranty_days, return_window_days
  - Replacement rules: Repair First, Replace First
  - Documentation: coverage_notes, exclusions
  - Named by policy_name field

- **Warranty Swap** - Device replacement tracking
  - Fields: warranty_claim, customer, faulty_serial_no, replacement_serial_no
  - Logistics: outbound_delivery_note, inbound_stock_entry, swap_date
  - Status workflow: DRAFT, COMPLETED, CANCELED
  - Naming series: `WS-.MM.DD.YY.-`

#### Dispatch Module
- **Dispatch Ticket** - Order fulfillment and shipping tracking
  - Fields: sales_order, sales_invoice, delivery_note, customer, destination_town
  - Carrier data: carrier (Supplier), tracking_code, sla_deadline
  - Status workflow: READY, PICKED, IN_TRANSIT, DELIVERED, FAILED
  - Naming series: `DSP-.YY.DD.MM.-`

### Technical Notes
- All DocTypes include System Manager permissions by default
- Child tables (QA Checklist Item, QA Inspection Result) marked as `istable: 1`
- Track changes enabled on critical documents for audit trail
- Link fields properly configured with fetch_from for denormalized display
- Custom Python controllers with identity normalization and validation logic

---

## [1.0.0] - 2026-01-27 - Artemis

### Added
- Initial release of NambaTech e-commerce platform
- Frappe v15 custom app foundation
- Basic project structure and configuration
- Pre-commit hooks for code quality
- GitHub Actions CI/CD workflows
- MIT License

### Notes
- This is the first production release
- Release codename: **Artemis**

---

## Release Names

| Version | Codename | Date |
|---------|----------|------|
| 1.1.0 | Artemis | 2026-01-28 |
| 1.0.0 | Artemis | 2026-01-27 |
