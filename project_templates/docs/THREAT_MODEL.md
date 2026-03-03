# Threat Model (Lightweight)

Version: 0.1
Last Updated: {{DATE}}

## Scope

- Product area: <!-- API / Web app / worker -->
- In-scope environments: <!-- local/stage/prod -->

## Critical Assets

- User identity/session
- Application data
- Secrets and credentials
- Payment/session metadata

## Trust Boundaries

- Client ↔ API
- API ↔ Database
- API ↔ Third-party services
- CI/CD ↔ Repository/Secrets

## Top Threats and Mitigations

| Threat | Example | Mitigation | Status |
|--------|---------|------------|--------|
| Injection | SQL/command/template injection | Input validation, parameterized queries, escaping | |
| Auth bypass | Broken auth/authorization | Managed auth, RBAC, deny-by-default checks | |
| Secrets exposure | Key in repo/logs | Secret scanning, `.env.example` only, redaction | |
| Data leakage | PII in logs or responses | Data minimization, no-PII logging, response filtering | |
| Abuse/DoS | Endpoint flood | Rate limits, abuse monitoring | |
| Prompt injection (AI) | User text manipulates tools | Tool allowlist, confirmation gates, context isolation | |

## Security Tests

- Unit tests for auth and permission checks
- Input validation tests at every external boundary
- CI SAST + dependency + secret scanning

## Residual Risks

- <!-- List known risks accepted for MVP and planned next step -->
