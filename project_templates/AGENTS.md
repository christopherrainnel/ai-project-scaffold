# Agent Rules (Read First)

> Universal entry point for AI agents in this scaffold.
> Tool-specific loaders (`CLAUDE.md`, `.github/copilot-instructions.md`) are thin front doors into the canonical policy at `ops/AI_WORKFLOW.md`.
> During active editing sessions, use the current working-tree versions of governance files; do not defer to older committed or remote copies.

## Start Here

1. Read `docs/FILE_MAP.md`.
2. Read `ops/AI_WORKFLOW.md`.
3. If the task touches paid/free or entitlement boundaries and a local overlay exists, read `guides/TIERING_POLICY.local.md` or `guides/TIERING_POLICY.md`.
4. Open only task-relevant files. Expand in small batches.
5. If you are resuming, read only the newest relevant `CHANGELOG_AI.md` entry.

If no local tiering file exists, continue normally without failing.

Use `ops/prompts/SESSION_RESUME.md` Section 1 when a session did not start with a governance-loading prompt.

## Read Triggers

- Feature, phase, public UX, entitlement, release QA, or architecture-impacting work: also read `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, and `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md`.
- Paid access, legal, privacy, or policy wording work: also read `docs/PRIVACY.md` and `docs/TERMS.md`.
- Local app or test work: use repo-local `.venv_run` and `python -m ...` commands per `ops/RUNBOOK.md`.

## Scaffold Rules

- Keep the scaffold fresh, generic, and free of carry-over history or creator-specific residue.
- Optional tiering overlays under `guides/` refine paid/free or entitlement boundary decisions when present.
- Never read or modify `.env`; only update `.env.example`.
- Never add dependencies without justification, version pinning, and lockfile update.
- Never run destructive commands or overwrite governance files without user approval.
- For legal, security, or policy guidance, use current official sources with concrete dates.
- Never claim certification or compliance without proof; use "aligned with" or "informed by".

## Closeout

- Run applicable quality gates from `ops/QUALITY_GATES.md`.
- Update `CHANGELOG_AI.md` after every task in a real project that uses this scaffold.
- Update `ops/LESSONS_LEARNED.md` for recurring issues.
- Update `docs/PRIVACY.md`, `docs/TERMS.md`, `docs/THREAT_MODEL.md`, `ops/RUNBOOK.md`, and `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md` when affected.

Reminder: in a real project created from this scaffold, a task is not done until its outcome is recorded in `CHANGELOG_AI.md`.
