# AI Workflow (Canonical Policy)

Version: 1.3
Last Updated: {{DATE}}
Owner: Project Lead

---

## Purpose

This file is the **single source of truth** for how AI agents and IDE assistants operate in this repository. All other agent config files (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`) defer to this document.

Applies to: Claude Code, Cursor, VS Code Copilot, Windsurf, and any other AI-assisted tool.

---

## 1. Session Start — Audit Rule

On opening this workspace or starting the first task:

1. Verify the governance scaffold exists (see Section 8).
2. If files are missing, ask: *"This workspace is missing governance files. Should I create the missing pieces (recommended) or skip?"*
3. If approved, create only what is missing. Never overwrite existing files unless the user approves a diff.
4. At least once per major milestone, audit the scaffold for completeness.

---

## 2. Operating Mode

Every task must follow this cycle:

1. **Plan** — Describe what you will do, which files you will touch.
2. **Execute** — Make small, reviewable edits. No unrelated reformatting.
3. **Verify** — Run quality gates (lint / test / build) when available.
4. **Summarize** — State what changed, why, how it was verified, and any risks.
5. **Learn** — If the issue is likely to recur, add it to `ops/LESSONS_LEARNED.md`.
6. **Log** — Record the work in `CHANGELOG_AI.md`.

---

## 3. Safety Rules (Non-Negotiable)

| Rule | Detail |
|------|--------|
| Secrets | Never request, paste, store, or echo secrets (keys, tokens, passwords). |
| `.env` | Never read or modify `.env`. Only update `.env.example`. |
| Terminal | Never run destructive commands without explicit user approval. |
| Data | Never request customer PII or sensitive data. Use redacted/synthetic samples. |

---

## 4. Dependency Discipline

- Do not add dependencies without justification (problem it solves, why built-in code is insufficient).
- Pin exact versions in the manifest.
- Update lockfiles in the same commit.
- Run vulnerability checks (`npm audit`, `pip-audit`, etc.) when dependencies change.

---

## 5. Anti-Drift Control

Before implementing any change:

1. Read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
2. If the proposed work conflicts with documented decisions, **stop and ask**.
3. If a new architectural decision is made, log it in `docs/DECISIONS.md`.

---

## 6. Definition of Done

A task is complete only when:

- [ ] Code compiles and builds (if applicable).
- [ ] Linting passes.
- [ ] Tests pass (if applicable).
- [ ] `CHANGELOG_AI.md` is updated.
- [ ] No secrets or hardcoded credentials were introduced.
- [ ] No dependency drift (lockfiles match manifests).
- [ ] `docs/DECISIONS.md` updated if an architectural choice was made.

---

## 7. Standards and Source Quality

When work touches legal, policy, compliance, privacy, security, or licensing topics:

1. Prefer current primary sources (official docs, standards body docs, upstream project policy pages).
2. Include concrete dates when summarizing time-sensitive guidance.
3. Never claim legal compliance/certification unless explicitly provided by the user.
4. Mark guidance as non-legal advice unless a qualified professional approved it.

---

## 8. Scaffold Checklist

Required governance files:

```
CLAUDE.md                       # Claude Code auto-read rules
AGENTS.md                       # Universal agent entry point
CHANGELOG_AI.md                 # AI change log
.env.example                    # Environment variable template
.gitignore                      # Version control exclusions
.github/copilot-instructions.md # VS Code Copilot policy loader
.github/ISSUE_TEMPLATE/01-bug-report.yml
.github/ISSUE_TEMPLATE/02-feature-request.yml
.github/ISSUE_TEMPLATE/config.yml
.github/PULL_REQUEST_TEMPLATE.md
.github/CODEOWNERS
.github/BRANCH_PROTECTION.md
docs/ARCHITECTURE.md            # System design
docs/DECISIONS.md               # Decision log
docs/FILE_MAP.md                # Plain-English file index
ops/AI_WORKFLOW.md              # This file (canonical policy)
ops/SECURITY_POLICY.md          # Secret and data handling rules
ops/DATA_CLASSIFICATION.md      # Data sensitivity levels
ops/DEPENDENCY_POLICY.md        # Dependency management rules
ops/QUALITY_GATES.md            # Definition of done + commands
ops/RELEASE_CHECKLIST.md        # Release verification steps
ops/LESSONS_LEARNED.md          # Recurring issues and fixes
ops/prompts/feature_request.md  # Feature request template
ops/prompts/bug_report.md       # Bug report template
ops/prompts/refactor_request.md # Refactor request template
ops/prompts/code_review.md      # Code review template
```
