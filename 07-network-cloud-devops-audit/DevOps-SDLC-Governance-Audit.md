# DevOps / SDLC Governance Audit — FY2026

Full finding tracker: [`Consolidated-Findings-Matrix.csv`](Consolidated-Findings-Matrix.csv)

## DEV-01 — 14 Repositories Contain Hardcoded Secrets — **CRITICAL**

GitHub Advanced Security secret scanning identified hardcoded secrets in **14 repositories** — AWS access keys, database connection strings with credentials, Twilio API keys, Stripe restricted keys, and GitHub Personal Access Tokens. Several have been present in repository history for **6+ months**.

**Root cause:** No pre-commit secret scanning hooks; no mandatory secret-detection gate in the CI/CD pipeline prior to this finding.

**Business Risk:** Hardcoded AWS keys give any party with repository read access — including the 22 stale external collaborators identified in the [GitHub vendor assessment](../05-vendor-risk-management/Vendor-Risk-Assessments.md) — persistent, unrestricted AWS access. This is the entry point exploited in the ["Operation Frozen Payroll" tabletop exercise](../08-incident-response-program/Tabletop-Exercise-Operation-Frozen-Payroll.md).

**Immediate Action:** All 14 identified credentials rotated without delay; pre-commit hooks (detect-secrets / GitLeaks) installed; GHAS secret scanning enabled as a required status check blocking merges with detected secrets; AWS Secrets Manager/Vault adopted for all secret storage; developer training scheduled within 30 days.

## DEV-02 — No Mandatory SAST/DAST in CI/CD Pipeline — High
No Static or Dynamic Application Security Testing is integrated into the pipeline — security review is ad hoc, and code can reach production without automated validation, a direct OWASP Top 10 exposure for the application processing 1.2M employee records (cross-ref [R-017](../02-risk-register/Enterprise-Risk-Register.csv)).
**Recommendation:** Integrate SAST (Semgrep/CodeQL) as a mandatory PR gate; implement DAST (OWASP ZAP) against staging before release; block deployment on Critical/High findings.

## DEV-03 — 6 Repositories Allow Direct Commits to Main Branch — High
6 of 22 production repos have no branch protection, permitting unreviewed deploys to production. One of the [5 unauthorized CloudTrail deployments (CM-02)](../04-itgc-audit/ITGC-Audit-Report.md) was traced to a direct main-branch commit in one of these repos.
**Recommendation:** Enforce branch protection org-wide; ≥1 PR approval required; required status checks (SAST scan, unit tests); automated alert if protection is disabled.

## DEV-04 — No Formal Threat Modeling for 3 Major FY2026 Features — Medium
Payroll API v3, Benefits Enrollment Portal v2, and the Talent Acquisition Module shipped with no formal threat modeling or defined security requirements.
**Recommendation:** Require STRIDE/PASTA threat modeling for all features touching Restricted/Confidential data; make it a required design-review gate; train Engineering Lead and senior engineers within 60 days.

## DEV-05 — 47 Open Dependency Alerts Aging 90+ Days — Low
GitHub Dependabot is enabled but has no remediation SLA; 47 alerts open 90+ days, including 9 rated High severity.
**Recommendation:** Define SLA — Critical 7 days, High 30 days, Medium 90 days; integrate into Jira security tracking; immediate triage of all 47 open alerts for active exploits.

## Executive Translation

Two of this audit's 15 findings (CLD-01, DEV-01) were treated as **emergencies requiring same-day action** — a publicly exposed payroll data bucket and 14 repositories with live production credentials. Both are now the leading examples in this program of *why* GRC audit cadence matters: neither was caught by a scheduled review, both were caught by automated scanning tooling deployed as part of this audit cycle, and both are the exact scenario dramatized in the [ransomware tabletop exercise](../08-incident-response-program/Tabletop-Exercise-Operation-Frozen-Payroll.md).
