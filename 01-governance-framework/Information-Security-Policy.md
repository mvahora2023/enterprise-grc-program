# Information Security Policy

| Field | Value |
|---|---|
| Policy Title | Information Security Policy |
| Version | 3.2 |
| Effective Date | January 1, 2026 |
| Next Review | January 1, 2027 |
| Approved By | CISO & VP Compliance |

## 1. Purpose

This Policy establishes the principles, requirements, and responsibilities governing the protection of information assets owned, processed, or managed by NimbusHR Technologies, Inc. It protects the confidentiality, integrity, and availability of NimbusHR's information assets — and those of its clients, employees, and business partners — from unauthorized access, disclosure, modification, destruction, or disruption.

## 2. Scope

Applies to all employees, contractors, consultants, temporary workers, and third parties with access to NimbusHR's information systems, networks, applications, or data — regardless of format, location, or medium. Compliance is a condition of continued employment or engagement.

## 3. Data Classification

| Level | Definition | Examples | Handling Requirements |
|---|---|---|---|
| **Public** | Approved for unrestricted public disclosure | Press releases, job postings, marketing site content | No special handling; standard quality review before publication |
| **Internal** | For internal use; not approved for public distribution | Meeting notes, employee directories, operational procedures | Not shared externally without authorization; standard access controls |
| **Confidential** | Sensitive business or client information | Client contracts, financial reports, audit findings, vendor assessments, source code, HR records | Encrypted in transit and at rest; access logged; need-to-know basis; NDA required for external sharing |
| **Restricted** | Highest sensitivity; unauthorized access causes severe harm | Employee SSNs, banking credentials, health data, auth secrets, encryption keys, production credentials | AES-256 encryption required; MFA mandatory; strict access controls and logging; data minimization enforced |

## 4. Acceptable Use

Company systems may only be used for authorized business purposes. All activity is subject to monitoring and logging (email, network, endpoint, application access), and users have no expectation of privacy while using Company resources.

## 5. Password Standards

- Minimum length: **14 characters** (standard accounts) / **20 characters** (privileged accounts)
- Must include uppercase, lowercase, numeral, and special character
- Privileged account passwords rotated every **90 days**; standard accounts rotated annually or immediately upon suspected compromise
- No reuse of the previous **12** password generations
- **MFA is mandatory** for all accounts accessing Restricted data, all administrative accounts, all remote access, and all production system access
- Secrets stored only in approved secrets management tooling (AWS Secrets Manager, HashiCorp Vault) — never hardcoded

## 6. Data Retention

- PII and client data retained **7 years** post-contract termination unless a longer period is required by law
- Backups: 90-day minimum retention, daily incremental + weekly full for Tier 1 systems
- Audit/security logs: 12 months operational storage + 24 months cold/archive storage
- Expired data securely destroyed via cryptographic erasure (cloud) or NIST 800-88 wiping (physical media)

## 7. Enforcement

Violations may result in disciplinary action up to and including termination, and criminal conduct is referred to law enforcement. Suspected violations are reported to `security@nimbushr.com` or the anonymous ethics hotline.
