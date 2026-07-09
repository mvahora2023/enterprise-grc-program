# Cloud Security Audit (AWS) — FY2026

Full finding tracker: [`Consolidated-Findings-Matrix.csv`](Consolidated-Findings-Matrix.csv)

## CLD-01 — Public S3 Bucket Containing Historical Payroll Export Files — **CRITICAL — ACTIVE DATA EXPOSURE**

S3 bucket `nimbus-hr-exports-2024` has had **public read access enabled since November 2024** and contains **847 historical payroll export files** with employee names, salary figures, and partial SSN data — **currently accessible to anyone with the bucket URL.**

**Root cause:** Bucket was created by a developer for a temporary client export and never reviewed by Security; S3 Block Public Access was not enabled at the account level, allowing the bucket-level ACL to override the default.

**Business Risk:** This is an active data exposure event, not a theoretical gap. It is a **GDPR-reportable personal data breach** if EU employee data is included, triggers **CCPA notification obligations** for California residents, and could reach **$1.68M in GDPR penalties** alone, plus client notification obligations.

**Immediate Action Taken:** Public access disabled on the bucket; S3 Block Public Access confirmed enabled at the account level; full inventory of all S3 buckets for public access initiated; incident response procedures activated to assess exposure scope and regulatory notification obligations; preventive AWS Config rule deployed to block any public bucket configuration going forward.

*This finding drove [Risk R-005](../02-risk-register/Enterprise-Risk-Register.csv) and is one of the two Critical/emergency findings in this audit cycle (alongside DEV-01).*

## CLD-02 — AWS CloudTrail Not Enabled in `eu-west-1` — High
CloudTrail is configured for `us-east-1` but not the EU data-residency region — **all API activity involving EU personal data is unlogged**, directly impairing GDPR Article 5(1)(f)/Article 32 accountability and a SOC 2 CC7.2 gap.
**Recommendation:** Immediately enable CloudTrail in `eu-west-1` matching `us-east-1` configuration; AWS Config rule to detect any region without CloudTrail.

## CLD-03 — 4 IAM Users With Direct AdministratorAccess Policy — High
4 IAM users have `AdministratorAccess` attached directly (assigned during founding-team setup, never reviewed since). Combined with IAM-01 (service account MFA gap), a credential-compromise scenario is materially dangerous.
**Recommendation:** Remove direct admin policy from all users; role-based privilege via scoped IAM Roles; MFA-gated role assumption for admin operations; enable IAM Access Analyzer.

## CLD-04 — AWS Config Not Configured in 3 of 8 Accounts — Medium
Development, data engineering, and EU residency sub-accounts have no Config rules, so misconfigurations there go undetected.
**Recommendation:** Deploy AWS Config org-wide via delegated administrator; standard conformance pack covering S3, IAM, EC2, CloudTrail, VPC.

## CLD-05 — RDS Backup Retention 7 Days vs. 90-Day Policy — Medium
7-day retention is inadequate against a ransomware dwell time of 10–21 days, and is a compliance gap against the Data Retention Policy (indirectly against SOC 2 A1.2).
**Recommendation:** Increase to 90 days on all production instances; validate as part of the Q3 2026 DR test (see [R-015](../02-risk-register/Enterprise-Risk-Register.csv) and SOC 2 control A1.3).
