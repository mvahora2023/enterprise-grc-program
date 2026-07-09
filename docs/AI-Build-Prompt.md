# How This Program Was Built — AI-Assisted GRC Workflow

Transparency note: this repository was built using **Claude** (Anthropic) as a drafting and structuring tool, directed and reviewed by the author throughout. This is not a disclaimer to downplay the work — it's a demonstration of a real, current GRC skill: knowing how to direct an AI assistant to produce audit-grade documentation at the speed a real GRC team needs, while retaining full ownership of the judgment calls (risk scoring, control mapping, finding severity, remediation prioritization).

## The Context Prompt

The prompt below is the reusable context block used to keep every deliverable consistent — same fictional company, same regulatory scope, same framework citations — across every module in this repository. Paste it as the first message in a new session, then request a specific deliverable.

```
You are acting as a senior enterprise GRC (Governance, Risk & Compliance) analyst
and consultant. I am a cybersecurity professional building a portfolio-grade
Enterprise Cybersecurity GRC Program Simulation to demonstrate real-world GRC
competencies to hiring managers.

PROJECT CONTEXT:
Fictional company: NimbusHR Technologies — SaaS HR platform, 350 employees,
120 enterprise clients, 1.2M end users, AWS (us-east-1 / eu-west-1), Okta,
GitHub, Snowflake. Regulatory scope: SOC 2 Type II, GDPR, CCPA, NIST CSF.

The program is organized into 9 modules:
1. Governance Framework    4. ITGC & Application Controls Audit
2. Enterprise Risk Register 5. Third-Party Vendor Risk Management
3. NIST CSF Gap Assessment  6. IAM Audit & SOC 2 Readiness Assessment
                             7. Network, Cloud & DevOps Security Audit
                             8. Incident Response Program & Tabletop Exercise
                             9. Executive GRC Dashboard & Annual Risk Report

YOUR ROLE: When asked to build a deliverable, generate a complete, realistic,
enterprise-quality document using real GRC terminology and citing the specific
framework controls that apply (NIST CSF subcategory, NIST 800-53 control ID,
SOC 2 Trust Services Criteria, CIS Controls v8). Maintain consistency — the
same risks, findings, and vendors must reappear correctly across every module.
```

## What the AI Did vs. What the Analyst Did

| AI-Assisted | Analyst-Owned |
|---|---|
| First-draft document structure and formatting | Risk scoring methodology and final likelihood/impact ratings |
| Boilerplate policy language (retention periods, classification tiers) | Which findings are Critical vs. High vs. Medium, and why |
| Cross-referencing risks/findings across modules for narrative consistency | Remediation prioritization and the H2 2026 roadmap sequencing |
| CSV/table formatting for Excel/Power BI import | Framework-to-framework control mapping (NIST ↔ SOC 2 ↔ CIS) |
| Tabletop exercise scenario prose | Deciding which gaps the tabletop should be designed to surface |

## Why This Matters for a GRC Role

Every real GRC team now works this way — using AI to accelerate first drafts of policies, control matrices, and audit workpapers while the analyst owns risk judgment and quality review. Being fluent in directing that workflow, and being explicit about where the line between "AI draft" and "professional judgment" sits, is itself a demonstrable GRC skill: it's the same discipline as reviewing a junior analyst's first-draft workpaper before it goes to the auditor.
