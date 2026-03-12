# Upgrade Triggers

Version: 0.1
Last Updated: {{DATE}}

> Defines when to escalate architecture. Do not add complexity until a trigger is met.

---

## Trigger Rules

| Condition | Action |
| --------- | ------ |
| >1 external user | Add authentication |
| Shared multi-device usage | Move from SQLite to Postgres |
| Public traffic | Add rate limiting + monitoring |
| Storing PII | Add data retention policy + audit logging |
| Payments added | Add security hardening |
| AI feature with external actions | Add tool allowlist + explicit user confirmation |
| Users in EU/UK/CA | Complete jurisdiction-specific privacy checks |
| Minors may use product | Add age-gating or block collection |
| Regulated/sensitive data added | Trigger legal/compliance review + DPIA/PIA-style assessment |
| Cross-domain high-risk change (feature + security + architecture) | Recommend temporary multi-agent mode |
| Planned change touches >=4 files | Recommend temporary multi-agent mode |
| Two consecutive tasks touch <=3 files each and no material review findings | Recommend return to single-agent mode |
| Multi-agent overhead delays delivery without added quality findings | Recommend return to single-agent mode |
| Closing a major phase or stage | Run User/Consumer Journey Completion Gate (`Discover -> Acquire Access -> Verify -> Deliver -> Study/Use -> Support/Recovery`) and log gaps before closure |
| Preparing production release candidate | Run Product Readiness Polish Gate (UI + legal + professionalism) |
| Release-critical path depends on model behavior | Document and review model-selection strategy before release |
| (Add project-specific triggers below) | |

---

## Project-Specific Triggers

<!-- Add triggers for this project based on the Bootstrap Interview. -->

---

## Multi-Agent Safety Thresholds

Use these thresholds to reduce avoidable overhead and drift.

- Prefer single-agent mode by default.
- Enable multi-agent only for complex or high-risk tasks.
- Re-check benefit after each major task.
- Inform the user when switching modes and why.

## Tier2 Roadmap (Coming Soon)

Tier2 is planned as a future, higher-assurance workflow focused on reducing setup friction and increasing first-pass correctness.

Planned intent (subject to validation):

- Guaranteed structure and run-order checks executed.
- Guided checkpoints with explicit human approvals.
- Stronger session continuity and auditability.
- Clear boundaries for what is automated vs human judgment.

This section is a roadmap note only and does not represent a released feature.
