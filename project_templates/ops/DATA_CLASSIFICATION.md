# Data Classification

Version: 1.0
Last Updated: {{DATE}}

> Use this guide to determine what data can be shared with AI agents, committed to git, or discussed in chat.

## Public (Safe to Share)

- Open-source code and documentation
- Synthetic / sample / mock data
- Sanitized logs (no secrets, no PII)
- Published API documentation
- Error messages with redacted context

## Internal (Redaction Required Before Sharing)

- Internal strategy documents, pricing models, unpublished roadmaps
- Contracts and vendor terms (redact names, amounts, dates)
- Architecture diagrams with internal hostnames or IPs (redact infra details)
- Analytics data with user segments (aggregate only, no individual records)

## Prohibited (Never Share)

- Secrets: API keys, tokens, passwords, signing keys, certificates
- Customer PII: names, emails, phone numbers, addresses, payment info
- Production database dumps or connection strings
- Session tokens, JWTs, or auth cookies
- Internal IP addresses, hostnames, or infrastructure topology
- Source code of proprietary third-party systems

## What to Do If Data Is Misclassified

1. If prohibited data was shared in chat: note it immediately, do not copy or repeat it.
2. If prohibited data was committed to git: remove it, rotate any exposed secrets, and scrub git history.
3. When in doubt, treat data as **Internal** and ask the user for clarification.
