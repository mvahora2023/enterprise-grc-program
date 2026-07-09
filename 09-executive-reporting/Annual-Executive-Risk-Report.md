# Annual Executive Risk Report — FY2026

**Prepared by:** GRC Analyst · **Sponsor:** CISO · **Owner:** VP, Compliance and Risk · **Report Period:** FY2026 · **Classification:** Board / Audit Committee

## 1. GRC Program Overview

NimbusHR's GRC Program was chartered in January 2023 and operating under its current structure since January 2025. FY2026 was its most comprehensive cycle to date: an 18-item enterprise risk register, a full NIST CSF gap assessment across 20 subcategories, an ITGC audit, four vendor risk assessments, a complete IAM + SOC 2 readiness audit, a network/cloud/DevOps security audit, and the company's **first structured tabletop exercise**. The Audit Committee receives semi-annual status reports; the CISO receives monthly risk metrics.

## 2. Risk Landscape Summary

The register grew from 12 items (FY2025) to **18 items** in FY2026, reflecting expanded coverage into cloud, DevOps, and regulatory domains. Top 5 risks by residual score (all at 12/25):

1. **[R-001](../02-risk-register/Enterprise-Risk-Register.csv)** — Unauthorized Access via Compromised Credentials — highest-priority risk on the register
2. **[R-003](../02-risk-register/Enterprise-Risk-Register.csv)** — Third-Party Data Breach via ADP Integration
3. **[R-015](../02-risk-register/Enterprise-Risk-Register.csv)** — Backup Failure / Inadequate Recovery — the single most operationally dangerous open item; **overdue**
4. **[R-016](../02-risk-register/Enterprise-Risk-Register.csv)** — Orphaned User Accounts
5. **[R-018](../02-risk-register/Enterprise-Risk-Register.csv)** — SOC 2 Type II Audit Unpreparedness — **$16.8M ARR at risk**

Full register and heat map: [`02-risk-register/`](../02-risk-register/)

## 3. Compliance Status

NIST CSF maturity improved from 2.3 (FY2025 baseline) to **2.6** overall in FY2026 — progress in governance documentation, encryption controls, and incident response capability — against a target of 3.8. **SOC 2 Type II readiness stands at 62%**, below the 85% minimum recommended before scheduling a formal audit. Five critical H2 2026 priorities: DLP deployment, DR test completion, data disposal procedures, service-account MFA remediation, and quarterly access recertification — each with a named owner, budget, and due date. See [`03-nist-csf-gap-assessment/`](../03-nist-csf-gap-assessment/) and [`06-iam-soc2-assessment/`](../06-iam-soc2-assessment/).

## 4. Audit Findings Summary

The FY2026 audit program generated **23 total findings** across ITGC, IAM, cloud, network, and DevOps domains — 3 Critical, 8 High, 7 Medium, 5 Low. The two Critical emergency findings — [CLD-01](../07-network-cloud-devops-audit/Cloud-Security-Audit-Report.md) (public S3 payroll bucket) and [DEV-01](../07-network-cloud-devops-audit/DevOps-SDLC-Governance-Audit.md) (14 repos with hardcoded secrets) — were both remediated same-day upon discovery. Average finding closure time is 34 days against a 21-day target for High findings; **1 finding (AC-03/CAP-001) is overdue**. Full tracker: [`Master-CAP-Tracker.csv`](Master-CAP-Tracker.csv).

## 5. Vendor Risk Status

8 vendors assessed: 3 Tier 1 (Okta, Stripe, ADP) and 5 Tier 2 (GitHub, Twilio, Snowflake, PagerDuty, AWS). Overall portfolio risk is **Medium**, driven by ADP (Medium-High, 58/100) and GitHub (Medium, 44/100). Okta and Stripe both rate Low with strong third-party certification programs. Vendor assessment coverage reached **100% of Tier 1/Tier 2 vendors** in FY2026, up from 75% in FY2025. See [`05-vendor-risk-management/`](../05-vendor-risk-management/).

## 6. Financial Stewardship Impact

The GRC program directly protects NimbusHR's **$42M ARR** through three mechanisms:

- **Client Revenue Protection** — SOC 2 Type II is a contractual prerequisite for ~40% of the enterprise client base; loss of certification risks **$16.8M in ARR**.
- **Regulatory Fine Avoidance** — a material GDPR breach affecting the 230,000 EU data subjects on the platform could reach **$1.68M** (4% of ARR); CCPA exposure adds further risk.
- **Breach Cost Prevention** — industry benchmarks (IBM Cost of a Data Breach Report) put the average HR-sector breach at **$4.88M**; proposed H2 2026 investments — a DLP solution ($60K/yr, preventing an estimated $2.1M in breach cost, ~34:1 ROI) and a SIEM/UEBA platform ($95K/yr) — are the two highest-leverage spends in the roadmap.

**Total FY2026 GRC program budget:** $280K. **Estimated risk exposure reduction from the H2 2026 roadmap:** $4.5M+ in avoided regulatory, breach, and client-loss costs.

## 7. Strategic Recommendations — H2 2026 Roadmap

| # | Recommendation | Priority | Target |
|---|---|---|---|
| 1 | Execute DR/BCP restoration test, validate RTO ≤4h / RPO ≤1h for all Tier 1 systems | **Critical** | Sep 30, 2026 |
| 2 | Procure and deploy a DLP solution (Microsoft Purview or Forcepoint) | **Critical** | Oct 31, 2026 |
| 3 | Deploy a SIEM/UEBA platform (Splunk Cloud or Microsoft Sentinel) | High | Q3 2026 |
| 4 | Implement automated HRIS-to-Okta deprovisioning via SCIM | High | Sep-Oct 2026 |
| 5 | Integrate SAST/DAST as a mandatory CI/CD pipeline gate | High | Sep 30, 2026 |
| 6 | Complete quarterly access recertification program + formal RBAC for engineering sub-teams | High | Oct 1, 2026 |
| 7 | Renegotiate ADP contract terms (pen test cadence, 24-hr notification SLA, data retention clause) | Medium-High | Oct 2026 renewal |
| 8 | Establish continuous, automated SOC 2 evidence collection (Okta, AWS Config, CloudTrail, GitHub APIs) | High | Aug 31, 2026 |

Full CAP tracker with owners, completion %, and status: [`Master-CAP-Tracker.csv`](Master-CAP-Tracker.csv). One-page scorecard: [`GRC-Program-Scorecard.md`](GRC-Program-Scorecard.md).
