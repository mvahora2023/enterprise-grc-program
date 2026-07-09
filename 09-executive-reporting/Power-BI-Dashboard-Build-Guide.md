# Master GRC Dashboard — Power BI Build Guide

This is a build specification, not a `.pbix` binary — page layout, visuals, and DAX measures precise enough to build in Power BI Desktop in under an hour, using the CSV data files already in this repository as the source tables. Publish to the NimbusHR Power BI workspace with Row-Level Security scoped to CISO / VP Compliance / Audit Committee; refresh nightly.

## Data Sources (already in this repo)

| Table | Source File |
|---|---|
| RiskRegister | [`02-risk-register/Enterprise-Risk-Register.csv`](../02-risk-register/Enterprise-Risk-Register.csv) |
| NISTGaps | [`03-nist-csf-gap-assessment/NIST-CSF-Gap-Scorecard.csv`](../03-nist-csf-gap-assessment/NIST-CSF-Gap-Scorecard.csv) |
| Findings | [`04-itgc-audit/Corrective-Action-Plan-Tracker.csv`](../04-itgc-audit/Corrective-Action-Plan-Tracker.csv) + [`07-network-cloud-devops-audit/Consolidated-Findings-Matrix.csv`](../07-network-cloud-devops-audit/Consolidated-Findings-Matrix.csv) |
| VendorRegister | [`05-vendor-risk-management/Vendor-Risk-Register.csv`](../05-vendor-risk-management/Vendor-Risk-Register.csv) |
| SOC2Scorecard | [`06-iam-soc2-assessment/SOC2-Readiness-Scorecard.csv`](../06-iam-soc2-assessment/SOC2-Readiness-Scorecard.csv) |
| IRMetrics | [`08-incident-response-program/IR-Metrics.csv`](../08-incident-response-program/IR-Metrics.csv) |
| MasterCAP | [`Master-CAP-Tracker.csv`](Master-CAP-Tracker.csv) |

## Page 1 — Executive Summary
Four KPI cards: **Overall GRC Compliance Score** (68%, conditional color green ≥80 / amber 60–79 / red <60), **Total Open Findings** (63, tooltip breakdown by severity), **High/Critical Risk Count** (residual ≥12 → 7 risks), **Overdue Remediations** (1 — CAP-001). Below: a 3×3 domain scorecard matrix pulling from [`GRC-Program-Scorecard.md`](GRC-Program-Scorecard.md). Date slicer for report period.

## Page 2 — Risk Dashboard
5×5 risk heat map (Likelihood × Impact) as a matrix visual, bubble size = risk count per cell, color red (15–25) / amber (8–14) / green (1–7). Bar chart: risk count by category. Line chart: average residual score by month. Table: all 18 risks with conditional formatting on Status (Overdue = red, In Progress = amber, Open = yellow).

## Page 3 — Audit Findings Dashboard
Donut: findings by severity (Critical/High/Medium/Low). Horizontal bar: finding count by audit area (Access Control, Change Management, Cloud, Network, DevOps, IAM). Table: overdue findings with a calculated `Days Overdue` column. Trend line: findings opened vs. closed by month. Gauge: closure rate (63% closed/in-progress vs. 100% target).

## Page 4 — Vendor Risk Dashboard
Card matrix: all 8 vendors with risk score/100 and color-coded rating. Gauge: portfolio average risk score (30.5/100) vs. target line (25/100). Table: overdue assessments. Stacked bar: open findings by vendor and severity.

## Page 5 — Compliance Dashboard
Radar/spider chart: NIST CSF 5 functions, Current Maturity vs. Target Maturity (gap visually apparent in Protect and Recover). Horizontal bar: control compliance % by subcategory, sorted by gap size. Gauge cluster: SOC 2 readiness by TSC category (Security 52% · Availability 67% · Confidentiality 25% · Processing Integrity 100% · Privacy 67%). Table: policy register with days-until-next-review, color-coded urgency.

## Page 6 — Incident Response Dashboard
Line chart: total incidents by month, target threshold line at 10/month. Dual-axis trend: MTTD and MTTR by quarter with target lines at 2h/4h. Donut: incident category breakdown. Trend line: SIEM false-positive rate (34% → 28%, target 20%). Table: incidents closed within SLA, quarter-over-quarter.

## Key DAX Measures

```dax
AVG_Residual_Risk = AVERAGE(RiskRegister[Residual Risk])

Compliance_Pct =
DIVIDE(
    COUNTROWS(FILTER(Controls, Controls[Status] = "Implemented")),
    COUNTROWS(Controls), 0
)

MTTD_Hours = AVERAGE(IRMetrics[Mean Time to Detect (MTTD - hours)])

Closure_Rate =
DIVIDE(
    COUNTROWS(FILTER(Findings, Findings[Status] IN {"Closed", "Remediated"})),
    COUNTROWS(Findings), 0
)

Days_Overdue = DATEDIFF(Findings[Due Date], TODAY(), DAY)
```
