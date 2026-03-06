# Copilot Instructions (VS Code Policy Loader)

**Version:** 2.0
**Last Updated:** {{DATE}}
**Owner:** Project Lead

---

> **Canonical policy:** `ops/AI_WORKFLOW.md` is the source of truth.
> If any conflict arises between this file and `ops/AI_WORKFLOW.md`, the workflow file wins. Stop and ask the user.

## 0. Activation

On session start or first task:
1. Check if the `ops/` folder exists.
2. Read `docs/FILE_MAP.md` first to orient quickly before loading source files.
3. Read `guides/TIERING_POLICY.local.md` (or `guides/TIERING_POLICY.md`) if present for local tiering boundary rules.
4. If the user has not started with a governance-loading first message, point them to `ops/prompts/SESSION_RESUME.md` Section 1 for the full recommended prompt before implementation work.

5. If missing, ask: *"This workspace is missing the governance scaffold. Should I install it?"*
6. If approved, create only missing files. Never overwrite existing ones without a diff and approval.

If no local tiering file exists, continue normally without failing.

Context efficiency rule:
- Do not preload the full codebase.
- Load only task-relevant files.
- Never load more than 3 source files per task unless explicitly required.

## 1. Operating Rules

- **Default flow (simple work)**: Build -> Review.
- **Planning for complex/high-risk work**: Add a short plan and risk register when complexity or risk justifies it.
- **Small diffs**: Make reviewable, atomic changes. No unrelated reformatting.
- **Verify**: Run lint/test/build after changes when available.
- **Log**: Update `CHANGELOG_AI.md` after every task.
- **Learn**: Record recurring issues in `ops/LESSONS_LEARNED.md`.

## 2. Safety (Non-Negotiable)

- Never request, paste, or expose secrets (keys, tokens, passwords).
- Never read or modify `.env`. Only update `.env.example`.
- Never run destructive commands without explicit user approval.
- Never add dependencies without justification and version pinning.
- Never claim certification/compliance without independent proof; use "aligned with" or "informed by".

## 3. Anti-Drift

Before implementing changes:
1. Read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
2. If proposed work conflicts with documented decisions, **stop and ask**.

## 4. Definition of Done

- [ ] Code compiles/builds (if applicable).
- [ ] Lint/format/typecheck pass.
- [ ] Tests pass.
- [ ] `CHANGELOG_AI.md` updated.
- [ ] No secrets or hardcoded credentials introduced.
- [ ] No dependency drift (lockfiles match manifests).
- [ ] Dependency scan, secret scan, and basic SAST pass in CI.

## 5. Growth & Governance

- Create product folders as needed (`apps/`, `services/`, `packages/`, `infra/`, `tests/`, etc.).
- Treat governance files as protected; edit only when needed and with rationale logged.

## 6. Communication

- Explain technical concepts in plain English.
- When introducing unfamiliar patterns, briefly state why the approach was chosen.
- If the user is learning, connect new concepts to ones they already know.
- For legal/security/policy guidance, prefer current official sources and include concrete dates.
