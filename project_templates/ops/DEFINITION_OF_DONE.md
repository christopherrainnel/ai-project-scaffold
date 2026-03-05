# Definition of Done (Future Features)

Version: 1.0
Last Updated: {{DATE}}

Use this checklist before merging feature work.

## Product Quality

- [ ] Acceptance criteria are met.
- [ ] One vertical slice is complete end-to-end.
- [ ] Non-goals were not accidentally included.
- [ ] User Journey Completion Gate evaluated for the current phase/stage (`Discover -> Buy (if applicable) -> Verify -> Deliver -> Study/Use -> Support/Recovery`) with unresolved gaps explicitly documented.
- [ ] If the project has no purchase path, the `Buy (if applicable)` stage is mapped to an equivalent access/adoption checkpoint and recorded.

## Engineering Quality

- [ ] Lint, format, typecheck, tests, and build pass.
- [ ] CI workflow passes on pull request.
- [ ] Changes are small, focused, and reviewed.

## Security & Privacy

- [ ] No secrets are committed.
- [ ] Input validation and authorization checks are in place.
- [ ] Rate limits/abuse controls are added for public endpoints.
- [ ] Logging avoids secrets and personal data.
- [ ] Data retention/deletion impacts are reflected in `docs/PRIVACY.md`.

## Documentation & Operations

- [ ] `docs/DECISIONS.md` updated for architectural choices.
- [ ] `docs/THREAT_MODEL.md` updated for new attack surfaces.
- [ ] `ops/RUNBOOK.md` updated if operations changed.
- [ ] `CHANGELOG_AI.md` entry added.

## Compliance Wording Rule

- [ ] Language uses "aligned with" or "informed by" standards.
- [ ] No certification/compliance claims are made without proof.
