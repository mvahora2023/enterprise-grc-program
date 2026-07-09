# GRC Program Scorecard — FY2026

One-page "report card" view of NimbusHR's GRC posture, built for board/CISO consumption. Backing detail for every row lives in its respective module.

| Domain | Score | Rating | Open Findings | Trend | Detail |
|---|---|---|---|---|---|
| Governance & Policy | **88%** | 🟢 Good | 2 | ↑ Improving | [Module 1](../01-governance-framework/) |
| Risk Management | **71%** | 🟡 Needs Improvement | 9 (High/Critical residual) | → Stable | [Module 2](../02-risk-register/) |
| Compliance — NIST CSF | **65%** | 🟡 Needs Improvement | 12 gaps identified | ↑ Improving | [Module 3](../03-nist-csf-gap-assessment/) |
| Audit — ITGC | **57%** | 🟠 At Risk | 14 open findings | → Stable | [Module 4](../04-itgc-audit/) |
| Vendor Risk Management | **74%** | 🟢 Good | 6 (across 4 vendors) | ↑ Improving | [Module 5](../05-vendor-risk-management/) |
| Identity & Access Management | **61%** | 🟡 Needs Improvement | 7 IAM findings | → Stable | [Module 6](../06-iam-soc2-assessment/) |
| Cloud & Network Security | **55%** | 🟠 At Risk | 10 cloud/network findings | ↓ Worsening | [Module 7](../07-network-cloud-devops-audit/) |
| Incident Response | **76%** | 🟢 Good | 3 process gaps | ↑ Improving | [Module 8](../08-incident-response-program/) |
| **Overall GRC Posture** | **68%** | 🟡 **Needs Improvement** | **63 total open items** | **↑ Improving** | This report |

## Reading the Scorecard

The program is trending in the right direction overall (5 of 8 domains improving or stable) but has two domains rated **At Risk**: **ITGC** (driven by the service-account MFA gap and unauthorized production deployments) and **Cloud & Network Security** — the only *worsening* domain, driven by the July 2026 discovery of a publicly exposed S3 bucket ([CLD-01](../07-network-cloud-devops-audit/Cloud-Security-Audit-Report.md)) and 14 repositories with hardcoded secrets ([DEV-01](../07-network-cloud-devops-audit/DevOps-SDLC-Governance-Audit.md)). Both were caught by this audit cycle's tooling, not by prior process — the honest read on this scorecard is that the program's *detection* got better in FY2026 even where the underlying *domain score* looks worse.

Full narrative and financial context: [`Annual-Executive-Risk-Report.md`](Annual-Executive-Risk-Report.md).
