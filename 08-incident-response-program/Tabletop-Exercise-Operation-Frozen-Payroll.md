# Tabletop Exercise — "Operation Frozen Payroll"

| Field | Detail |
|---|---|
| Exercise Type | Tabletop (discussion-based) |
| Scenario | Ransomware attack with data exfiltration threat |
| Participants | CISO, VP Compliance, GRC Analyst, IT Manager, Engineering Lead, Legal Counsel, Finance Manager, VP Communications |
| Facilitator | GRC Analyst |

## Scenario

Monday, 9:41 AM — AWS GuardDuty flags anomalous beaconing traffic from a production EC2 instance. Simultaneously, engineers report being locked out of shared EFS directories that were accessible Friday. At 9:47 AM, a ransom note appears in shared directories: **$2.4M in Bitcoin within 72 hours**, or employee PII and payroll records for NimbusHR's enterprise clients get published to a dark-web forum.

Forensics traces the intrusion to a phishing email opened by a Finance employee **6 days prior**, which installed a backdoor. The attacker moved laterally and obtained Snowflake data-warehouse credentials via a **hardcoded secret in a GitHub repository** — the exact [DEV-01](../07-network-cloud-devops-audit/DevOps-SDLC-Governance-Audit.md) gap identified in this program's own DevOps audit — then exfiltrated historical payroll records for **78 of 120 enterprise clients** (~940,000 individuals' SSNs, salary, and banking data) before encrypting the data warehouse backups and multiple EFS directories.

## Exercise Injects and Gaps Identified

| # | Inject | Gap Identified |
|---|---|---|
| 1 | GuardDuty flags 4 anomalous EC2 instances; engineers report file-access issues | **EC2 isolation decision framework needed.** Isolation was delayed 22 minutes over uncertainty about which instances to isolate without disrupting client-facing services. Need a pre-defined runbook for emergency VPC isolation by service tier. |
| 2 | Forensics reveals the phishing email is 6 days old and evaded filtering | **Legal hold procedures were not invoked in the first 30 minutes.** The team correctly expanded investigation scope but took 45 minutes to request relevant logs, and Legal Counsel had to raise the legal-hold question rather than it being automatic. |
| 3 | A reporter contacts Communications for comment | **No pre-approved media holding statement existed.** The team correctly deferred to Communications/Legal, but had to draft the statement live rather than having one ready. |
| 4 | Exfiltrated data includes EU employee data for 12 EU-based clients | **No country-specific regulatory reference table.** Legal Counsel correctly identified the 72-hour GDPR clock, but the team was initially unclear whether UK ICO notification is required separately post-Brexit (it is, under UK GDPR). |
| 5 | CISO recommends paying the ransom; Legal Counsel objects | Team correctly escalated to CEO/Board and flagged OFAC risk, but **cyber insurance policy details (carrier, policy number, coverage limits) were not readily available** — Finance Manager had to ask, and no one knew the answer. |
| 6 | 36 hours in, enterprise clients are calling about missing payroll reports | **No pre-approved client communication template existed**, and VP Client Success — who should own client-facing incident communication — was not originally part of the IR team roster. |
| 7 | IT finds a clean-looking backup from 5 days ago | **The recovery runbook had no explicit step to validate backup date against confirmed infection date.** The team's first instinct was to restore immediately; the facilitator had to point out that a 5-day-old backup falls *within* the 6-day dwell period and could itself be compromised. |
| 8 | 72 hours post-incident — what should the PIR cover? | Team produced a strong PIR agenda, but the CISO requested a **quantified financial impact section** (revenue at risk, regulatory fine exposure, remediation cost, insurance claim documentation) that wasn't originally in the template. |

## Key Lessons Learned (Actioned)

1. Build an EC2/VPC emergency-isolation decision framework by service tier
2. Trigger legal hold procedures automatically within the first 30 minutes of any Critical incident declaration
3. Draft and pre-approve a media holding statement as a standing IRP artifact
4. Add a country-specific regulatory notification table (EU GDPR vs. UK GDPR) to the IRP
5. Embed cyber insurance carrier contact, policy number, and coverage summary directly in the IRP
6. Formally add VP Client Success to the Incident Response team roster
7. Add an explicit recovery-checklist step: *"Validate backup creation date against confirmed infection date before initiating restore"*
8. Add a quantified financial-impact section to the standard PIR template

This exercise is the clearest evidence in the entire program that a tabletop is worth running: **five of eight injects surfaced a real, previously undocumented process gap** — none of which would have been found by a document review alone.
