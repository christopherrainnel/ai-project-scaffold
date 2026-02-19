# Security Policy
Version: 1.0
Last Updated: 2026-02-19

## Goals
Prevent secret leakage, unsafe command execution, and accidental inclusion of sensitive data.

## Secrets
- Store secrets ONLY in `.env` (local) or platform secret managers.
- Never commit `.env`.
- Maintain `.env.example` with placeholder keys only.

## Prohibited Content in Chat/Logs
- API keys, tokens, passwords
- Private URLs containing tokens
- Production database exports
- Customer PII (names, phone, email, payment info)

## Terminal Safety
- Commands must be explained before execution.
- Require explicit user approval before running commands.
- Never run destructive operations without confirmation (rm -rf, destructive migrations, credential changes).

## Telemetry/Privacy
- Prefer privacy modes where supported.
- Avoid sending proprietary code snippets to third-party services unnecessarily.
