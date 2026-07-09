# Identity & Access Management (IAM) Audit — FY2026

Conducted in Q2 2026 across NimbusHR's identity infrastructure — Okta (primary, governs authentication for all 350 employees and third-party integration access via SAML/OIDC), AWS IAM (infrastructure access), and GitHub (repository governance). Seven findings identified, ranging Critical to Low, all communicated to the IT Manager and VP of Compliance. Full data: [`IAM-Findings.csv`](IAM-Findings.csv)

## IAM-01 — Service Account MFA Gap — **CRITICAL**

**Systems Affected:** 6 service accounts with production access to AWS RDS, Snowflake, and GitHub API.
**Evidence:** Okta admin export — 6 accounts flagged "No factors enrolled," all confirmed with active production access via AWS IAM role mapping.
**Business Risk:** Service accounts without MFA are a high-value credential-compromise target. A compromised service account with production database access could enable mass exfiltration of employee PII, SSNs, and payroll data for 1.2M individuals. This is a critical **SOC 2 CC6.1** control failure.
**Management Response:** *"We acknowledge the finding and have initiated emergency remediation. A service-account inventory is complete by July 20; AWS IAM Role conversion is the target solution for 4 of 6 accounts; the remaining 2 require machine identity management pending vendor evaluation."*
**Target Remediation:** August 15, 2026 (extended from July 31)

## IAM-02 — Privileged Access Review Not Performed in 14 Months — High

**Evidence:** Last documented privileged access review: January 2025. No evidence of Q2–Q4 2025 or Q1 2026 review activity; SOC 2 evidence request returned no documentation for the period.
**Business Risk:** Failure to perform quarterly access reviews drives the privilege-creep accumulation described in [R-004](../02-risk-register/Enterprise-Risk-Register.csv), increases insider threat risk, and is a direct SOC 2 CC6.1 failure.
**Management Response:** Manual privileged access review underway in July 2026; Okta Access Certifications evaluated as a tooling solution; first automated quarterly review committed for October 1, 2026.
**Target Remediation:** October 1, 2026

## IAM-03 — 81 of 350 Users (23%) Have Not Enrolled in MFA — High

**Evidence:** Okta MFA enrollment report (June 15, 2026) — 81 accounts unenrolled: 42 client-facing employees, 21 HR operations, 18 general business users.
**Business Risk:** Unenrolled users are vulnerable to phishing, password spraying, and credential stuffing — a direct Information Security Policy and SOC 2 CC6.1 violation.
**Management Response:** Enrollment campaign launched July 1 with daily reminders; enforcement blocking activates July 21; enrollment improved from 77% → 89% as of July 9; 100% expected by July 31.
**Target Remediation:** July 31, 2026

## IAM-04 — RBAC Not Formally Defined for 4 Engineering Sub-Teams — High

**Evidence:** Platform, Data Engineering, DevOps, and Mobile sub-teams have no documented RBAC matrix — access is granted ad hoc based on manager requests. 14 instances of ad hoc access grants identified with no corresponding role justification.
**Business Risk:** Without formal RBAC, access creep is uncontrolled, least privilege cannot be enforced, and SOC 2 access recertification cannot be performed meaningfully.
**Management Response:** Engineering Lead and IT Manager to jointly define RBAC roles by September 1; Okta Groups restructured and access certified against new roles by October 1.
**Target Remediation:** October 1, 2026

## IAM-05 — Password Reset Bypasses MFA for 12 Legacy Accounts — Medium

**Evidence:** Self-service reset flow for 12 legacy application accounts (not managed via Okta SSO) allows password reset via email link only — bypassing MFA entirely.
**Business Risk:** An attacker who compromises a user's email can reset the application password without MFA validation, rendering MFA protection moot for these accounts.
**Management Response:** Migration plan initiated — 6 accounts migrated to Okta SSO by August 30, remaining 6 by October 31; self-service reset disabled as an interim measure.
**Target Remediation:** October 31, 2026

## IAM-06 — No Alert for Excessive Privileged System Accumulation — Medium

**Evidence:** 7 users hold access to 4+ privileged systems (AWS Console, Snowflake admin, GitHub admin, RDS admin) with no automated alert or approval workflow triggered.
**Business Risk:** Accumulation of privileged access across systems significantly amplifies the impact of a compromised account.
**Management Response:** Okta Workflow to trigger an alert to IT Manager/VP Compliance when a user is provisioned to a 3rd privileged system group, by September 15.
**Target Remediation:** September 15, 2026

## IAM-07 — MFA Session Token Lifetime Exceeds Industry Recommendation — Low

**Evidence:** Standard-user Okta session lifetime is configured at 24 hours vs. the NIST SP 800-63B / CIS Controls v8 recommendation of 8-hour re-authentication.
**Business Risk:** Extended session tokens increase the window for session-hijacking attacks.
**Management Response:** 8-hour session policy pilot in Q3 2026; full rollout decision by November 1.
**Target Remediation:** November 1, 2026
