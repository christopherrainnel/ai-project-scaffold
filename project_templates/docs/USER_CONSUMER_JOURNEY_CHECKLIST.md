# User/Consumer Journey Checklist (Project-Specific)

Version: 1.0
Last Updated: {{DATE}}
Owner: Product owner

Purpose: single execution checklist for this project so all agents can track real user progress from discovery to successful access, delivery, and recovery.

Status key:
- Complete: implemented and validated in the current environment
- Conditional: implemented but requires additional validation before sign-off
- Gap: missing or not reliably usable for non-technical users

## Active Journey Variant

- Variant: paid consumer (Tier1 or equivalent paid entitlement path)
- Entry host currently used: {{PUBLIC_BASE_URL}}

If this project is not using a paid-consumer path, replace the variant above with the actual journey type before release work begins.

## Stage Checklist

### 1) Discover

- [ ] Landing page or product entry point is reachable.
- [ ] Trust baseline exists (branding, support contact, privacy/terms links where applicable).
- [ ] A non-technical visitor can understand the flow from purchase or qualification to access.

Current status: Gap
Evidence: Add release-cycle evidence here.

### 2) Acquire Access

- [ ] User can initiate payment or qualification from the intended product flow.
- [ ] The purchase, signup, or qualification path is explicit and not hidden behind manual instructions.
- [ ] The user understands what happens before, during, and after access verification.

Current status: Gap
Evidence: Add release-cycle evidence here.

### 3) Verify

- [ ] Verification or entitlement eligibility path exists when required.
- [ ] Unverified or unpaid users do not receive protected access.
- [ ] Failure states show an actionable next step.

Current status: Gap
Evidence: Add release-cycle evidence here.

### 4) Deliver

- [ ] User can successfully reach the promised asset, account, page, or workflow.
- [ ] Status transitions are recorded or auditable.
- [ ] At least one realistic end-to-end proof run has been completed.

Current status: Gap
Evidence: Add release-cycle evidence here.

### 5) Study + Use

- [ ] First-time instructions exist and are visible at the point of use.
- [ ] The user can take the first meaningful action without extra hand-holding.
- [ ] Post-access guidance is understandable for the intended audience.

Current status: Gap
Evidence: Add release-cycle evidence here.

### 6) Support + Recovery

- [ ] Recovery path exists for expired links, mismatched accounts, or other common failures.
- [ ] Support actions are documented and auditable.
- [ ] Recovery does not require unsafe manual shortcuts.

Current status: Gap
Evidence: Add release-cycle evidence here.

## Immediate Gaps To Close (Priority Order)

1. Replace placeholders in this checklist with project-specific evidence before release.
2. Run at least one realistic end-to-end proof for the active journey variant.

## Agent Execution Rule (Project-Specific)

For any task that affects public pages, payment/verification, access handling, onboarding, delivery, support, or release readiness:

1. Read this file before editing.
2. Update impacted stage checkboxes and status labels.
3. Add a matching evidence note in `CHANGELOG_AI.md`.
4. Do not mark release complete if any in-scope stage remains `Gap` unless the owner explicitly accepts the defer.
