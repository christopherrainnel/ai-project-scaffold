# Copilot Instructions (VS Code Policy Loader)

**Version:** 2.4
**Last Updated:** 2026-03-07
**Owner:** Project Lead

---

> Canonical policy: `ops/AI_WORKFLOW.md`.
> If this file conflicts with the workflow, the workflow wins and the agent should stop and ask.
>
> Copilot instructions are supplemental. Native rule and hook systems remain stronger where supported.

## Activation

On session start or first task:
1. Check that the `ops/` folder exists.
2. Read `docs/FILE_MAP.md`.
3. Read `ops/AI_WORKFLOW.md`.
4. If the task touches paid/free or entitlement boundaries and a local overlay exists, read `guides/TIERING_POLICY.local.md` or `guides/TIERING_POLICY.md`.
5. Load only task-relevant files. If resuming, read only the newest relevant `CHANGELOG_AI.md` entry.
6. If governance files are missing, ask to create only the missing ones.

If no local tiering file exists, continue normally without failing.

Use `ops/prompts/SESSION_RESUME.md` Section 1 when a governance-loading first prompt is needed.

## Copilot Loader Rules

- During active editing sessions, treat the current working-tree governance files as authoritative.
- Keep initial context small; start with at most 3 source files unless the task clearly needs more.
- For feature or phase work, follow the dual-lens plan plus risk-register requirement from `ops/AI_WORKFLOW.md`.
- For architecture-impacting work, read `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, and `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md` before implementing.
- For paid access, legal, privacy, or policy wording work, read `docs/PRIVACY.md` and `docs/TERMS.md` before implementing.
- Keep the scaffold fresh, generic, and free of creator-specific residue.

## Safety

- Never request, paste, or expose secrets.
- Never read or modify `.env`; only update `.env.example`.
- Never run destructive commands without explicit user approval.
- Never add dependencies without justification, version pinning, and lockfile updates.
- Never claim certification or compliance without proof.

## Closeout

- Run the applicable checks from `ops/QUALITY_GATES.md`.
- Update `CHANGELOG_AI.md` after every task in a real project that uses this scaffold.
- Log recurring failures in `ops/LESSONS_LEARNED.md`.
- Treat governance files as protected and edit them only when necessary.
