# Network Security Audit — FY2026

Audits governance and process — *whether the right protections are in place, documented, and consistently followed* — not exploitation (that is penetration testing, performed separately and referenced under vendor evidence). Full finding tracker: [`Consolidated-Findings-Matrix.csv`](Consolidated-Findings-Matrix.csv)

## NET-01 — Unrestricted Inbound SSH Access on 3 EC2 Instances — **High**
Security groups for 3 EC2 instances in `us-east-1` allow unrestricted inbound access (`0.0.0.0/0`) on port 22, hosting components of the data processing pipeline.
**Root cause:** Security groups configured at initial standup without IP allowlisting; no automated policy check detects overly permissive rules.
**Risk:** Exposure to brute-force attacks and unauthorized remote access; successful exploitation could provide a foothold for lateral movement to RDS and the Snowflake integration layer.
**Recommendation:** Restrict SSH inbound to corporate IP range + VPN exit nodes; implement AWS Config rule to detect/alert on `0.0.0.0/0` on port 22/3389; transition to AWS Systems Manager Session Manager, eliminating exposed SSH ports entirely.

## NET-02 — No Network Segmentation Between Dev and Production VPCs — High
Dev and production VPCs are peered with no NACL restriction beyond Security Group rules.
**Risk:** An attacker compromising the (typically weaker-controlled) dev environment could pivot to production via the peering connection — also a SOC 2 change-management/environment-isolation violation.
**Recommendation:** Implement strict NACLs on the peering connection; evaluate migration to a fully isolated production VPC; require an explicit bastion/VPN for cross-environment access.

## NET-03 — VPC Flow Logs Not Enabled on 2 of 5 VPCs — Medium
Flow Logs are missing on the EU data-residency VPC and the development VPC, creating monitoring blind spots and impairing GDPR accountability in the EU environment (see CLD-02).
**Recommendation:** Enable Flow Logs on all VPCs; route to a centralized S3 bucket (12-month retention); AWS Config rule to detect gaps.

## NET-04 — Internal Vulnerability Scans Performed Only Quarterly — Medium
Tenable.io scans run quarterly; infrastructure grew from 12 to 47 EC2 instances without revisiting scan cadence. A 90-day exposure window is significant for actively exploited Critical CVEs (cross-ref [R-007](../02-risk-register/Enterprise-Risk-Register.csv)).
**Recommendation:** Increase to weekly scans for production; continuous scanning via Tenable AWS cloud connector; 15-day SLA for Critical/High remediation.

## NET-05 — DNS Logging Not Enabled on Route 53 — Low
Limits forensic capability for DNS tunneling / command-and-control detection.
**Recommendation:** Enable Route 53 Resolver query logging for all VPCs; 12-month retention; integrate into future SIEM.
