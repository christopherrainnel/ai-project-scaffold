# User/Consumer Journey Checklist (Project-Specific)

Version: 1.1
Last Updated: {{DATE}}
Owner: Product owner

> Keep this file in fresh placeholder state until the operator defines the actual journey variant for the project.

Status key:
- Complete: implemented and validated in the current environment
- Conditional: implemented but requires additional validation before sign-off
- Gap: missing or not reliably usable for non-technical users
- Awaiting human validation: implementation exists, but required practical testing or owner confirmation is still pending

## Active Journey Variant

- Variant: <!-- e.g. paid consumer / internal operator / B2B workspace / not applicable yet -->
- Entry host currently used: <!-- e.g. staging URL / public base URL / N/A -->

## Validation Ownership Rule

- Complete all credible `AI-runnable verification` before requesting human practical testing.
- `Developer POV practical testing` is used only when automation cannot credibly validate the behavior.
- `Consumer POV practical testing` requires human owner confirmation when the stage depends on real user experience rather than technical evidence alone.
- AI may prepare test steps, expected outcomes, pass/fail capture format, and fallback checks, but must not self-certify consumer proof.
- If required human practical testing is still pending, mark the affected stage `Awaiting human validation` and do not treat it as complete.

## Stage Checklist

### 1) Discover

- [ ] Landing page or product entry point is reachable.
- [ ] Trust baseline exists for the actual journey.
- [ ] A non-technical user can understand the path from entry to success.

Current status: <!-- Gap / Conditional / Complete / Awaiting human validation -->
Evidence: <!-- Add project-specific release evidence here. -->

### 2) Acquire Access

- [ ] User can start the intended signup, purchase, qualification, or entry flow.
- [ ] The access path is explicit for this project.
- [ ] The user understands what happens before, during, and after access or setup.

Current status: <!-- Gap / Conditional / Complete / Awaiting human validation -->
Evidence: <!-- Add project-specific release evidence here. -->

### 3) Verify

- [ ] Verification or eligibility path exists when required.
- [ ] Unauthorized users do not receive protected access when protection is in scope.
- [ ] Failure states show an actionable next step.

Current status: <!-- Gap / Conditional / Complete / Awaiting human validation -->
Evidence: <!-- Add project-specific release evidence here. -->

### 4) Deliver

- [ ] User can successfully reach the promised asset, account, page, or workflow.
- [ ] Status transitions are recorded or auditable when needed.
- [ ] At least one realistic end-to-end proof run has been completed.

Current status: <!-- Gap / Conditional / Complete / Awaiting human validation -->
Evidence: <!-- Add project-specific release evidence here. -->

### 5) Study + Use

- [ ] First-time instructions exist and are visible at the point of use.
- [ ] The user can take the first meaningful action without extra hand-holding.
- [ ] Post-access guidance is understandable for the intended audience.

Current status: <!-- Gap / Conditional / Complete / Awaiting human validation -->
Evidence: <!-- Add project-specific release evidence here. -->

### 6) Support + Recovery

- [ ] Recovery path exists for common failures relevant to this project.
- [ ] Support actions are documented and auditable when needed.
- [ ] Recovery does not require unsafe manual shortcuts.

Current status: <!-- Gap / Conditional / Complete / Awaiting human validation -->
Evidence: <!-- Add project-specific release evidence here. -->
