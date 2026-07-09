# Enterprise Risk Register — FY2026

Full data file: [`Enterprise-Risk-Register.csv`](Enterprise-Risk-Register.csv) (18 risks, open directly in Excel/Sheets)

## Methodology

Each risk is scored on a **5×5 likelihood-impact matrix** (Likelihood 1–5 × Impact 1–5), producing an **Inherent Risk Score** (pre-control, 1–25) and a **Residual Risk Score** (post-control, after applying current control effectiveness). Risk owners execute treatment plans against defined due dates. The register is reviewed quarterly by the VP of Compliance and presented to the CISO monthly, consistent with the [Risk Appetite Statement](../01-governance-framework/Risk-Appetite-Statement.md) thresholds (residual ≥ 12 requires quarterly CISO review; inherent ≥ 20 requires 30-day remediation-plan approval).

## Risk Heat Map (Residual Risk, Likelihood × Impact)

|            | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|---|---|---|---|---|---|
| **Likelihood 5** | | | | | 🔴 R-001 (inherent) |
| **Likelihood 4** | | | | 🟠 R-004, R-007, R-016, R-017 (inherent) | |
| **Likelihood 3** | | | 🟡 R-014 (inherent) | | 🟠 R-002, R-003, R-005, R-008, R-015, R-018 (inherent) |
| **Likelihood 2** | | | | 🟡 R-011, R-013 (inherent) | 🟠 R-006, R-010, R-012 (inherent) |
| **Likelihood 1** | | | | | |

🔴 Critical (20–25) · 🟠 High (12–19) · 🟡 Medium (6–11) · 🟢 Low (1–5) — plotted at **inherent** score; see CSV for residual scores per risk.

## FY2026 Summary Metrics

| Metric | Value |
|---|---|
| Total risks identified | 18 |
| High/Critical residual risks (≥ 12) | 9 — R-001, R-003, R-004*, R-007*, R-015, R-016, R-018 (*borderline, tracked closely) |
| Medium residual risks (6–11) | 7 |
| Low residual risks (1–5) | 2 (R-011, R-013 — formally accepted) |
| Risks formally accepted | 2 (R-011, R-013) |
| Overdue remediations | 1 — **R-015 (Critical)**, past its July 31, 2026 due date |
| Average residual risk score | 8.2 / 25 |
| Risks requiring CISO escalation (residual ≥ 12) | 7 |
| Risk domains with ≥ 3 active risks | Access Control (3), Third-Party Risk (2), Cloud Security (2) |

## Top 5 Risks — Treatment Plans

### R-001 — Unauthorized Access via Compromised Credentials (Residual: 12)
**Treatment:** Enforce MFA on all remaining legacy API endpoints; remediate the IAM-01 service-account MFA gap (see [IAM Audit](../06-iam-soc2-assessment/IAM-Audit-Report.md)); complete by **2026-09-30**. This is the single highest-priority item on the register — a compromised credential with legacy API access is a direct path to the 1.2M-record employee dataset.

### R-003 — Third-Party Data Breach via ADP Integration (Residual: 12)
**Treatment:** Require an updated penetration test from ADP within 60 days; renegotiate the incident-notification SLA to 24 hours (currently 72); add data retention/destruction clauses at the October 2026 contract renewal. See [Vendor Risk Register](../05-vendor-risk-management/Vendor-Risk-Register.csv).

### R-015 — Backup Failure / Inadequate Recovery (Residual: 12) — **CRITICAL, OVERDUE**
**Treatment:** Execute a full DR/BCP restoration test from AWS backup for all Tier 1 systems, validating RTO ≤ 4 hours / RPO ≤ 1 hour, by **September 30, 2026**. This is the single most operationally dangerous open item in the program — NimbusHR cannot currently prove it can recover from a ransomware event within its own client SLA commitments.

### R-016 — Orphaned User Accounts (Residual: 12)
**Treatment:** Implement automated HRIS-to-Okta deprovisioning via SCIM to eliminate the manual offboarding gap that left 14 terminated employees with active accounts (one for 87 days). Target: **October 1, 2026**.

### R-018 — SOC 2 Type II Audit Unpreparedness (Residual: 12)
**Treatment:** Establish continuous, automated evidence collection from Okta, AWS Config, CloudTrail, and GitHub by August 31, 2026 — the current episodic, point-in-time evidence-gathering approach is insufficient for a Type II engagement. Directly protects **$16.8M in ARR** (40% of enterprise client base requires SOC 2 as a contract condition).

## Cross-References

Every risk in this register reappears elsewhere in the program: R-001/R-004/R-016 in the [ITGC audit](../04-itgc-audit/ITGC-Audit-Report.md), R-003 in [vendor risk](../05-vendor-risk-management/Vendor-Risk-Register.csv), R-015 in the [incident response tabletop](../08-incident-response-program/Tabletop-Exercise-Operation-Frozen-Payroll.md), and all nine highest-residual risks in the Annual Executive Risk Report.
