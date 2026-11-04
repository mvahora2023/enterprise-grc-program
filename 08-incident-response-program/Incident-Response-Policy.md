# Incident Response Policy

| Field | Value |
|---|---|
| Document ID | POL-IRP-001 |
| Version | 2.0 |
| Owner | CISO |
| Approved By | CEO, Legal Counsel |
| Effective Date | January 1, 2026 |
| Next Review | January 1, 2027 |

> This **Policy** establishes the *authority and requirements* for incident response at NimbusHR. The operational **[Incident Response Plan](Incident-Response-Plan.md)** is the document teams actually execute during an incident — this policy is what gives that plan its teeth.

## 1. Purpose

Governs the identification, containment, eradication, recovery, and post-incident review process for cybersecurity incidents affecting NimbusHR Technologies — establishing clear roles, escalation paths, communication requirements, and regulatory notification obligations.

## 2. Scope

Applies to all security events and incidents involving NimbusHR systems, data, vendors, or personnel — including incidents originating in third-party environments that affect NimbusHR or its clients.

## 3. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Incident Commander | CISO — overall incident coordination and decision-making authority |
| Technical Lead | Engineering Lead — system containment and forensic preservation |
| Communications Lead | VP of Compliance — client and regulatory communications |
| Legal Counsel | Regulatory notification obligations; evidence preservation; litigation hold |
| HR Representative | Insider threat incidents; employee disciplinary process |
| All Employees | Report suspected incidents to `security@nimbushr.example` within **1 hour** of discovery |

## 4. Operating Requirements by Phase

- **Preparation** — this Policy and the IRP are tested annually via tabletop exercise minimum; all employees trained on incident reporting; incident tooling maintained (GuardDuty, PagerDuty, CloudTrail, Okta System Log); Tier 1 vendor security-escalation contact list maintained.
- **Identification** — all alerts routed to PagerDuty on-call; incident ticket opened in Jira within **15 minutes** of P1/P2 alert confirmation.
- **Containment** — containment decisions for P1/P2 events require Incident Commander approval; forensic snapshots taken in parallel with clean-environment restoration.
- **Eradication** — eradication must be verified complete before proceeding to Recovery; all actions timestamped in the incident ticket.
- **Recovery** — 72-hour enhanced monitoring post-recovery; RTO/RPO conformance confirmed and any deviation documented.
- **Post-Incident Review** — conducted within **72 hours** of closure for P1/P2 events; corrective actions added to the [CAP tracker](../04-itgc-audit/Corrective-Action-Plan-Tracker.csv) with owners and due dates; IRP/playbooks updated based on lessons learned.

## 5. Evidence Preservation

All incident-related logs, system snapshots, and communications are preserved for a minimum of **7 years**. Legal Counsel issues a litigation hold notice for any incident with potential legal or regulatory implications; evidence must not be modified, deleted, or overwritten without Legal Counsel approval.

## 6. Regulatory Notification Requirements

See the full table in the [Incident Response Plan](Incident-Response-Plan.md#regulatory-notification-requirements). Legal Counsel must be notified **immediately** for any P1 incident to begin the regulatory notification assessment.
