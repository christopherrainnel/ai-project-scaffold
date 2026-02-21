# Copilot Instructions (VS Code Policy Loader)

**Version:** 1.1
**Last Updated:** {{DATE}}
**Owner:** Project Lead

---

> **Canonical policy:** `ops/AI_WORKFLOW.md` is the source of truth.
> If any conflict arises between this file and `ops/AI_WORKFLOW.md`, the workflow file wins. Stop and ask the user.

## 0. Activation

On session start or first task:
1. Check if the `ops/` folder exists.
2. If missing, ask: *"This workspace is missing the governance scaffold. Should I install it?"*
3. If approved, create only missing files. Never overwrite existing ones without a diff and approval.

## 1. Operating Rules

- **Plan first**: Describe what will change before making edits.
- **Small diffs**: Make reviewable, atomic changes. No unrelated reformatting.
- **Verify**: Run lint/test/build after changes when available.
- **Log**: Update `CHANGELOG_AI.md` after every task.
- **Learn**: Record recurring issues in `ops/LESSONS_LEARNED.md`.

## 2. Safety (Non-Negotiable)

- Never request, paste, or expose secrets (keys, tokens, passwords).
- Never read or modify `.env`. Only update `.env.example`.
- Never run destructive commands without explicit user approval.
- Never add dependencies without justification and version pinning.

## 3. Anti-Drift

Before implementing changes:
1. Read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
2. If proposed work conflicts with documented decisions, **stop and ask**.

## 4. Definition of Done

- [ ] Code compiles and builds.
- [ ] Linting passes.
- [ ] Tests pass (if applicable).
- [ ] `CHANGELOG_AI.md` updated.
- [ ] No secrets or hardcoded credentials introduced.
- [ ] No dependency drift (lockfiles match manifests).

## 5. Communication

- Explain technical concepts in plain English.
- When introducing unfamiliar patterns, briefly state why the approach was chosen.
- If the user is learning, connect new concepts to ones they already know.
- For legal/security/policy guidance, prefer current official sources and include concrete dates.
