# Vendor Risk Assessments — Detailed (Tier 1 Vendors + GitHub)

Summary of all 8 assessed vendors: [`Vendor-Risk-Register.csv`](Vendor-Risk-Register.csv)

---

## 1. Okta — Identity Provider (Tier 1 — Critical)

| Field | Detail |
|---|---|
| Service Provided | SSO, MFA, Directory Services, Lifecycle Management |
| Data Accessed | All employee credentials, auth tokens, session data for all 350 employees + client-facing portal sessions |
| Assessment Date | March 10, 2026 |
| Method | SOC 2 Type II report review (FY2025), security questionnaire, DPA review, SLA review |
| Security Posture | **Excellent** — SOC 2 Type II with no exceptions; FedRAMP authorized; ISO 27001 certified |
| Findings | Minor — Okta's default audit log retention is 90 days, shorter than NimbusHR's contractual 12-month requirement; no contractual SLA amendment currently in place |
| **Risk Rating** | **Low — Score: 18/100** |
| Recommendation | Request contractual SLA amendment for 12-month audit log retention at next annual contract review (September 2026) |
| Next Review | March 2027 |

## 2. Stripe — Payment Processing (Tier 1 — Critical)

| Field | Detail |
|---|---|
| Service Provided | Payment card processing for client billing and subscription management |
| Data Accessed | Tokenized payment/billing data only (raw PANs never stored by NimbusHR) |
| Assessment Date | April 5, 2026 |
| Method | PCI DSS Attestation of Compliance review, SOC 1 Type II review, security questionnaire, DPA review |
| Security Posture | **Strong** — PCI DSS Level 1 Service Provider certified; SOC 1 Type II with no exceptions; SOC 2 Type II available |
| Findings | None material — all certifications current, no exceptions noted |
| **Risk Rating** | **Low — Score: 22/100** |
| Recommendation | Continue annual review; confirm GDPR DPA reflects current service scope; confirm Stripe's sub-processor list is reviewed annually |
| Next Review | April 2027 |

## 3. ADP — Payroll Integration (Tier 1 — Critical)

| Field | Detail |
|---|---|
| Service Provided | Payroll data exchange API for NimbusHR's client payroll processing |
| Data Accessed | Employee SSNs, salary data, banking routing/account numbers, tax IDs, employment records for **all 120 enterprise clients** |
| Assessment Date | March 22, 2026 |
| Method | Security questionnaire, contract/DPA review, SOC 1 Type II review, penetration testing evidence review |
| Security Posture | **Moderate** — material gaps identified requiring follow-up |

**Findings (Medium-High Risk Vendor):**

| Finding | Severity | Description | Status |
|---|---|---|---|
| ADP-F1 | High | Most recent penetration test performed **22 months ago** (May 2024) — exceeds NimbusHR's annual pen-test policy requirement for Tier 1 vendors | Open — awaiting ADP response |
| ADP-F2 | Medium | Data retention practices for offboarded client data are not contractually defined — no specified retention period or secure deletion obligation | Open — contract renewal Oct 2026 |
| ADP-F3 | Medium | Contractual incident-notification SLA is **72 hours**, versus NimbusHR's required 24-hour SLA for Tier 1 vendors — a 48-hour gap that could impair NimbusHR's own GDPR notification obligations | Open — renegotiation in progress |

| | |
|---|---|
| **Risk Rating** | **Medium-High — Score: 58/100** |
| Recommendation | Require updated penetration test results within 60 days; renegotiate incident notification SLA to 24 hours; add data retention/destruction clause at October 2026 renewal; escalate to VP Compliance per policy |
| Residual Risk | Medium — compensating controls via API request monitoring, payload data minimization, API rate limiting |
| Next Review | September 2026 (interim) / March 2027 (full annual) |

*Cross-reference: [R-003](../02-risk-register/Enterprise-Risk-Register.csv) in the Enterprise Risk Register.*

## 4. GitHub — Code Repository (Tier 2 — High)

| Field | Detail |
|---|---|
| Service Provided | Source code management, CI/CD (GitHub Actions), IaC repository, secret scanning |
| Data Accessed | Proprietary source code, IaC configs, CI/CD scripts, deployment secrets (potentially exposed) |
| Assessment Date | February 18, 2026 |
| Method | Security questionnaire, GitHub Advanced Security scan review, internal repository governance audit, branch protection review, collaborator access review |
| Security Posture | **Moderate** — GitHub's platform security is strong; the findings below are internal NimbusHR governance gaps, not platform deficiencies |

**Findings (CRITICAL finding required immediate action):**

| Finding | Severity | Description | Immediate Action |
|---|---|---|---|
| GH-F1 | **Critical** | GitHub Advanced Security secret scanning identified **14 repositories containing hardcoded secrets** — AWS access keys, DB credentials, Twilio/Stripe API keys, GitHub PATs. Several present in history for 6+ months | Rotate ALL exposed secrets immediately; invalidate identified keys; implement pre-commit secret scanning hooks; enable GHAS on all repos |
| GH-F2 | High | 6 of 22 production repos had **no branch protection rules**, permitting direct commits to `main` without PR or peer review | Enforce branch protection org-wide; require ≥1 PR approval; enable required status checks |
| GH-F3 | Medium | 22 external collaborators retained active access to private repos despite associated projects concluding 3–18 months ago | Revoke all stale collaborator access within 14 days; implement quarterly external collaborator reviews |

| | |
|---|---|
| **Risk Rating** | **Medium — Score: 44/100** |
| Recommendation | Immediately rotate exposed secrets (GH-F1 treated as an emergency action); enforce branch protection; revoke stale collaborator access; implement pre-commit secret scanning; establish a formal GitHub governance policy |
| Residual Risk | Medium-Low following completion of secret rotation and branch protection enforcement |
| Next Review | August 2026 (interim for GH-F1 validation) / February 2027 (full annual) |

*Cross-reference: [DEV-01](../07-network-cloud-devops-audit/Consolidated-Findings-Matrix.csv) in the DevOps/SDLC audit and the [ransomware tabletop exercise](../08-incident-response-program/Tabletop-Exercise-Operation-Frozen-Payroll.md), where this exact secret-exposure gap is the exploited entry point.*
