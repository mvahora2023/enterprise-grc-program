# Incident Response Plan (IRP)

Owned by the CISO; operationally executed by the GRC Analyst and Security Lead. Reviewed and tested annually via tabletop exercise (see [`Tabletop-Exercise-Operation-Frozen-Payroll.md`](Tabletop-Exercise-Operation-Frozen-Payroll.md)) and updated after any material incident.

## Purpose and Scope

Establishes procedures, roles, and communication protocols NimbusHR executes for any confirmed or suspected cybersecurity incident affecting the confidentiality, integrity, or availability of its systems, data, or services (including those operated on behalf of enterprise clients). Applies to all employees, contractors, vendors, and managed service providers.

## Incident Severity Classification Matrix

| Severity | Definition | Example | Initial Response SLA | Escalation | Executive Notification |
|---|---|---|---|---|---|
| **CRITICAL (P1)** | Imminent/confirmed breach of Restricted data; active ransomware; complete system unavailability; regulatory breach trigger | Active ransomware encryption; confirmed SSN/banking exfiltration; public exposure of Restricted data; Okta/AWS account compromise | **15 min** — on-call Security Lead acknowledges; IRP invoked within 30 min | CISO immediate; CEO within 1 hr; Board within 4 hrs | CISO, CEO, Legal, PR within 1 hr; external counsel + cyber insurer within 2 hrs |
| **HIGH (P2)** | Potential breach under investigation; significant system impairment; credible targeted threat | GuardDuty high-severity finding; suspected phishing compromise; large-scale unauthorized access attempt | **1 hr** — Security Lead + IT Manager engaged | CISO within 2 hrs; VP Compliance within 2 hrs | CISO + VP Compliance within 2 hrs; CEO if it escalates |
| **MEDIUM (P3)** | Isolated policy violation; single-system anomaly | Phishing email received (not clicked); failed patch deployment; low-confidence alert | **4 hrs** — GRC Analyst + IT investigate during business hours | IT Manager within 4 hrs; CISO if escalation threshold met | CISO notified only if it escalates |
| **LOW (P4)** | Minor violation; no evidence of data impact | Phishing blocked by filter; password reuse on non-corporate site | **24 hrs** — tracked in incident log | None — document and track | Reported in monthly security metrics |

## Incident Response Phases

1. **Preparation** — current IRP reviewed/tested annually; 24×7 on-call via PagerDuty; playbooks for ransomware, data breach, phishing compromise, insider threat, cloud misconfiguration, DDoS; annual IRP training; monitoring via AWS GuardDuty, CloudTrail, CrowdStrike Falcon, PagerDuty, Proofpoint.
2. **Identification** — detection sources: GuardDuty, PagerDuty, CrowdStrike, employee self-reporting (`security@nimbushr.example`), vendor notifications, external researcher reports. On-call Security Lead classifies severity per the matrix above.
3. **Containment** — *Short-term:* isolate affected systems (VPC security group / instance isolation); disable compromised Okta accounts; block malicious IPs at WAF; preserve volatile evidence before shutdown. *Long-term:* emergency patches; restrict to known-good IPs; expanded-scope investigation.
4. **Eradication** — root cause analysis with forensic evidence; remove malware/backdoors/unauthorized access; remediate exploited vulnerability; rotate all potentially compromised credentials; harden related controls.
5. **Recovery** — restore from last known-good backup (integrity-validated pre-compromise); validate system integrity before returning to production; 30-day enhanced monitoring; reconciliation of application/data integrity; documented recovery communications.
6. **Lessons Learned** — formal Post-Incident Review (PIR) within **72 hours** of closure — full timeline, root cause analysis, detection-gap analysis, MTTD/MTTR metrics, control failures, action items with owners. Incorporated into risk register updates, IRP revisions, and training updates.

## Roles and Responsibilities

| Role | Responsibilities | Owner |
|---|---|---|
| Incident Commander | Overall coordination; containment/escalation decisions; executive comms; regulatory notification decision | CISO (primary) / VP Compliance (backup) |
| Security Lead | Technical investigation, forensics, tool deployment, root cause analysis | GRC Analyst / Sr. Security Engineer |
| Communications Lead | External/client communications; regulatory notification; media inquiries | VP Communications / Legal Counsel (regulatory) |
| Legal Counsel | Regulatory notification guidance (GDPR 72-hr clock, state laws); legal hold; ransom-payment legal analysis | General Counsel / External Counsel |
| IT Operations | System isolation and recovery execution; backup restoration; vendor coordination | IT Manager / Engineering Lead (production) |

## Regulatory Notification Requirements

| Regulation | Trigger | Notification Target | Timeline |
|---|---|---|---|
| GDPR | Personal data breach affecting EU data subjects | Supervisory Authority (ICO / applicable EU DPA) | **72 hours** from discovery |
| GDPR | High risk to rights/freedoms of individuals | Affected EU data subjects | Without undue delay |
| CCPA | Breach of unencrypted/unredacted PII of CA residents | Affected California residents | Expediently / without unreasonable delay |
| State Breach Laws | Breach of PA/other state resident SSN, financial, or health data | Affected residents; state AG if threshold exceeded | Varies by state — PA: without unreasonable delay |
| Client Contracts | Any security incident affecting client data | Affected enterprise clients | **24 hours** (contractual Tier 1 SLA) |
