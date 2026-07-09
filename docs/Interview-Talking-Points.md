# Interview Talking Points

Concrete, deliverable-specific answers for interviews — each one names a real artifact in this repository, a specific framework, and a business outcome. Adapt in your own voice.

## Module 1 — Governance Framework
*"I designed a governance framework — a GRC Program Charter, Information Security Policy, Risk Appetite Statement, and RACI matrix — mirroring what enterprise GRC teams maintain annually. I structured it around NIST CSF Govern principles and NIST SP 800-53 PL and PS control families, and it's the foundational layer every other module in the program references."*

## Module 2 — Enterprise Risk Register
*"I built an 18-item enterprise risk register with inherent and residual scoring on a 5×5 likelihood-impact matrix, risk ownership, and treatment plans — then designed the Power BI heat map specification leadership would use to prioritize remediation, the same artifact a GRC team produces for a quarterly risk committee."*

## Module 3 — NIST CSF Gap Assessment
*"I ran a full NIST CSF gap assessment across all 20 subcategories in all five functions — Identify, Protect, Detect, Respond, Recover — on a four-level maturity scale, and produced a remediation roadmap with NIST 800-53 and CIS Controls v8 cross-mapping. The assessment surfaced that Recover had the largest gap in the whole program — the company literally couldn't prove it could restore from a ransomware attack, which became the anchor finding for the entire report."*

## Module 4 — ITGC Audit
*"I performed an ITGC audit covering access control, change management, and segregation of duties — the same three pillars tested in SOX and SOC 2 audits — and found a Critical finding (MFA missing on 6 production-access service accounts) alongside a segregation-of-duties conflict where one DevOps engineer could approve their own production deployments. I documented every test in formal workpapers with a corrective action plan tracker."*

## Module 5 — Third-Party Vendor Risk
*"I built a complete vendor risk program — policy, a 30+ question assessment questionnaire, individual risk assessments across cloud, identity, payroll, and code-repository vendor categories, and a risk register. One assessment (GitHub) surfaced a Critical finding — 14 repositories with hardcoded production credentials — that I flagged for same-day emergency remediation rather than waiting for the standard 30-day cycle. Third-party risk is consistently the most underrepresented skill in entry-level GRC candidates, and this module is built to close that gap directly."*

## Module 6 — IAM Audit & SOC 2 Readiness
*"I conducted an IAM audit that found 23% of users hadn't enrolled in MFA and that privileged access hadn't been recertified in 14 months, then ran a full SOC 2 Type II readiness assessment against all five AICPA Trust Services Criteria. The program came out at 62% readiness — below the 85% threshold I'd recommend before scheduling a real audit — with two audit-disqualifying failures I flagged as the top two priorities in the executive report."*

## Module 7 — Network, Cloud & DevOps Audit
*"I audited network configuration, AWS cloud infrastructure, and DevOps/SDLC governance and found 15 findings, including a publicly exposed S3 bucket containing 847 historical payroll files — an active data exposure, not a theoretical one — which I treated as an emergency and documented the same-day remediation. I also produced the executive translation of every technical finding into business risk language, because that's the actual job."*

## Module 8 — Incident Response Program
*"I wrote a full Incident Response Plan with a four-tier severity matrix and regulatory notification requirements, then facilitated a ransomware tabletop exercise I designed to specifically stress-test the gaps I already knew existed in the program — the hardcoded GitHub secrets from Module 7 became the tabletop's exact intrusion vector. Five of eight injects surfaced a real, previously undocumented process gap, which is the whole point of running one."*

## Module 9 — Executive Reporting
*"I built the Power BI dashboard specification and wrote the annual executive risk report, including a financial stewardship section that ties every recommended control investment to a dollar figure — for example, a $60K DLP deployment against an estimated $2.1M in avoided breach cost. Translating technical risk into a number a CFO will act on is the most senior GRC skill there is, and it's the thread running through every module in this repository."*

## Closing / Full-Project Summary
*"While I haven't yet held a formal enterprise GRC title, I designed, built, and documented a complete enterprise GRC program — governance, risk management, ITGC auditing, vendor risk, IAM, SOC 2 assessment, cloud and DevOps security auditing, incident response, and executive reporting — all cross-referenced against each other exactly the way a real GRC program's risk register, audit findings, and dashboard all describe the same organization. Every deliverable cites the specific NIST CSF subcategory, NIST 800-53 control, SOC 2 criterion, or CIS Controls v8 safeguard it maps to. It's public on my GitHub if you'd like to walk through any part of it."*
