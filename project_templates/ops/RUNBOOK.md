# Runbook (Operations Basics)

Version: 0.2
Last Updated: 2026-03-09

## Environments

| Environment | URL/Endpoint | Owner | Notes |
|-------------|--------------|-------|-------|
| Dev | | | |
| Stage | | | |
| Prod | | | |

## Workstation Re-Adoption

Use this SOP when a session resumes on a different workstation, user profile, shell, or local path.

1. Confirm the current repo root path and stop trusting old absolute paths until rechecked.
2. Reconfirm the canonical local run commands from `README.md` and `ops/RUNBOOK.md`.
3. Validate the local runtime context needed for the task:
   - Python work: verify `.venv_run` health and recreate it if stale.
   - Other stacks: validate the equivalent repo-local toolchain before continuing.
4. Check `git config --get core.hooksPath` and re-enable repo-managed hooks if the project expects them.
5. Review any local overlays, machine-specific launch settings, or path-sensitive file mappings before feature work.
6. Resume only after the local environment is credible enough for `AI-runnable verification`.

## Monitoring Baseline

- Structured logs enabled
- Error tracking configured
- Basic service health checks
- No secrets/PII in logs

## Incident Severity (Simple)

- **SEV-1**: major outage/data-impacting issue
- **SEV-2**: partial outage or major feature degraded
- **SEV-3**: minor issue with workaround

## Incident Response Steps

1. Acknowledge and assign incident owner.
2. Stabilize service (rollback/feature flag/isolation).
3. Assess privacy/security impact.
4. Communicate status internally.
5. Resolve and verify.
6. Record post-incident actions in `ops/LESSONS_LEARNED.md`.

## Security/Privacy Incident Minimum Actions

- Rotate exposed secrets immediately.
- Disable compromised credentials/tokens.
- Preserve logs/evidence for review.
- Document impact, scope, and remediation.

## Backup and Restore Notes

- Backup schedule: <!-- define -->
- Restore procedure: <!-- define -->
- Last restore test date: <!-- define -->
