# Agent Rules (Read First)

> Universal entry point for all AI agents and IDE assistants.
> If your tool reads a specific config file (e.g., `CLAUDE.md`, `.github/copilot-instructions.md`), follow that file — it references the same canonical policy below.

## Mandatory Read Order

1. `docs/FILE_MAP.md` — primary project index; use this first for fast orientation.
2. `ops/AI_WORKFLOW.md` — **canonical policy** (source of truth for all agents).
3. `guides/TIERING_POLICY.local.md` (or `guides/TIERING_POLICY.md`) — optional local policy overlay for paid/free boundary decisions.
4. `docs/ARCHITECTURE.md` — system design and component map.
5. `docs/DECISIONS.md` — why things were built this way.

If no local tiering file exists, continue normally without failing.

Do not preload the full codebase. Fetch only files needed for the current task.

## Session Start - Required User Action

Have the user paste this at session start (also in `ops/prompts/SESSION_RESUME.md`, Section 1):

```text
Before anything else this session: read docs/FILE_MAP.md, AGENTS.md, and ops/AI_WORKFLOW.md -
follow the governance rules you find there. For any feature or phase work, produce a dual-lens
plan (Technical Builder POV + User/Consumer POV) and at least one risk with mitigation before
implementing. My task: [REPLACE WITH ACTUAL TASK]
```

## Hard Constraints

- Single-agent mode is default. Multi-agent behavior is optional.
- No mandatory planner: use a short plan + risk register only for complex/high-risk tasks.
- CI gates must include lint/format/typecheck/tests/dependency scan/secret scan/basic SAST before shipping.
- Never overwrite governance files without showing a diff and receiving approval.
- Never read or modify `.env`. Only update `.env.example`.
- Never add dependencies without justification, version pinning, and lockfile updates.
- Never run destructive commands without explicit user approval.
- For legal/security/policy recommendations, use current official sources and state the effective date.
- Never claim compliance/certification. Use wording such as "aligned with" or "informed by".

## After Every Task

- Update `CHANGELOG_AI.md` with: date, task, files changed, verification, risks.
- If the issue is likely to recur, add it to `ops/LESSONS_LEARNED.md`.
- Update `docs/PRIVACY.md` / `docs/THREAT_MODEL.md` / `ops/RUNBOOK.md` when changes affect those areas.
