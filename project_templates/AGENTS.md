# Agent Rules (Read First)

> Universal entry point for all AI agents and IDE assistants.
> If your tool reads a specific config file (e.g., `CLAUDE.md`, `.github/copilot-instructions.md`), follow that file — it references the same canonical policy below.

## Mandatory Read Order

1. `ops/AI_WORKFLOW.md` — **canonical policy** (source of truth for all agents).
2. `docs/ARCHITECTURE.md` — system design and component map.
3. `docs/DECISIONS.md` — why things were built this way.

## Hard Constraints

- Never overwrite governance files without showing a diff and receiving approval.
- Never read or modify `.env`. Only update `.env.example`.
- Never add dependencies without justification, version pinning, and lockfile updates.
- Never run destructive commands without explicit user approval.
- For legal/security/policy recommendations, use current official sources and state the effective date.

## After Every Task

- Update `CHANGELOG_AI.md` with: date, task, files changed, verification, risks.
- If the issue is likely to recur, add it to `ops/LESSONS_LEARNED.md`.
