# SOC 2 Type II Readiness Assessment — FY2026

Evaluates NimbusHR against all five AICPA Trust Services Criteria ahead of the Q4 2026 formal audit engagement. Full test-by-test data: [`SOC2-Readiness-Scorecard.csv`](SOC2-Readiness-Scorecard.csv)

## Readiness Score Summary

| TSC Category | Controls Tested | Passing | Partial | Failing | Readiness Score | Status |
|---|---|---|---|---|---|---|
| Security (CC) | 4 | 1 | 2 | 1 | **52%** | Needs Improvement |
| Availability (A) | 3 | 2 | 0 | 1 | **67%** | Needs Improvement |
| Confidentiality (C) | 2 | 0 | 1 | 1 | **25%** | **At Risk — Critical** |
| Processing Integrity (PI) | 1 | 1 | 0 | 0 | **100%** | Ready |
| Privacy (P) | 2 | 1 | 1 | 0 | **67%** | Needs Improvement |
| **Overall** | **12** | **5** | **4** | **3** | **62%** | **Remediation Required Before Audit** |

> **A minimum readiness score of 85% is recommended before scheduling the formal audit.** At 62%, NimbusHR is not yet ready. Two controls are **audit-disqualifying FAILs**: **A1.3** (no DR test in 18 months) and **C1.2** (no evidenced data disposal). Both are top H2 2026 priorities in the Annual Executive Risk Report.

## Key Test Results (Failing / Partial Controls)

| Control ID | Criteria | Result | Finding | Risk |
|---|---|---|---|---|
| **CC6.1** | Logical access protects against external threats | Pass w/ Exception | 14 terminated accounts active post-offboarding; service account MFA gap (IAM-01) | High |
| **CC6.2** | Access provisioning/authorization | Partial | RBAC not defined for 4 engineering sub-teams (IAM-04) | High |
| **CC9.2** | Vendor and business-partner risk management | Partial | ADP penetration test 22 months stale; 2 of 8 vendor reviews missed in prior year | High |
| **A1.2** | Backup/recovery infrastructure design | Pass | Multi-AZ redundancy + automated backups configured, but *not validated* | Low |
| **A1.3** | Recovery plan testing | **FAIL** | No DR test performed in **18 months**; no documented RTO/RPO validation — cross-ref [R-015](../02-risk-register/Enterprise-Risk-Register.csv) | **Critical** |
| **C1.1** | Confidential information protected through SDLC | Partial | Only 40% of Snowflake data fields tagged per classification scheme | Medium |
| **C1.2** | Confidential information disposed of when no longer needed | **FAIL** | No documented evidence of data disposal aligned to retention policy — no records of deletion/cryptographic erasure for any expired contract | **High** |
| **P6.7** | Mechanisms for data subject complaints/requests | Partial | DSR intake mechanism exists but internal response procedures/SLA tracking not formally documented | Medium |

## Passing Controls (For Context)

- **CC6.7** (data transmission protection) — TLS 1.2/1.3 enforced org-wide, TLS 1.0/1.1 disabled, A+ SSL Labs rating
- **A1.1** (capacity management) — AWS auto-scaling configured, quarterly capacity reviews documented
- **PI1.1** (processing integrity) — payroll reconciliation controls verified, automated validation rules in place
- **P4.1** (data collection limited to stated purpose) — privacy notices current, GDPR consent mechanisms in place for EU data subjects
