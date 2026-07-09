# Vendor Risk Management Policy

| Field | Value |
|---|---|
| Version | 2.0 |
| Effective Date | February 15, 2026 |
| Owner | VP Compliance |

## Purpose

Establishes requirements for identifying, assessing, managing, and monitoring cybersecurity and compliance risk introduced by third-party technology vendors and service providers engaged by NimbusHR Technologies.

## Vendor Tiering

| Tier | Definition | Assessment Frequency |
|---|---|---|
| **Tier 1 — Critical** | Access to Restricted-class data, or failure would significantly impair service delivery | Annual full assessment |
| **Tier 2 — High** | Access to Confidential data, or supports significant operational processes | Annual questionnaire-based assessment |
| **Tier 3 — Standard** | Limited data access, low operational dependency | Biennial self-assessment or upon material contract change |

## Contractual Requirements

All Tier 1 and Tier 2 vendors must: execute a Data Processing Agreement (DPA) or equivalent; meet minimum security standards (SOC 2 Type II or ISO 27001 preferred); provide evidence of annual penetration testing; maintain cyber liability insurance ≥ $5M; and include security incident notification requirements, data retention/destruction obligations, and compliance audit cooperation clauses in their contracts.

## Right-to-Audit

NimbusHR reserves the right to audit or commission an independent audit of any Tier 1 or Tier 2 vendor's security controls with 30 days' written notice. Vendors unwilling to consent are escalated to the CISO for contract renegotiation or termination consideration.

## Vendor Assessment Process

1. **Intake** — requesting team submits a vendor intake form to the GRC team
2. **Tier Assignment** — GRC assigns the vendor's risk tier based on data access and criticality
3. **Assessment** — GRC conducts the assessment via the [Vendor Assessment Questionnaire](Vendor-Assessment-Questionnaire.md), certification review, and/or on-site audit
4. **Risk Scoring** — vendor scored 0–100 on the [Vendor Risk Register](Vendor-Risk-Register.csv) scale (**Low 80–100 · Medium 60–79 · Medium-High 40–59 · High <40** — lower score reflects higher residual risk)
5. **Approval** — vendors scoring Medium-High or below require VP Compliance approval; High requires CISO approval
6. **Contracting** — Legal ensures the DPA, security requirements, right-to-audit clause, and incident-notification SLA are written into the contract
7. **Onboarding** — IT provisions access per least privilege; access is logged
8. **Ongoing Monitoring** — annual reassessment; continuous monitoring for Tier 1 vendors via SOC 2 report review

## Contractual Incident-Notification SLA (by Tier)

| Tier | Notification SLA |
|---|---|
| Tier 1 — Critical | 24 hours |
| Tier 2 — High | 48 hours |
| Tier 3 — Standard | 72 hours |

*Note: [ADP's contract currently specifies 72 hours despite being Tier 1](Vendor-Risk-Assessments.md#3-adp--payroll-integration-tier-1--critical) — this policy gap is tracked as finding ADP-F3 and is being renegotiated at the October 2026 contract renewal.*

## Vendor Offboarding

Upon contract termination, the vendor must return or certify destruction of all NimbusHR data within **30 days** and provide a data destruction certificate; IT confirms revocation of all system access via an access audit. GRC documents offboarding completion in the [Vendor Risk Register](Vendor-Risk-Register.csv).

## Escalation

Any vendor assessment resulting in a **Medium-High or above** risk rating is escalated to the VP of Compliance within 5 business days, with a remediation plan agreed with the vendor within 30 days. Failure to agree a plan triggers executive review and potential vendor contract action.
