# Project Rules (Claude Code)

> Claude Code reads this file automatically on every session.
> This is the quick-start authority file. For full policy, see `ops/AI_WORKFLOW.md`.

## Read Order

1. **This file** — essential rules and constraints.
2. `ops/AI_WORKFLOW.md` — canonical workflow policy (source of truth).
3. `docs/ARCHITECTURE.md` + `docs/DECISIONS.md` — anti-drift anchors.
4. `CHANGELOG_AI.md` — recent change history.

## Non-Negotiable Rules

- **Secrets**: Never request, paste, store, or echo secrets (keys, tokens, passwords).
- **`.env`**: Never read or modify `.env`. Only update `.env.example`.
- **Destructive commands**: Never run without explicit user approval.
- **Dependencies**: Never add without justification and version pinning.
- **Governance files**: Never overwrite without showing a diff and receiving approval.
- **Policy guidance**: For legal/security/compliance topics, use current official sources and include concrete dates.

## Operating Mode

1. Plan first — name files to change, describe the approach.
2. Small, reviewable edits — no unrelated reformatting.
3. Run quality gates (lint/test/build) when available.
4. After changes — update `CHANGELOG_AI.md` with what changed, why, and how verified.
5. If a mistake is likely to recur — log it in `ops/LESSONS_LEARNED.md`.

## Anti-Drift

Before implementing changes, read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
If proposed work conflicts with recorded decisions, **stop and ask**.
