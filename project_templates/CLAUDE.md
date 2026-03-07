# Project Rules (Claude Code)

> Claude Code reads this file automatically.
> Use it together with `.claude/settings.json`. For full policy, see `ops/AI_WORKFLOW.md`.
> During active editing sessions, use the current working-tree versions of governance files.

## Claude Startup

1. Read this file.
2. Read `docs/FILE_MAP.md`.
3. Read `ops/AI_WORKFLOW.md`.
4. If the task touches paid/free or entitlement boundaries and a local overlay exists, read `guides/TIERING_POLICY.local.md` or `guides/TIERING_POLICY.md`.
5. Open only task-relevant files. If resuming, read only the newest relevant `CHANGELOG_AI.md` entry.

If no local tiering file exists, continue normally without failing.

If the session did not begin with a governance-loading prompt, use `ops/prompts/SESSION_RESUME.md` Section 1 before feature work.

Expand the read set only when triggered by the workflow:

- Feature, phase, public UX, entitlement, release QA, or architecture-impacting work: read `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, and `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md`.
- Paid access, legal, privacy, or policy wording work: read `docs/PRIVACY.md` and `docs/TERMS.md`.

## Claude-Specific Enforcement

- Respect `.claude/settings.json` deny and ask rules.
- `ops/AI_WORKFLOW.md` remains canonical if this file and the workflow ever diverge.
- This loader is intentionally thin; do not restate the full policy when the workflow file is available.

## Non-Negotiables

- Plan plus risk register before feature or phase work; use the dual-lens gate from `ops/AI_WORKFLOW.md`.
- Never read or modify `.env`; only update `.env.example`.
- Never expose secrets or run destructive commands without approval.
- Treat governance files as protected.
- Keep the scaffold fresh, generic, and free of creator-specific residue.
- Update `CHANGELOG_AI.md` after every task in a real project that uses this scaffold.

## Local Python Pattern

- Prefer repo-local `.venv_run`.
- Use `python -m ...` command forms for app start and test execution.
- If `.venv_run` points to an old path, follow the reset SOP in `README.md` and `ops/RUNBOOK.md`.
