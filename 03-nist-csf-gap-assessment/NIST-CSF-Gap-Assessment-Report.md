# NIST CSF Gap Assessment — FY2026

Full scorecard: [`NIST-CSF-Gap-Scorecard.csv`](NIST-CSF-Gap-Scorecard.csv) (20 subcategories across all 5 functions)

## Methodology

Conducted in accordance with **NIST Cybersecurity Framework v1.1**. Current maturity is scored against a defined target state per subcategory on a 4-point scale:

| Level | Name | Description |
|---|---|---|
| 1 | Initial / Ad Hoc | Controls are ad hoc, reactive, or undefined |
| 2 | Risk Informed | Controls are defined but inconsistently applied |
| 3 | Repeatable | Controls are formally documented and consistently implemented |
| 4 | Adaptive | Controls are automated, continuously monitored, and optimized |

Evidence was gathered through management interviews, documentation inspection, system configuration review, and re-performance of selected control procedures. Target maturity states reflect client contractual requirements, regulatory obligations, and NimbusHR's [Risk Appetite Statement](../01-governance-framework/Risk-Appetite-Statement.md).

## Maturity Summary by Function

| NIST CSF Function | Current Avg. Maturity | Target Avg. Maturity | Gap | Status |
|---|---|---|---|---|
| Identify (ID) | 2.8 | 4.0 | 1.2 | Below Target |
| Protect (PR) | 2.5 | 3.8 | **1.3** | Below Target — Priority |
| Detect (DE) | 2.5 | 3.8 | 1.3 | Below Target |
| Respond (RS) | 2.7 | 4.0 | 1.3 | Below Target |
| Recover (RC) | 2.0 | 3.5 | **1.5** | Below Target — Critical |
| **Overall** | **2.6** | **3.8** | **1.2** | **Needs Improvement** |

- **Controls at target maturity:** 2 of 20 (10%) — ID.GV-1 and PR.DS-1 (both 4/4)
- **Critical gap areas:** Data Loss Prevention (PR.DS-5, gap 3), Access recertification (PR.AC-4, gap 2), BCP/DR testing (RC.RP-1, gap 2), SIEM/UEBA (DE.CM-7, gap 2)
- **Functions below target:** all five; **Recover has the largest gap (1.5)**

## Executive Gap Summary

NimbusHR's cybersecurity program has a solid policy foundation and several strong technical controls, but the assessment reveals significant gaps in the ability to **detect** and **recover from** cybersecurity events. In plain terms: NimbusHR can largely prevent common attacks, but has limited visibility into whether an attack is happening right now, and — critically — has not validated its ability to recover from a major incident such as ransomware in over 18 months (see [R-015](../02-risk-register/Enterprise-Risk-Register.csv)).

The most urgent business risk is the **absence of a Data Loss Prevention (DLP) solution** (PR.DS-5, current maturity 1/4) — NimbusHR has no technical mechanism to detect or block unauthorized exfiltration of employee PII, SSNs, or banking data for 1.2M individuals, a direct exposure to GDPR fines, CCPA liability, and reputational harm to $42M in ARR.

The second most urgent gap is the lack of **validated backup recovery** (RC.RP-1) — NimbusHR cannot currently confirm it could restore operations within contractually committed timeframes in a ransomware scenario. Both gaps directly threaten SOC 2 Type II certification, a contractual prerequisite for ~40% of NimbusHR's enterprise client base (~$16.8M ARR). Both are top priorities in the Annual Executive Risk Report's H2 2026 roadmap.

## Framework Cross-Mapping (Selected)

| Gap | NIST SP 800-53 | CIS Controls v8 | SOC 2 TSC |
|---|---|---|---|
| PR.AC-1 (MFA gap) | IA-2, IA-5 | 6.3, 6.5 | CC6.1 |
| PR.AC-4 (access recert) | AC-2, AC-6 | 5.1, 5.4 | CC6.2 |
| PR.DS-5 (no DLP) | SI-4, SC-7 | 3.13 | CC6.7 |
| DE.CM-7 (no SIEM) | SI-4, AU-6 | 8.11, 13.1 | CC7.1 |
| RC.RP-1 (no DR test) | CP-4, CP-9 | 11.2, 11.5 | A1.3 |

A complete 20-control mapping to NIST 800-53, SOC 2, and CIS Controls v8 is maintained in the program's internal control library.
