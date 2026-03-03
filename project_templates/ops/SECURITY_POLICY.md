# Security Policy

Version: 2.0
Last Updated: {{DATE}}

## Goal

Maintain a secure-by-default baseline for MVP delivery without custom security complexity.

## Core Rules

1. **No secrets in repository or client code.**
2. **Least privilege by default.** Explicit permissions and deny-by-default access.
3. **Data minimization.** Collect and retain only what is needed for the feature.
4. **Managed services over custom crypto/auth.** Prefer proven providers.

## Secret Management

| Rule | Detail |
|------|--------|
| Storage | Secrets in `.env` (local) and managed secret store (non-local). |
| Git | `.env` is never committed. Only `.env.example` is tracked. |
| Rotation | Rotate immediately after any suspected exposure. |
| Environment split | Separate keys per dev/stage/prod. |

## Access Control

- Use explicit roles/permissions.
- Deny-by-default endpoint behavior.
- Prefer managed auth (OIDC/OAuth) when accounts are needed.
- Use short-lived tokens/sessions with secure cookie settings when applicable.

## App & API Controls

- Input validation and output encoding at all trust boundaries.
- CSRF protection when cookie auth is used.
- Secure headers: CSP, HSTS, frame protections, and MIME protections (when applicable).
- Rate limiting and abuse controls for public interfaces.
- Upload controls: MIME/type checks, size limits, private storage, malware scanning strategy.

## Data Protection

- Encrypt in transit (TLS).
- Use provider-managed encryption at rest.
- Do not log secrets or full sensitive payloads.
- Define retention/deletion in `docs/PRIVACY.md`.

## Payments Baseline

- Never process raw card number/CVV in app code.
- Use hosted checkout/tokenization with a PCI-compliant payment provider.

## AI Safety Controls (If AI Features Exist)

- Treat user prompts and uploads as hostile input.
- Isolate system/tool prompts from user content.
- Require explicit user confirmation for sensitive actions.
- Apply tool/action allowlists and safe-fail behavior.

## Prohibited Content in Chat/Logs/Commits

- API keys, tokens, passwords, private URLs with auth material
- Production database exports/connection strings
- Customer PII and regulated data unless explicitly approved and redacted
- Internal infrastructure-sensitive data (hostnames/IP topology)
