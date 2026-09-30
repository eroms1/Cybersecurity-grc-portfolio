# GRC Data Architecture

## Purpose

This document describes the data architecture used by the Northstar
Financial Group GRC Risk Analytics project.

The architecture separates assets, risks, controls and control assessments
into related datasets rather than maintaining all GRC information within
a single risk register.

This approach supports data quality, control assurance, risk analysis,
automation and executive reporting.

---

## Architecture Overview

Business & Technology Environment
            |
            v
      Asset Inventory
       assets.csv
            |
            v
       Risk Register
    risk_register.csv
            |
            v
   Risk-Control Mapping
risk_control_mapping.csv
            |
            v
      Control Library
       controls.csv
            |
            v
    Control Assessments
control_assessments.csv
            |
            v
      Python Analytics
            |
            v
   Management Dashboard

---

## Data Sources

Risks may originate from multiple sources including:

- Asset assessments
- Internal audit
- External audit
- Penetration testing
- Vulnerability assessments
- Security incidents
- Third-party assessments
- Regulatory requirements
- Control assessments
- Risk workshops
- RCSA activities
- Threat intelligence
- Business and technology change
- Business continuity exercises

The asset inventory is therefore one source of risk information rather
than the sole driver of the risk register.

---

## Dataset Relationships

### Asset Inventory

`assets.csv` contains information about systems and other assets within
the organisation.

Primary key:

`asset_id`

Example:

AST-005 - Microsoft Azure

A risk may reference an asset where the risk relates to a specific asset.

---

### Risk Register

`risk_register.csv` contains identified information security and
technology risks.

Primary key:

`risk_id`

Foreign key:

`asset_id` (optional)

Not every risk is associated with a single asset. Risks originating from
regulatory requirements, governance weaknesses, third parties or
enterprise-wide processes may therefore have no asset_id.

---

### Control Library

`controls.csv` defines the security and governance controls implemented
by the organisation.

Primary key:

`control_id`

Controls can be mapped to ISO/IEC 27001:2022 Annex A controls to support
control assurance and compliance reporting.

---

### Risk-Control Mapping

`risk_control_mapping.csv` establishes the relationship between risks
and the controls intended to mitigate them.

A risk may depend on multiple controls.

A control may mitigate multiple risks.

This creates a many-to-many relationship between the risk register and
control library.

---

### Control Assessments

`control_assessments.csv` stores the results of control testing and
assurance activities.

Assessments may consider:

- Design effectiveness
- Operating effectiveness
- Evidence
- Findings
- Remediation actions
- Assessment dates

Control effectiveness is maintained separately from the risk register
so that control performance can be assessed and reported independently.

---

## Target Analytics

The architecture is designed to support reporting such as:

- High and critical residual risks
- Risk exposure by business function
- Risk exposure by category
- Risk identification source
- Overdue risk treatments
- Accepted risks approaching expiry
- Ineffective controls
- Design vs operating effectiveness
- Risks associated with ineffective controls
- High/critical risks dependent on weak controls
- ISO 27001 control coverage
- Assets associated with high residual risk
