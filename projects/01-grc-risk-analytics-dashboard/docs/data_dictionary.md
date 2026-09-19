# Asset Inventory Data Dictionary

## Purpose

This data dictionary defines the structure, meaning, permitted values,
and governance rules for the Northstar Financial Group asset inventory.

The asset inventory supports the identification and management of
information and other associated assets within the organisation's
Information Security Management System (ISMS).

The inventory is used as an input into cyber risk assessment,
control assessment, risk reporting, and security governance activities.

---

## Asset Inventory Fields

### asset_id

**Description:**  
Unique identifier assigned to each asset.

**Format:**  
AST-XXX

**Example:**  
AST-001

**Rules:**
- Mandatory
- Must be unique
- Must not be reused for another asset

---

### asset_name

**Description:**  
The recognised name of the asset, system, platform, or service.

**Examples:**
- Microsoft Entra ID
- Salesforce CRM
- Payroll Management System
- Microsoft Azure

**Rules:**
- Mandatory
- Should use a consistent business-recognised name

---

### asset_type

**Description:**  
Identifies the type or category of asset.

**Permitted values may include:**
- Business Application
- SaaS Application
- Cloud Platform
- Identity Platform
- Security Platform
- Development Platform
- Analytics Platform
- HR Information System
- Finance ERP
- Web Application
- Network Security
- Information Asset
- Database
- Infrastructure

**Example:**  
Identity Platform

---

### primary_business_function

**Description:**  
The business function primarily responsible for or dependent upon
the asset.

**Permitted values:**
- Technology
- Information Security
- Finance
- Human Resources
- Operations
- Customer Services
- Legal & Compliance
- Data & Analytics

**Example:**  
Human Resources

---

### supporting_business_function

**Description:**  
Other business function significantly dependent upon or supported
by the asset.

Assets may support more than one part of the organisation.

**Examples:**
- Finance
- Technology
- Information Security
- Enterprise-wide

**Example:**  
Finance

---

### business_process

**Description:**  
The business or technology process supported by the asset.

**Examples:**
- Payroll Processing
- Identity & Access Management
- Customer Relationship Management
- Vulnerability Management
- Financial Reporting
- Security Monitoring
- Software Development
- Network Operations

**Example:**  
Payroll Processing

---

### asset_description

**Description:**  
Short description explaining the purpose of the asset and how it
supports the organisation.

**Example:**  
System used to calculate and process employee salaries, deductions,
tax information, and payroll payments.

---

### asset_owner

**Description:**  
Business role accountable for ensuring that the asset is appropriately
managed and protected.

The asset owner represents accountability rather than day-to-day
technical administration.

**Examples:**
- HR Director
- Finance Director
- Head of Technology
- Head of Customer Services
- CISO

**Rules:**
- Mandatory
- Should normally contain a role rather than an individual's name

---

### technical_owner

**Description:**  
Role or team responsible for the technical administration,
maintenance, configuration, and operation of the asset.

**Examples:**
- IAM Lead
- Cloud Platform Lead
- M365 Service Owner
- Network Security Lead
- Enterprise Applications Manager

---

### information_processed

**Description:**  
Describes the primary information stored, processed, transmitted,
or otherwise handled by the asset.

**Examples:**
- Customer personal information
- Employee records
- Payroll and banking information
- Source code
- Security logs
- Financial transactions
- Authentication information

---

### data_classification

**Description:**  
Highest material information classification the asset is authorised
to store or process.

**Permitted values:**

#### Public
Information approved for public disclosure.

#### Internal
Information intended for internal organisational use.

#### Confidential
Sensitive business or personal information where unauthorised
disclosure could cause material harm.

#### Restricted
Highly sensitive information requiring the strongest level of
protection.

**Examples of Restricted information:**
- Privileged credentials
- Banking information
- Authentication secrets
- Highly sensitive personal information

---

### business_criticality

**Description:**  
Represents the importance of the asset to business operations and
the potential impact of significant disruption or loss.

**Permitted values:**

#### Low
Limited business impact if unavailable or compromised.

#### Medium
Noticeable operational impact, but alternative processes are
generally available.

#### High
Significant operational, financial, customer, or regulatory impact.

#### Critical
Severe impact to essential services, major business processes,
security operations, or regulatory obligations.

---

### confidentiality_requirement

**Description:**  
Required level of protection against unauthorised disclosure.

**Permitted values:**
- Low
- Medium
- High

---

### integrity_requirement

**Description:**  
Required level of protection against unauthorised or inappropriate
modification or destruction of information.

**Permitted values:**
- Low
- Medium
- High

---

### availability_requirement

**Description:**  
Required level of accessibility and operational availability of
the asset.

**Permitted values:**
- Low
- Medium
- High

---

## CIA Model

The confidentiality, integrity, and availability fields represent
the three core information security objectives.

### Confidentiality
Can unauthorised disclosure cause significant harm?

### Integrity
Would unauthorised modification or inaccurate information cause
significant harm?

### Availability
Would the organisation suffer significant impact if the asset
became unavailable?

These requirements contribute to understanding the security
importance of each asset.

---

### hosting_model

**Description:**  
Describes how the asset is hosted or delivered.

**Permitted values may include:**
- SaaS
- IaaS
- PaaS
- Cloud
- On-premises
- Hybrid
- Network Appliance
- Custom Application

**Example:**  
SaaS

---

### supplier

**Description:**  
External supplier or technology provider associated with the asset.

**Examples:**
- Microsoft
- Salesforce
- Cisco
- CyberArk
- Rapid7
- Atlassian

Where an internally developed service is used, this may be recorded
as Internal.

---

### location

**Description:**  
Primary geographic location or data-hosting region associated with
the asset.

**Examples:**
- Ireland
- EU
- EU / Global Service
- Global

This field may later support data residency, regulatory, and
third-party risk analysis.

---

### lifecycle_status

**Description:**  
Current lifecycle state of the asset.

**Permitted values:**
- Planned
- Active
- Retiring
- Decommissioned

---

### last_review_date

**Description:**  
Date on which the asset record was last formally reviewed.

**Format:**  
YYYY-MM-DD

**Example:**  
2026-09-01

---

### next_review_date

**Description:**  
Date by which the next formal asset review should be completed.

**Format:**  
MMMM D, YYYY

**Example:**  
September 6, 2026

Review frequency may be determined by asset criticality.

Example approach:

- Critical assets: every 6 months
- High assets: annually
- Medium assets: annually
- Low assets: annually or risk-based

---

## Data Quality Rules

The following rules apply to the asset inventory:

1. Every asset must have a unique asset ID.
2. Every active asset must have an asset owner.
3. Every active asset should have a technical owner.
4. Every asset must be associated with a primary business function.
5. Every asset must have a defined business process.
6. Every asset must have a business criticality rating.
7. Assets processing information must have a data classification.
8. CIA requirements must use the approved Low, Medium, or High values.
9. Lifecycle status must use an approved value.
10. Review dates must use the MMMM D, YYYY format (e.g September 6, 2026).
11. Critical assets should be reviewed more frequently than lower-criticality assets.
12. Decommissioned assets must remain identifiable for appropriate governance and historical traceability.

---

## Relationship to Risk Management

The asset inventory is one input into the enterprise cyber risk
management process.

Risks may be associated with one asset, multiple assets, or no
specific technology asset.

Risk sources may include:

- Asset assessments
- Internal audits
- External audits
- Penetration tests
- Vulnerability assessments
- Security incidents
- Regulatory requirements
- Third-party assessments
- Risk workshops
- RCSA activities
- Threat intelligence
- Control assessments
- Business or technology change

The asset inventory therefore supports risk identification but does
not define the entire scope of the risk register.
