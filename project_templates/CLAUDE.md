# Project Rules (Claude Code)

> Claude Code reads this file automatically on every session.
> This is the quick-start authority file. For full policy, see `ops/AI_WORKFLOW.md`.

## Read Order

1. **This file** — essential rules and constraints.
2. `docs/FILE_MAP.md` — primary project index; use this before opening source files.
3. `ops/AI_WORKFLOW.md` — canonical workflow policy (source of truth).
4. `guides/TIERING_POLICY.local.md` (or `guides/TIERING_POLICY.md`) — optional local policy overlay for paid/free boundary decisions.
5. `docs/ARCHITECTURE.md` + `docs/DECISIONS.md` — anti-drift anchors.
6. `CHANGELOG_AI.md` — recent change history.

If no local tiering file exists, continue normally without failing.

Do not load the full codebase into context. Fetch only the files required for the current task.

## Session-Start Prompt

If the user has not provided a governance boot prompt, ask for this exact prompt before implementation work:

```text
Before anything else this session: read docs/FILE_MAP.md, AGENTS.md, and ops/AI_WORKFLOW.md -
follow the governance rules you find there. For any feature or phase work, produce a dual-lens
plan (Technical Builder POV + User/Consumer POV) and at least one risk with mitigation before
implementing. My task: [REPLACE WITH ACTUAL TASK]
```

## Non-Negotiable Rules

- **No mandatory planner**: Use a short plan and risk register only for complex/high-risk feature work.
- **Security gates before shipping**: Lint/format/typecheck/tests + dependency scan + secret scan + basic SAST must pass in CI.
- **Secrets**: Never request, paste, store, or echo secrets (keys, tokens, passwords).
- **`.env`**: Never read or modify `.env`. Only update `.env.example`.
- **Destructive commands**: Never run without explicit user approval.
- **Dependencies**: Never add without justification and version pinning.
- **Governance files**: Never overwrite without showing a diff and receiving approval.
- **Policy guidance**: For legal/security/compliance topics, use current official sources and include concrete dates.
- **Compliance wording**: Never claim certification/compliance without independent proof; use "aligned with" / "informed by".

## Product Growth Rules

- It is acceptable to create new product folders (`apps/`, `services/`, `packages/`, `infra/`, `tests/`, etc.) as needed.
- Keep governance stable by default: edit `ops/`, `.github/`, and governance docs only when required and log the rationale in `CHANGELOG_AI.md`.

## Operating Mode

1. Default flow for simple work: Build -> Review.
2. For complex/high-risk work: add a short plan before building.
3. Keep edits small and reviewable — no unrelated reformatting.
4. Run quality gates (lint/test/build) when available.
5. After changes — update `CHANGELOG_AI.md` with what changed, why, and how verified.
6. If a mistake is likely to recur — log it in `ops/LESSONS_LEARNED.md`.

## Anti-Drift

Before implementing changes, read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
If proposed work conflicts with recorded decisions, **stop and ask**.
