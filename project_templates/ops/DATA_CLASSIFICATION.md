# Data Classification

Version: 2.0
Last Updated: {{DATE}}

> Use this guide to decide what can be shared with AI tools, logs, and repositories.

## Public

- Open-source code and docs
- Synthetic/mock datasets
- Redacted error logs
- Public API documentation

## Internal

- Non-public roadmap and pricing material
- Internal architecture and runbooks
- Aggregated analytics without direct identifiers

## Confidential

- Customer account metadata
- Non-public business contracts
- Deployment and infrastructure internals

## Regulated / Restricted (Highest)

- Secrets and credentials
- Personal data (name, email, phone, address, location, identifiers)
- Payment data (never store raw card data)
- Health, children, or other sensitive-category data
- Session tokens, auth cookies, private keys

## Handling Rules by Class

| Class | AI Sharing | Logging | Git Commit |
|------|------------|---------|------------|
| Public | Allowed | Allowed | Allowed |
| Internal | Redacted only | Minimal | Allowed with care |
| Confidential | Prefer no; redact if required | Metadata-only | Avoid unless necessary |
| Regulated/Restricted | Do not share by default | Avoid payload logging | Never commit raw values |

## Retention & Deletion

- Every collected data class must have an owner, retention period, and deletion path in `docs/PRIVACY.md`.
- If uncertain, default to shorter retention.

## Incident Response for Misclassification

1. Stop sharing immediately.
2. Revoke/rotate impacted secrets.
3. Remove exposed data from git history and logs where possible.
4. Document incident in `ops/RUNBOOK.md` and add follow-up controls.
