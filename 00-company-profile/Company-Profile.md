# NimbusHR Technologies — Company Profile

> **Fictional company used throughout this GRC program simulation.** All names, employees, vendors, and figures below are fictional and constructed solely to give every deliverable in this repository a single, internally consistent subject — the same way a real enterprise GRC program's risk register, audit findings, and executive dashboard all describe the same organization.

## Why a Fictional Company

A mid-size SaaS Human Resources platform touches the most sensitive data categories that exist in enterprise GRC work — PII, SSNs, banking/payroll data, and health benefits data — while also carrying SOC 2, GDPR, and CCPA obligations simultaneously. That combination makes it a realistic, rich subject for every module in this program: governance, risk, audit, vendor risk, IAM, cloud/DevOps security, and incident response all have real work to do here.

## Corporate Profile

| Attribute | Detail |
|---|---|
| Legal Name | NimbusHR Technologies, Inc. |
| Headquarters | Philadelphia, Pennsylvania, USA |
| Founded | 2018 |
| Business Model | SaaS — multi-tenant cloud HR platform (HR management, payroll, benefits administration, talent acquisition) |
| Client Count | 120 enterprise clients (North America & Europe) |
| End Users Served | 1.2 million employee end users |
| Annual Recurring Revenue (ARR) | $42,000,000 |
| Employee Count | 350 (80 Engineering · 40 HR Ops · 30 Finance · 200 Client-Facing / Other) |
| Cloud Infrastructure | AWS `us-east-1` (primary) · AWS `eu-west-1` (EU data residency) |
| Identity Provider | Azure Active Directory (employee identity) · Okta (SSO / MFA) |
| Code Repository | GitHub Enterprise |
| Data Warehouse | Snowflake |
| Key Integrations | ADP (payroll) · Stripe (payments) · Twilio (SMS/MFA) · PagerDuty (alerting) |
| Regulatory Obligations | SOC 2 Type II · GDPR · CCPA · NIST CSF (board-directed) |
| GRC Program Sponsor | Chief Information Security Officer (CISO) |
| GRC Program Owner | Vice President, Compliance and Risk |
| GRC Program Analyst | Mahmadarsh Vahora (author of this program) |

## Data Processing Environment

| Data Category | Examples | Regulatory Framework | Approx. Volume |
|---|---|---|---|
| Personally Identifiable Information (PII) | Full name, DOB, address, email, phone | GDPR, CCPA, state laws | 1.2M records |
| Social Security Numbers (SSNs) | Employee tax identification | CCPA, federal tax law | 890,000 records |
| Banking & Financial Data | Routing/account numbers for payroll | GLBA, PCI DSS-adjacent | 620,000 records |
| Health Benefits Data | Insurance elections, dependent info | HIPAA-adjacent, ERISA | 410,000 records |
| Payment Card Data | Client billing (processed via Stripe) | PCI DSS | Tokenized only |
| EU Personal Data | EU employee HR records, 18 enterprise clients | GDPR (DSGVO) | ~230,000 data subjects |

## GRC Governance Hierarchy

```
Board of Directors / Audit Committee   (oversight & direction)
        │
Chief Information Security Officer     (executive sponsorship, escalation authority)
        │
VP, Compliance and Risk                (program ownership, regulatory interface)
        │
GRC Analyst                            (operational execution — risk, audit, compliance, vendor risk)
        │
IT Manager / Engineering Lead / Legal Counsel   (control ownership & remediation)
```

## How This Repository Is Organized

This repository is a full-cycle FY2026 GRC program built around NimbusHR — governance documents, an 18-item enterprise risk register, a NIST CSF gap assessment, an ITGC audit, a four-vendor third-party risk program, an IAM + SOC 2 Type II readiness audit, a network/cloud/DevOps security audit, a full incident response program (including a ransomware tabletop exercise), an executive dashboard specification, and a 20-control control library mapped to NIST CSF, NIST 800-53, SOC 2 Trust Services Criteria, and CIS Controls v8. See the root [README.md](../README.md) for the full index.

Every finding, risk score, and control status in this repository is internally consistent — a risk identified in the register (`02-risk-register/`) reappears in the relevant audit finding, the IAM/SOC 2 assessment, the incident response tabletop, and the executive dashboard, exactly as it would in a real enterprise GRC program.
