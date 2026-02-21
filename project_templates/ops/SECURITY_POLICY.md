# Security Policy

Version: 1.0
Last Updated: {{DATE}}

## Goal

Prevent secret leakage, unsafe command execution, and accidental exposure of sensitive data throughout the development lifecycle.

## Secret Management

| Rule | Detail |
|------|--------|
| Storage | Secrets go in `.env` (local) or a platform secret manager (production). |
| Git | `.env` is never committed. `.gitignore` enforces this. |
| Template | `.env.example` contains placeholder keys only — no real values. |
| Rotation | If a secret is accidentally committed, rotate it immediately and scrub git history. |

## Prohibited Content (Never Share in Chat, Logs, or Commits)

- API keys, tokens, passwords, or signing secrets
- Private URLs containing tokens or session IDs
- Production database exports or connection strings
- Customer PII (names, phone numbers, email addresses, payment info)
- Internal infrastructure details (IP addresses, internal hostnames)

## Terminal Safety

- Explain what a command does before running it.
- Require explicit user approval before execution.
- Never run destructive operations without confirmation (`rm -rf`, destructive migrations, `DROP TABLE`, credential changes).
- Prefer `--dry-run` flags when available for risky operations.

## Code Safety

- Never hardcode secrets — always use environment variables.
- Validate and sanitize all external input (user input, API responses).
- Use parameterized queries — never concatenate user input into SQL.
- Keep dependencies updated and run vulnerability scans regularly.

## Privacy

- Prefer privacy/telemetry-off modes where supported.
- Avoid sending proprietary code to third-party AI services unless explicitly approved.
- Minimize data collection — only request what the feature needs.
