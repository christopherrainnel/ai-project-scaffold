# Runbook (Operations Basics)

Version: 0.1
Last Updated: {{DATE}}

## Environments

| Environment | URL/Endpoint | Owner | Notes |
|-------------|--------------|-------|-------|
| Dev | | | |
| Stage | | | |
| Prod | | | |

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
