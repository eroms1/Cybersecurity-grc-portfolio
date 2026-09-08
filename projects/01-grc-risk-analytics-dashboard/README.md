# GRC Risk Analytics & Executive Dashboard

## Project Overview 

This project demonstrates the design and engineering of an end-to-end cybersecurity Governance, Risk and Compliance (GRC) risk analytics solution for a fictional financial services organisation.

The project combines traditional enterprise cyber risk management with data analytics, Python automation, database technologies, REST APIs and Tableau to demonstrate how security risk information can be transformed into measurable, automated and management-focused intelligence.

Rather than treating a risk register as a static spreadsheet, the project develops a complete risk reporting architecture capable of:

- capturing cybersecurity risks;
- calculating inherent and residual risk;
- monitoring remediation activity;
- identifying overdue risks;
- measuring risk exposure;
- identifying risks requiring management decisions;
- generating GRC metrics;
- supporting executive reporting;
- and eventually exposing risk information through APIs and interactive dashboards.

The project is designed as a practical demonstration of how GRC processes can be engineered, automated and integrated with modern data technologies.

---

# Business Scenario

A fictional regulated financial services organisation operates a hybrid technology environment consisting of:

- Microsoft Azure;
- Microsoft 365;
- enterprise business applications;
- cloud-hosted infrastructure;
- third-party SaaS platforms;
- external technology suppliers;
- remote users;
- privileged administrator accounts;
- business-critical data;
- and externally accessible services.

The organisation operates across several business functions and maintains cybersecurity controls aligned with recognised information security frameworks.

Cybersecurity risks are identified through activities such as:

- vulnerability assessments;
- penetration testing;
- internal audit;
- cloud security assessments;
- risk and control self-assessments;
- security incidents;
- third-party assessments;
- architecture reviews;
- access reviews;
- regulatory assessments;
- and operational security monitoring.

Management requires a structured process for understanding the organisation's cyber risk exposure and determining which risks require remediation, acceptance, escalation or further investment.

---

# Business Problem

The organisation currently relies heavily on manually maintained risk information.

This creates several challenges:

- inconsistent risk scoring;
- limited visibility of risk exposure;
- difficulty identifying overdue remediation actions;
- manual preparation of management reports;
- limited historical trend analysis;
- fragmented risk ownership information;
- limited ability to identify risks above appetite;
- difficulty distinguishing inherent and residual risk;
- inconsistent treatment tracking;
- and limited automation between GRC data and executive reporting.

Senior management requires a more effective method for converting operational cyber risk information into actionable management intelligence.

---

# Project Objective

The objective of this project is to design a practical GRC analytics architecture capable of transforming raw cyber risk data into meaningful security metrics and executive reporting.

The completed solution will demonstrate how technologies such as Python, SQL, APIs and Tableau can support the automation and modernisation of cybersecurity governance and risk management.

---

# Core Project Objectives

The project aims to:

- Design an enterprise cybersecurity risk register.
- Develop a structured cyber risk data model.
- Define likelihood and impact scoring criteria.
- Calculate inherent and residual risk.
- Track risk treatments and remediation actions.
- Identify overdue cybersecurity risks.
- Measure risk ageing.
- Identify risks above risk appetite.
- Track accepted cybersecurity risks.
- Identify risks requiring management decisions.
- Calculate GRC key risk indicators and performance metrics.
- Automate cyber risk data processing using Python.
- Store structured risk information in a database.
- Expose selected risk information through a REST API.
- Develop an interactive Tableau executive dashboard.
- Produce CISO and senior-management-level cyber risk reporting.
- Document the complete technical and GRC architecture.

---

# Solution Architecture

The target solution architecture is:

```text
Cybersecurity Risk Sources
        |
        v
Fictional Cyber Risk Register
        |
        v
CSV / Excel Dataset
        |
        v
Python Data Processing
-------------------------------
- Data validation
- Data cleansing
- Risk calculations
- KPI calculations
- Risk ageing
- Overdue detection
- Appetite assessment
-------------------------------
        |
        v
SQLite / PostgreSQL
        |
        v
REST API
        |
        v
Tableau
        |
        v
Executive CISO Dashboard
        |
        v
Management Risk Decisions
```

The architecture demonstrates how traditional GRC information can move from manually maintained records towards a more automated data-driven security governance model.

---

# Technology Stack

## GRC & Security

- Enterprise Cyber Risk Management
- ISO/IEC 27001:2022
- ISO/IEC 27005
- NIST Cybersecurity Framework 2.0
- NIST SP 800-30
- DORA
- Security Assurance
- Risk Treatment
- Risk Acceptance
- Security Metrics
- Control Assessment

## Data & Automation

- Python
- Pandas
- CSV
- Excel
- JSON
- REST APIs

## Database

- SQLite
- PostgreSQL

## Data Visualisation

- Tableau

## Development & Version Control

- Git
- GitHub
- Visual Studio Code

---

# Project Architecture Components

## 1. Cyber Risk Dataset

The first component is a fictional enterprise cybersecurity risk dataset.

The dataset will simulate risks identified across different technology and security domains.

Example areas include:

- Identity and Access Management
- Cloud Security
- Vulnerability Management
- Network Security
- Data Protection
- Security Monitoring
- Incident Response
- Business Continuity
- Third-Party Risk
- Application Security
- Backup and Recovery
- Privileged Access
- Security Awareness
- Configuration Management

The dataset acts as the primary data source for the Python analytics engine and Tableau dashboard.

---

# Risk Register Data Model

The risk register will include fields such as:

| Field | Description |
|---|---|
| Risk ID | Unique identifier assigned to each risk |
| Risk Title | Short description of the risk |
| Risk Category | Security domain associated with the risk |
| Risk Statement | Structured description of the risk scenario |
| Threat | Threat capable of exploiting the weakness |
| Vulnerability | Weakness contributing to the risk |
| Asset / Service | Technology or service affected |
| Business Unit | Business area exposed to the risk |
| Risk Owner | Senior individual accountable for the risk |
| Action Owner | Individual responsible for remediation |
| Date Identified | Date the risk was identified |
| Likelihood | Probability of the risk occurring |
| Impact | Business consequence if the risk occurs |
| Inherent Risk Score | Risk before considering controls |
| Existing Controls | Current safeguards |
| Control Effectiveness | Assessment of existing controls |
| Residual Likelihood | Likelihood following existing controls |
| Residual Impact | Impact following existing controls |
| Residual Risk Score | Remaining risk after controls |
| Treatment Strategy | Mitigate, Accept, Transfer or Avoid |
| Treatment Action | Planned remediation activity |
| Target Date | Expected remediation date |
| Status | Current risk status |
| Risk Appetite Status | Whether the risk exceeds appetite |
| Management Decision | Decision required from management |
| Acceptance Expiry | Expiration date for accepted risk |
| Last Review Date | Most recent review |
| Comments | Additional context |

---

# Risk Statement Methodology

Risk statements will use a structured format.

Example:

> There is a risk that excessive privileged access could allow unauthorised administrative activity due to persistent privileged assignments, resulting in data compromise, system disruption or regulatory impact.

This structure helps distinguish:

```text
Threat
+
Vulnerability
+
Risk Event
+
Business Impact
```

Example:

```text
Compromised administrator
        +
Excessive permanent privileges
        ↓
Unauthorised administrative activity
        ↓
Data breach / system compromise
```

---

# Risk Scoring Methodology

A 5x5 risk scoring model will be used.

## Likelihood Scale

| Score | Rating | Description |
|---:|---|---|
| 1 | Rare | Highly unlikely to occur |
| 2 | Unlikely | Could occur but not expected |
| 3 | Possible | Could reasonably occur |
| 4 | Likely | Expected to occur in many circumstances |
| 5 | Almost Certain | Expected to occur frequently |

---

# Impact Scale

| Score | Rating | Description |
|---:|---|---|
| 1 | Insignificant | Minimal operational or business effect |
| 2 | Minor | Limited business disruption |
| 3 | Moderate | Noticeable financial, operational or compliance impact |
| 4 | Major | Significant disruption, financial loss or regulatory exposure |
| 5 | Severe | Critical business, regulatory, financial or reputational impact |

---

# Risk Calculation

The basic risk score is calculated using:

```text
Risk Score = Likelihood × Impact
```

For example:

```text
Likelihood = 4
Impact = 5

Risk Score = 4 × 5 = 20
```

---

# Risk Rating

Example risk classification:

| Score | Rating |
|---:|---|
| 1–4 | Low |
| 5–9 | Moderate |
| 10–14 | High |
| 15–25 | Critical |

The exact thresholds may be adjusted during the project as the risk methodology is refined.

---

# Inherent Risk

Inherent risk represents the level of risk before considering the effectiveness of existing controls.

Example:

```text
Likelihood = 5
Impact = 5

Inherent Risk = 25
```

---

# Residual Risk

Residual risk represents the remaining exposure after considering existing controls.

Example:

```text
Initial likelihood = 5
Initial impact = 5

Inherent Risk = 25

Following implementation of controls:

Residual likelihood = 3
Residual impact = 4

Residual Risk = 12
```

This allows management to understand the value provided by existing security controls.

---

# Risk Treatment

Each risk will be assigned one of four treatment approaches.

## Mitigate

Implement additional controls to reduce likelihood or impact.

## Accept

Formally acknowledge the risk and approve continued operation within defined conditions.

## Avoid

Remove the activity or technology creating the risk.

## Transfer

Transfer some of the financial or operational exposure to another party.

Examples may include:

- cyber insurance;
- managed service providers;
- contractual risk transfer;
- or outsourcing arrangements.

---

# Risk Acceptance

Accepted risks will include appropriate governance information such as:

- risk owner;
- acceptance authority;
- residual risk;
- business justification;
- acceptance date;
- expiry date;
- compensating controls;
- and scheduled review date.

Accepted risks should not automatically remain accepted indefinitely.

The project will therefore include monitoring of acceptance expiry dates.

---

# Risk Appetite

The solution will distinguish between risks that are:

```text
Within Appetite
Above Appetite
Accepted Above Appetite
Requiring Decision
```

Python will eventually automate the identification of risks exceeding defined thresholds.

Example logic:

```python
if residual_risk_score >= 15:
    appetite_status = "Above Appetite"
```

More sophisticated logic may later include different thresholds for different risk categories.

---

# Example Cybersecurity Risks

The fictional dataset may include scenarios relating to:

1. Excessive Azure privileged access
2. Missing privileged access reviews
3. Critical vulnerabilities exceeding remediation SLA
4. Internet-facing systems with unsupported software
5. Cloud security misconfiguration
6. Weak backup resilience
7. Ransomware exposure
8. DDoS resilience weaknesses
9. Third-party security weaknesses
10. Inadequate logging and monitoring
11. Phishing and credential compromise
12. Data leakage
13. Weak conditional access controls
14. Insecure service accounts
15. Delayed patching
16. Insufficient disaster recovery testing
17. Excessive OAuth application permissions
18. Missing MFA coverage
19. Incomplete vulnerability scanning
20. Weak joiner, mover and leaver controls

All scenarios will be fictional and designed specifically for portfolio purposes.

---

# Python Risk Analytics Engine

Python will be used to automate risk processing.

The Python layer will eventually perform functions including:

## Data Validation

Identify:

- missing values;
- invalid risk scores;
- duplicate risk IDs;
- missing owners;
- invalid dates;
- incomplete treatment information;
- and inconsistent classifications.

---

## Automated Risk Calculation

Python will calculate:

```text
Inherent Risk
Residual Risk
Risk Rating
```

Example:

```python
risk_score = likelihood * impact
```

---

# Overdue Risk Detection

Python will compare target remediation dates against the current date.

Example logic:

```python
if target_date < today and status != "Closed":
    overdue = True
```

This enables automatic identification of remediation activity requiring escalation.

---

# Risk Ageing

The solution will calculate how long each risk has remained open.

Example:

```text
Risk Age = Current Date - Date Identified
```

Ageing bands may include:

```text
0–30 days
31–60 days
61–90 days
91–180 days
180+ days
```

---

# KPI & KRI Calculation

Python will calculate management metrics such as:

- Total open risks
- Critical risks
- High risks
- Risks above appetite
- Accepted risks
- Overdue risks
- Risks requiring decision
- Risks closed during the reporting period
- Average risk age
- Average remediation time
- Risk treatment completion rate
- Percentage of risks with assigned owners
- Percentage of accepted risks approaching expiry

---

# Database Layer

As the project develops, risk data will move from CSV/Excel into a structured database.

Initial implementation:

```text
SQLite
```

Later implementation may use:

```text
PostgreSQL
```

Example database entities may include:

```text
Risks
Risk Owners
Risk Categories
Risk Treatments
Risk Reviews
Risk Acceptances
Controls
Business Units
```

This will demonstrate how GRC information can be stored using a structured relational data model.

---

# REST API

A later stage of the project will expose selected risk information through a REST API.

Example endpoint:

```text
GET /api/risks
```

Potential response:

```json
{
  "risk_id": "CR-001",
  "category": "Identity & Access Management",
  "residual_risk": 16,
  "rating": "Critical",
  "status": "Open"
}
```

Additional endpoints may include:

```text
GET /api/risks
GET /api/risks/{id}
GET /api/risks/critical
GET /api/risks/overdue
GET /api/metrics
GET /api/risk-categories
```

This component demonstrates how GRC information could be integrated with other enterprise systems.

---

# Tableau Executive Dashboard

The Tableau component will convert processed GRC data into executive-level security reporting.

The dashboard will be designed primarily for audiences such as:

- CISO
- CTO
- CIO
- Security Leadership
- Risk Committee
- Senior Management
- Internal Audit
- Enterprise Risk

---

# Dashboard Page 1 — Executive Cyber Risk Overview

Planned metrics include:

```text
Total Open Risks
Critical Risks
High Risks
Risks Above Appetite
Accepted Risks
Overdue Risks
Risks Requiring Decision
Risks Closed This Period
```

Visualisations may include:

- risk severity distribution;
- risk trend;
- open versus closed risks;
- risk exposure by category;
- and treatment status.

---

# Dashboard Page 2 — Risk Exposure

This page will analyse exposure across the organisation.

Potential views include:

- Risks by security domain
- Risks by business unit
- Risks by risk owner
- Risks by treatment type
- Risks by status
- Risks above appetite
- Inherent versus residual risk

---

# Dashboard Page 3 — Risk Treatment

This page will focus on remediation activity.

Metrics may include:

- Open treatments
- Completed treatments
- Overdue treatments
- Upcoming deadlines
- Average remediation age
- Treatment completion rate

---

# Dashboard Page 4 — Management Decisions

This page will identify risks requiring senior management attention.

Examples:

- Risk acceptance required
- Risks above appetite
- Expired risk acceptances
- Critical overdue risks
- Risks without remediation plans
- Risks requiring additional investment

The objective is to move executive reporting away from large spreadsheets towards decision-focused security information.

---

# Dashboard Page 5 — Risk Trends

This view will provide historical analysis.

Potential metrics:

- Total risk exposure over time
- Critical risk trend
- High-risk trend
- Risks opened versus closed
- Residual risk trend
- Risk treatment trend
- Risk ageing trend

---

# Project Phases

## Phase 1 — GRC Data Foundation

Deliverables:

- Cyber risk register
- Fictional risk dataset
- Data dictionary
- Risk scoring methodology
- Risk taxonomy
- Likelihood and impact matrix
- Example cyber risks

Status:

```text
IN PROGRESS
```

---

## Phase 2 — Python Risk Engine

Deliverables:

- Data import
- Data validation
- Risk calculations
- Residual risk calculations
- Risk classification
- Overdue detection
- Risk ageing
- Appetite assessment

---

## Phase 3 — GRC Metrics Engine

Deliverables:

- KPI calculations
- KRI calculations
- Management decision logic
- Risk exposure metrics
- Remediation metrics

---

## Phase 4 — Tableau Dashboard

Deliverables:

- Executive risk dashboard
- Risk exposure dashboard
- Treatment dashboard
- Management decision dashboard
- Risk trend dashboard

---

## Phase 5 — Reporting Automation

Deliverables:

- Automated data processing
- Automated metric generation
- Reporting datasets
- Scheduled processing workflow

---

## Phase 6 — Database

Deliverables:

- Risk database
- Relational data model
- SQL queries
- Database documentation

---

## Phase 7 — REST API

Deliverables:

- Risk API
- JSON responses
- Metrics endpoint
- Critical risk endpoint
- Overdue risk endpoint

---

## Phase 8 — Integration

Target architecture:

```text
Risk Data
   ↓
Python
   ↓
Database
   ↓
REST API
   ↓
Tableau
   ↓
CISO Dashboard
```

---

# Proposed Repository Structure

```text
01-grc-risk-analytics-dashboard/
│
├── README.md
│
├── data/
│   ├── risk_register.csv
│   ├── processed_risks.csv
│   └── data_dictionary.md
│
├── python/
│   ├── risk_engine.py
│   ├── data_validation.py
│   ├── kpi_calculator.py
│   └── risk_automation.py
│
├── database/
│   ├── schema.sql
│   └── queries.sql
│
├── api/
│   └── app.py
│
├── tableau/
│   └── screenshots/
│
├── docs/
│   ├── architecture.md
│   ├── methodology.md
│   ├── risk-scoring.md
│   └── lessons-learned.md
│
└── requirements.txt
```

The structure will evolve as the project develops.

---

# Framework Alignment

The project draws on concepts from recognised cybersecurity and risk management frameworks.

## ISO/IEC 27001:2022

Relevant areas include:

- risk assessment;
- risk treatment;
- information security controls;
- monitoring;
- measurement;
- management review;
- and continual improvement.

## ISO/IEC 27005

Provides guidance relating to information security risk management.

## NIST Cybersecurity Framework 2.0

The project will consider the six CSF functions:

```text
GOVERN
IDENTIFY
PROTECT
DETECT
RESPOND
RECOVER
```

## NIST SP 800-30

Provides concepts relating to information security risk assessment.

## DORA

The project will also consider ICT risk-management principles relevant to regulated financial organisations.

Areas of interest include:

- ICT risk management;
- ICT incident management;
- operational resilience;
- third-party technology risk;
- testing;
- monitoring;
- and governance.

---

# Skills Demonstrated

This project is intended to demonstrate practical capability across several areas.

## Governance, Risk & Compliance

- Enterprise cyber risk management
- Risk assessment
- Risk treatment
- Risk acceptance
- Risk appetite
- Risk reporting
- Security metrics
- Governance
- Management reporting

## Security Assurance

- Control assessment
- Control effectiveness
- Risk identification
- Security monitoring
- Risk remediation
- Evidence-based assurance

## Data Analytics

- Data modelling
- Data cleansing
- Data transformation
- KPI calculation
- Trend analysis
- Data visualisation

## Python

- Data processing
- Automation
- Pandas
- Functions
- Conditional logic
- Date processing
- Data validation

## APIs

- REST architecture
- JSON
- API endpoints
- Data integration

## Database

- SQL
- Relational data modelling
- SQLite
- PostgreSQL

## Visualisation

- Tableau
- Executive dashboards
- Management reporting
- Security metrics

## Development

- Git
- GitHub
- Version control
- Technical documentation

---

# Expected Final Outcome

The completed project should demonstrate an end-to-end GRC engineering workflow:

```text
Cyber Risk Identification
          ↓
Structured Risk Dataset
          ↓
Python Risk Processing
          ↓
Automated Risk Metrics
          ↓
SQL Database
          ↓
REST API
          ↓
Tableau Dashboard
          ↓
Executive Cyber Risk Reporting
          ↓
Management Decision Making
```

The goal is not simply to create a dashboard.

The goal is to demonstrate how a security professional can combine:

```text
GRC knowledge
+
Cybersecurity knowledge
+
Data analytics
+
Automation
+
Technical architecture
+
Executive communication
```

to create a scalable cyber risk reporting capability.

---

# Future Enhancements

Possible future extensions include:

- Azure security data integration
- Microsoft Defender data
- Vulnerability-management API integration
- Automated control evidence collection
- Power BI comparison
- Threat intelligence integration
- Cloud security posture metrics
- Third-party risk data
- Automated risk notifications
- Risk prediction
- AI-assisted risk classification
- Compliance-as-Code concepts
- Continuous control monitoring
- ISO 27001 control mapping
- NIST CSF mapping
- DORA mapping
- AI governance risk integration

---

# Lessons Learned

This section will be updated throughout the project.

Topics will include:

- challenges encountered;
- design decisions;
- data-quality problems;
- Python lessons;
- dashboard design decisions;
- GRC methodology improvements;
- API development lessons;
- and areas for future improvement.

---

# Project Status

🚧 **In Progress**

Current phase:

**Phase 1 — GRC Data Foundation**

Current focus:

- defining the risk data model;
- developing fictional cyber risk scenarios;
- creating the risk register;
- designing the scoring methodology;
- and preparing the dataset for Python analysis.

---

# Disclaimer

This project is an independent cybersecurity portfolio project created for educational, professional development and demonstration purposes.

All organisations, risks, systems, business units, incidents, vulnerabilities, findings, individuals and datasets used in this project are fictional or sanitised.

No confidential employer, client or customer information is included.

Any resemblance to real organisations, systems or security events is coincidental.

This project does not represent the security posture, risk position or internal processes of any current or previous employer.
