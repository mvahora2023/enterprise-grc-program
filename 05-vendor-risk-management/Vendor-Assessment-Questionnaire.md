# Vendor Security Assessment Questionnaire

**Template Version:** 2.1 | **For:** Tier 1 and Tier 2 Vendors (per the [Vendor Risk Management Policy](Vendor-Risk-Management-Policy.md))

## Instructions

Complete all sections applicable to your service tier. Responses should reflect current security posture. Supporting evidence (SOC 2 reports, certifications, pen test summaries) should be attached where indicated. Completed questionnaires are reviewed by the NimbusHR GRC team and retained for 3 years.

**Return to:** `grc@nimbushr.example` | **Response Deadline:** 30 days from receipt

## Section 1 — Company & Service Overview (All Tiers)

| # | Question |
|---|---|
| 1.1 | Legal name of organization |
| 1.2 | Primary service provided to NimbusHR |
| 1.3 | What categories of NimbusHR data does your service access or process? |
| 1.4 | Where is NimbusHR data stored? (Country/Region) |
| 1.5 | Do you use sub-processors to process NimbusHR data? If yes, list them |
| 1.6 | Primary security contact name and email |
| 1.7 | Do you have a dedicated information security team? (Size) |

## Section 2 — Certifications & Compliance (All Tiers)

| # | Question | Evidence Required |
|---|---|---|
| 2.1 | Do you hold a current SOC 2 Type II certification? | Attach report summary |
| 2.2 | If yes, which Trust Services Criteria are covered? | |
| 2.3 | When was the last SOC 2 audit period? | |
| 2.4 | Were any exceptions noted in the SOC 2 report? | Describe if yes |
| 2.5 | Do you hold ISO 27001 certification? | Attach certificate |
| 2.6 | Are you PCI DSS certified? (if handling payment data) | Specify level |
| 2.7 | Do you comply with GDPR? | Describe program |
| 2.8 | Are you FedRAMP authorized? | |

## Section 3 — Access Control (All Tiers)

| # | Question |
|---|---|
| 3.1 | Is MFA required for all employee access to systems processing NimbusHR data? |
| 3.2 | Is MFA enforced for privileged/administrative accounts? |
| 3.3 | Describe your user access provisioning and deprovisioning process |
| 3.4 | How frequently are access rights reviewed and recertified? |
| 3.5 | Do you enforce least-privilege access controls (RBAC)? |
| 3.6 | Are shared accounts or shared credentials permitted? |
| 3.7 | Do you use Privileged Access Management (PAM) tooling? (specify product) |
| 3.8 | How quickly are terminated employee accounts disabled? |

## Section 4 — Data Security (Tier 1 & 2)

| # | Question |
|---|---|
| 4.1 | Is data encrypted at rest? What algorithm/standard? |
| 4.2 | Is data encrypted in transit? What protocols/TLS version? |
| 4.3 | Do you have a Data Loss Prevention (DLP) solution in place? |
| 4.4 | How is NimbusHR data logically isolated from other client data? |
| 4.5 | What is your data retention period for NimbusHR data? |
| 4.6 | Describe your data disposal process at contract termination |
| 4.7 | Can you provide a data destruction certificate upon request? |
| 4.8 | Do you process EU personal data? If yes, what legal basis? |

## Section 5 — Vulnerability Management (Tier 1 & 2)

| # | Question |
|---|---|
| 5.1 | How frequently do you scan internet-facing systems for vulnerabilities? |
| 5.2 | How frequently do you perform internal vulnerability scans? |
| 5.3 | What are your SLAs for remediating critical vulnerabilities? |
| 5.4 | Have you conducted a penetration test in the last 12 months? |
| 5.5 | Was the pen test performed by an independent third party? |
| 5.6 | Can you provide a summary of pen test findings and remediation status? |
| 5.7 | Do you have a vulnerability disclosure / bug bounty program? |

## Section 6 — Incident Response (All Tiers)

| # | Question |
|---|---|
| 6.1 | Do you have a documented Incident Response Plan (IRP)? |
| 6.2 | When was the IRP last tested (tabletop or simulation)? |
| 6.3 | What is your SLA to notify NimbusHR of a security incident affecting our data? |
| 6.4 | Have you experienced a data breach in the last 3 years? |
| 6.5 | If yes, were affected customers notified within regulatory timelines? |
| 6.6 | Do you carry cyber liability insurance? Coverage amount? |
| 6.7 | Who is the designated point of contact for security incidents? |

## Section 7 — Business Continuity (Tier 1)

| # | Question |
|---|---|
| 7.1 | Do you have a Business Continuity Plan (BCP)? |
| 7.2 | What is your target RTO for critical services? |
| 7.3 | What is your target RPO? |
| 7.4 | When was your last BCP/DR test? |
| 7.5 | Do you have redundant data centers or cloud availability zones? |
| 7.6 | What is your documented uptime SLA for services provided to NimbusHR? |

## Section 8 — Vendor Attestation

By submitting this questionnaire, the undersigned attests that the information provided is accurate and complete to the best of their knowledge as of the date indicated.

| Field | Value |
|---|---|
| Authorized Representative Name | |
| Title | |
| Date | |
| Signature | |

*NimbusHR GRC Team | `grc@nimbushr.example` | Vendor Management Policy POL-VMP-001*
