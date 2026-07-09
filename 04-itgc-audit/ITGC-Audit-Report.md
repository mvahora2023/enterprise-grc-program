# IT General Controls (ITGC) Audit — FY2026

## Audit Scope

| Field | Detail |
|---|---|
| Audit Name | NimbusHR Technologies FY2026 ITGC Audit |
| Audit Period | Q1–Q2 2026 (Jan 1 – Jun 30, 2026) |
| Audit Lead | GRC Analyst |
| Audit Sponsor | VP, Compliance and Risk |
| Scope | All IT general controls supporting the financial reporting environment and HR data processing systems classified as in-scope for SOC 2 Type II — access control, change management, operations, backup/recovery |
| In-Scope Systems | Okta (SSO/MFA), AWS (EC2, RDS, S3, CloudTrail, IAM), GitHub Enterprise, Snowflake, PagerDuty, Jira (change tracking), NimbusHR production application |
| Methodology | Inquiry (control-owner interviews) · Observation (config review) · Inspection of Evidence (docs, logs, screenshots) · Re-Performance (GRC Analyst re-executed selected control procedures) |
| Materiality | High/Critical findings on SOC 2 in-scope systems require a Corrective Action Plan within 30 days of issuance |

**Objectives:** evaluate logical access control design and operating effectiveness; assess change management consistency for production changes; evaluate segregation of duties across financial/technical roles; assess audit log completeness and accessibility; determine remediation status of prior-year findings.

## Access Control Review

Population: 350 total Okta users. Sample: 40 standard accounts + 25 privileged accounts, systematic sampling. Evidence: Okta Admin Console reports, AWS IAM policy exports, ServiceNow deprovisioning tickets, HRIS termination records.

Full workpaper data: [`Access-Control-Review-Workpaper.csv`](Access-Control-Review-Workpaper.csv)

| Control Area | Population / Sample | Finding | Severity | Root Cause | Recommendation |
|---|---|---|---|---|---|
| User Deprovisioning | 47 terminations / all 47 | **14 terminated employees retained active Okta accounts 30+ days post-termination**; one account active 87 days post-termination | High | HR-to-IT ticket process has no automated trigger; deprovisioning relies on manual submission within 24 hrs of termination | Integrate HRIS (BambooHR) with Okta via SCIM; automate deprovisioning; implement daily HR/IT reconciliation report — *see [R-016](../02-risk-register/Enterprise-Risk-Register.csv)* |
| Privileged Access Review | 25 privileged accounts / 25 | **3 of 25 privileged users had access beyond their defined role** — all three retained elevated access from a completed project | High | Access granted ad hoc for project delivery; no formal recertification or role reassessment process | Implement quarterly PAM access recertification; require written re-approval for all elevated roles every 90 days — *see [R-004](../02-risk-register/Enterprise-Risk-Register.csv)* |
| MFA Enforcement — Service Accounts | 18 service accounts w/ production access / 18 | **MFA not enabled on 6 of 18 service accounts with direct production access** (AWS RDS, Snowflake, GitHub API) — Critical SOC 2 finding | **Critical** | Service accounts were explicitly excluded from MFA policy during initial Okta configuration; no documented risk acceptance exists | Enforce MFA or certificate-based authentication on all service accounts immediately, no exceptions without CISO-signed risk acceptance; implement machine identity management (CyberArk / AWS IAM Roles) — *see IAM-01 in [IAM Audit](../06-iam-soc2-assessment/IAM-Audit-Report.md)* |
| Dormant Account Detection | 350 active accounts / 40 | 8 of 40 accounts had no login activity in 90+ days; 3 belonged to contractors whose engagements ended with no offboarding ticket filed | Medium | No automated dormant-account detection process exists; reports require manual export/analysis | Implement automated dormant-account review via Okta Workflows/Lambda; auto-disable at 60 days inactive; require reactivation approval |
| Shared Account Usage | All 6 production RDS instances / 6 | One shared administrative account (`dbadmin_shared`) actively used by 3 engineers for production database access; individual privileged accounts had not been provisioned | High | Shared credentials established during initial database setup for convenience; individual provisioning process not followed | Immediately eliminate shared accounts; provision individual privileged DB accounts per engineer; implement session recording (AWS SSM Session Manager / CyberArk); rotate shared credentials immediately |

## Change Management Audit

60 production changes deployed during Q1–Q2 2026 reviewed via Jira change tickets, compared against AWS CloudTrail deployment logs. Full detail: [`Change-Management-Findings.csv`](Change-Management-Findings.csv)

| Finding | Control Area | Severity | Summary |
|---|---|---|---|
| **CM-01** | CAB Approval | High | 12 of 60 changes had no CAB approval documented prior to deployment (all self-classified "emergency"); 8 of these 12 did not meet the Change Management Policy's emergency criteria |
| **CM-02** | Unauthorized Changes | High | 5 production deployments identified in CloudTrail with **no corresponding Jira ticket** — no documented approval, testing evidence, or rollback plan |
| **CM-03** | Rollback Procedures | Medium | Rollback procedures were not documented for 48 of 60 changes reviewed (80%) |
| **CM-04** | Post-Implementation Review | Medium | No post-implementation review (PIR) was performed for any of the 15 major releases deployed in the period |

## Segregation of Duties Matrix

Full data: [`Segregation-of-Duties-Matrix.csv`](Segregation-of-Duties-Matrix.csv)

| User Role | Conflict | Risk Level | Resolution Required |
|---|---|---|---|
| DevOps Engineer | Can commit code AND approve own PRs / trigger production deploys | **Critical** | Yes — Immediate |
| Finance Analyst | Can create vendors AND approve payments to them | High | Yes — Within 60 days |
| IT Administrator | Can provision access AND modify/delete audit log entries | **Critical** | Yes — Immediate |
| Database Administrator | Can access production employee data AND disable DB audit logging | High | Yes — Within 90 days |
| HR Manager | Can create employee records AND approve payroll runs | Medium | Monitor — strengthen dual approval |
| Security Analyst | Can view all SIEM alerts AND modify alert rules/suppression logic | Low | Monitor — peer review is adequate |

## Corrective Action Plan (CAP) Tracker

Live tracker: [`Corrective-Action-Plan-Tracker.csv`](Corrective-Action-Plan-Tracker.csv) — 9 findings tracked to closure with owner, due date, and status. As of this report, **1 finding (AC-03 — service account MFA gap) is overdue** and has been escalated to the CISO.
