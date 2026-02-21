#!/usr/bin/env python3
"""
Project Governance Scaffold Generator
======================================
Creates the standard governed project structure with all governance files,
documentation, prompt templates, and configuration for AI-assisted development.

Usage:
    python scaffold_project.py                      # create ./project_template/ and scaffold
    python scaffold_project.py /path/to/workspace  # create /path/to/workspace/project_template/
    python scaffold_project.py --name my-project   # create ./my-project/ and scaffold
    python scaffold_project.py --dry-run            # preview without writing
    python scaffold_project.py --force              # overwrite existing files

Default behavior is safe: existing files are skipped unless --force is used.
"""

import sys
import argparse
from pathlib import Path
from datetime import date

TODAY = date.today().strftime("%Y-%m-%d")
DEFAULT_PROJECT_FOLDER = "project_template"

# ---------------------------------------------------------------------------
# Template placeholders:
#   {{DATE}}          -> replaced with today's date at generation time
#   {{PROJECT_NAME}}  -> replaced with --name value (or "My Project")
# ---------------------------------------------------------------------------

FILES = {
".env.example": """\
# Environment Variables
# Copy this file to .env and fill in your values.
# NEVER commit .env — it is excluded by .gitignore.

# ── Application ──────────────────────────────────────────
# NODE_ENV=development
# PORT=3000

# ── Secrets ──────────────────────────────────────────────
# API_KEY=
# DATABASE_URL=
# AUTH_SECRET=

# ── Third-Party Services ─────────────────────────────────
# STRIPE_KEY=
# SENDGRID_API_KEY=
# AWS_ACCESS_KEY_ID=
# AWS_SECRET_ACCESS_KEY=

""",

".github/BRANCH_PROTECTION.md": """\
# Branch Protection Checklist (`main`)

Use this checklist in GitHub repository settings to enforce safe merges.

## Recommended Minimum

- [ ] Require a pull request before merging.
- [ ] Require at least 1 approving review.
- [ ] Dismiss stale approvals when new commits are pushed.
- [ ] Require status checks to pass before merging.
- [ ] Require branches to be up to date before merging.
- [ ] Include administrators in these rules.
- [ ] Restrict direct pushes to `main`.

## Status Checks to Require

- [ ] CI test workflow for your supported OS/runtime matrix

## Optional (Recommended for Growth)

- [ ] Require conversation resolution before merging.
- [ ] Require signed commits.
- [ ] Require linear history.
- [ ] Restrict who can dismiss pull request reviews.
- [ ] Enforce DCO sign-off checks if you want explicit per-commit contributor certification.

""",

".github/CODEOWNERS": """\
# TODO: Replace with your GitHub username/org team
* @your-github-handle

""",

".github/copilot-instructions.md": """\
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

""",

".github/ISSUE_TEMPLATE/01-bug-report.yml": """\
name: Bug report
description: Report a reproducible problem to help us improve the project.
title: "[Bug]: "
labels:
  - bug
body:
  - type: markdown
    attributes:
      value: |
        Thanks for filing a bug report.
        Please do not include secrets, tokens, passwords, or private user data.
  - type: textarea
    id: summary
    attributes:
      label: Summary
      description: What happened and what did you expect?
      placeholder: Concise description of the problem and expected behavior.
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Reproduction steps
      description: Provide exact steps so maintainers can reproduce quickly.
      placeholder: |
        1. Go to ...
        2. Run ...
        3. See error ...
    validations:
      required: true
  - type: input
    id: environment
    attributes:
      label: Environment
      description: OS, runtime, browser, and relevant versions.
      placeholder: Windows 11, Python 3.12, Chrome 123
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Logs or screenshots (redacted)
      description: Paste only redacted logs. Never include secrets.
      render: shell
  - type: checkboxes
    id: checks
    attributes:
      label: Pre-submission checks
      options:
        - label: I searched existing issues and did not find a duplicate.
          required: true
        - label: I redacted sensitive information from logs/screenshots.
          required: true
        - label: This is not a security vulnerability report.
          required: true

""",

".github/ISSUE_TEMPLATE/02-feature-request.yml": """\
name: Feature request
description: Suggest an improvement with clear use case and acceptance criteria.
title: "[Feature]: "
labels:
  - enhancement
body:
  - type: markdown
    attributes:
      value: |
        Thanks for suggesting an improvement.
        Clear outcomes and constraints help maintainers prioritize effectively.
  - type: textarea
    id: problem
    attributes:
      label: Problem statement
      description: What problem are you trying to solve?
      placeholder: Describe the current limitation and who is affected.
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposed solution
      description: What should change?
      placeholder: Describe the behavior, API, or workflow you want.
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives considered
      description: What other options did you evaluate?
  - type: textarea
    id: acceptance
    attributes:
      label: Acceptance criteria
      description: How should we verify this is complete?
      placeholder: |
        - [ ] Criterion 1
        - [ ] Criterion 2
    validations:
      required: true
  - type: checkboxes
    id: checks
    attributes:
      label: Pre-submission checks
      options:
        - label: I searched existing issues and did not find a duplicate.
          required: true
        - label: I explained user impact and success criteria.
          required: true

""",

".github/ISSUE_TEMPLATE/config.yml": """\
blank_issues_enabled: false

""",

".github/PULL_REQUEST_TEMPLATE.md": """\
## Summary

Describe what changed and why.

## Changes

- 

## Verification

List the commands or checks you ran.

```bash
# Example:
# npm test
# npm run lint
```

## Governance Checks

- [ ] I updated `CHANGELOG_AI.md` (if AI-assisted changes were made).
- [ ] I updated `docs/DECISIONS.md` if an architectural decision changed.
- [ ] I did not include secrets or sensitive data.
- [ ] I kept the diff focused and avoided unrelated formatting changes.
- [ ] I agree this contribution is submitted under the repository license in `LICENSE`.
- [ ] I understand contributions are voluntary and unpaid unless separately agreed in writing.

## Related Issues

Closes #

""",

".gitignore": """\
# Secrets
.env
.env.*
!.env.example

# OS / Editor
.DS_Store
Thumbs.db
*.swp
*.swo
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json
!.vscode/launch.json
.idea/
*.iml

# Logs
*.log
npm-debug.log*
yarn-debug.log*
pnpm-debug.log*

# Build / cache (common)
dist/
build/
out/
.cache/
tmp/
temp/

# Node (common web)
node_modules/
.next/
.vercel/
coverage/

# Python (common data)
__pycache__/
*.py[cod]
.venv/
venv/
.ipynb_checkpoints/

# Excel/VBA exports/backups
~$*.xls*
*.tmp

""",

"AGENTS.md": """\
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

""",

"CHANGELOG_AI.md": """\
# AI Change Log

> Every AI-made change is recorded here. Entries are newest-first.

## Entry Format

```
### YYYY-MM-DD — [Short task description]
**Files**: list of files changed
**Commands**: commands run (or "none")
**Verification**: how the change was verified
**Notes/Risks**: anything to watch out for
```

---

### {{DATE}} — Project scaffold created

**Files**: All governance, docs, and config files.
**Commands**: `python scaffold_project.py` (or manual setup)
**Verification**: Manual review of generated files.
**Notes/Risks**: Initial baseline. Fill in `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` next.

---

<!-- Add new entries above this line, newest first -->

""",

"CLAUDE.md": """\
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

""",

"docs/ARCHITECTURE.md": """\
# Architecture

Version: 0.1
Last Updated: {{DATE}}

> Fill this in when starting the project. AI agents read this before making changes to prevent architectural drift.

## Overview

<!-- Describe the system in 2-3 sentences. What does it do? Who uses it? -->

## Tech Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Frontend | | |
| Backend / API | | |
| Database | | |
| Hosting | | |
| Auth | | |

## Components

<!-- List the major parts of the system and what each one does. -->

- **UI**:
- **API**:
- **Data layer**:
- **External integrations**:

## Data Flow

<!-- Describe how data moves through the system. A simple text diagram works. -->

```
User -> [Frontend] -> [API] -> [Database]
                   -> [External Service]
```

## Security Boundaries

<!-- Where do secrets live? Where does authentication happen? What is publicly accessible? -->

- Secrets: stored in `.env` locally, platform secret manager in production.
- Auth:
- Public surface:

## Environments

| Environment | URL / Access | Notes |
|-------------|-------------|-------|
| Local | `localhost:XXXX` | |
| Staging | | |
| Production | | |

""",

"docs/DECISIONS.md": """\
# Decisions Log

Version: 0.1
Last Updated: {{DATE}}

> Record every significant decision here. AI agents check this before proposing changes.
> If a proposed change conflicts with a recorded decision, the agent must stop and ask.

## Entry Format

```
### YYYY-MM-DD — [Short title of the decision]
**Decision**: What was decided.
**Why**: The reasoning behind it.
**Alternatives considered**: What else was evaluated.
**Tradeoffs**: What you gain and what you give up.
```

---

### {{DATE}} — Governance scaffold adopted

**Decision**: Use a standardized governance scaffold for AI-assisted development.
**Why**: Reduce architectural drift, improve auditability, enforce secure defaults from day one.
**Alternatives considered**: Ad-hoc instructions per project; no governance at all.
**Tradeoffs**: Small upfront setup time; large reduction in long-term risk and rework.

---

<!-- Add new decisions above this line, newest first -->

""",

"docs/FILE_MAP.md": """\
# File Map

> Plain-English guide to what every file and folder does.
> Update this as the project grows so any contributor (human or AI) can orient quickly.

## Root Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview, quick start, and key rules |
| `CLAUDE.md` | Auto-loaded rules for Claude Code sessions |
| `AGENTS.md` | Universal entry point for all AI agents |
| `CHANGELOG_AI.md` | Running log of every AI-made change |
| `.env.example` | Template for environment variables (never commit `.env`) |
| `.gitignore` | Keeps secrets, build artifacts, and OS files out of version control |

## `docs/` — Project Knowledge

| File | Purpose |
|------|---------|
| `ARCHITECTURE.md` | High-level system design, components, data flow |
| `DECISIONS.md` | Decision log — what was chosen, why, and what was rejected |
| `FILE_MAP.md` | This file — plain-English index of the entire project |

## `ops/` — Governance and Workflow

| File | Purpose |
|------|---------|
| `AI_WORKFLOW.md` | **Canonical policy** — the single source of truth for AI agent behavior |
| `SECURITY_POLICY.md` | Rules for secrets, data handling, and terminal safety |
| `DATA_CLASSIFICATION.md` | What data can be shared, what must be redacted, what is prohibited |
| `DEPENDENCY_POLICY.md` | Rules for adding, pinning, and auditing dependencies |
| `QUALITY_GATES.md` | Definition of done + stack-specific commands (lint, test, build) |
| `RELEASE_CHECKLIST.md` | Pre-release and post-release verification steps |
| `LESSONS_LEARNED.md` | Recurring mistakes and their fixes — grows over time |

## `ops/prompts/` — Reusable Agent Prompts

| File | Purpose |
|------|---------|
| `feature_request.md` | Structured template for requesting new features |
| `bug_report.md` | Structured template for reporting and fixing bugs |
| `refactor_request.md` | Structured template for refactoring tasks |
| `code_review.md` | Structured template for AI-assisted code reviews |

## `.github/` — Repository Automation and Contribution UX

| File | Purpose |
|------|---------|
| `copilot-instructions.md` | VS Code Copilot policy loader — references `ops/AI_WORKFLOW.md` |
| `ISSUE_TEMPLATE/01-bug-report.yml` | Structured bug intake form for consistent, reproducible reports |
| `ISSUE_TEMPLATE/02-feature-request.yml` | Structured feature request form with acceptance criteria |
| `ISSUE_TEMPLATE/config.yml` | Issue template config (disables blank issues by default) |
| `PULL_REQUEST_TEMPLATE.md` | Standard pull request checklist and verification prompt |
| `CODEOWNERS` | Default code ownership and required reviewer routing |
| `BRANCH_PROTECTION.md` | Checklist for configuring branch protection in GitHub settings |

## `scripts/` — Automation

Utility scripts for setup, builds, or deployment. Add scripts here as the project grows.

""",

"ops/AI_WORKFLOW.md": """\
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

""",

"ops/DATA_CLASSIFICATION.md": """\
# Data Classification

Version: 1.0
Last Updated: {{DATE}}

> Use this guide to determine what data can be shared with AI agents, committed to git, or discussed in chat.

## Public (Safe to Share)

- Open-source code and documentation
- Synthetic / sample / mock data
- Sanitized logs (no secrets, no PII)
- Published API documentation
- Error messages with redacted context

## Internal (Redaction Required Before Sharing)

- Internal strategy documents, pricing models, unpublished roadmaps
- Contracts and vendor terms (redact names, amounts, dates)
- Architecture diagrams with internal hostnames or IPs (redact infra details)
- Analytics data with user segments (aggregate only, no individual records)

## Prohibited (Never Share)

- Secrets: API keys, tokens, passwords, signing keys, certificates
- Customer PII: names, emails, phone numbers, addresses, payment info
- Production database dumps or connection strings
- Session tokens, JWTs, or auth cookies
- Internal IP addresses, hostnames, or infrastructure topology
- Source code of proprietary third-party systems

## What to Do If Data Is Misclassified

1. If prohibited data was shared in chat: note it immediately, do not copy or repeat it.
2. If prohibited data was committed to git: remove it, rotate any exposed secrets, and scrub git history.
3. When in doubt, treat data as **Internal** and ask the user for clarification.

""",

"ops/DEPENDENCY_POLICY.md": """\
# Dependency Policy

Version: 1.0
Last Updated: {{DATE}}

## Default Stance

Prefer built-in solutions. Every dependency is a maintenance and security liability. Only add one when the cost of writing it yourself clearly outweighs the cost of the dependency.

## Before Adding a Dependency

Answer these questions:

1. **What problem does it solve?**
2. **Can this be done with built-in language/framework features?**
3. **Is the package actively maintained?** (Check: last commit, open issues, bus factor)
4. **What is the license?** (Avoid GPL in proprietary projects; MIT/Apache-2.0 preferred)
5. **What is the install size and dependency tree?** (Avoid packages that pull in hundreds of sub-dependencies)

## Rules

- **Pin exact versions** in the manifest (`package.json`, `requirements.txt`, `pyproject.toml`).
- **Update lockfiles** in the same commit as the dependency change.
- **Run vulnerability scans** after adding or updating dependencies:
  - Node: `npm audit` or `pnpm audit`
  - Python: `pip-audit` or `safety check`
- **Document the justification** in the commit message or in `docs/DECISIONS.md` for significant additions.

## Removing Dependencies

Periodically review for unused packages:
- Node: `npx depcheck`
- Python: `pip-extra-reqs` or manual review

Remove anything that is no longer imported or used.

""",

"ops/LESSONS_LEARNED.md": """\
# Lessons Learned

> Log recurring mistakes and their fixes here. Only add entries that are likely to happen again.
> Keep entries short and actionable. This is not a general journal — it is a reference for avoiding repeat errors.

## Format

```
### YYYY-MM-DD — Short title
**Problem**: What went wrong.
**Root cause**: Why it happened.
**Fix**: What resolved it.
**Prevention**: How to avoid it next time.
```

---

<!-- Add entries below this line -->

""",

"ops/prompts/bug_report.md": """\
# Bug Report

> Copy this template and fill it in before handing the task to an AI agent.

## Symptom

What is broken? Include exact error text (redacted if it contains secrets).

- Error message:
- Where it happens:
- Frequency (always / intermittent / once):

## Reproduction Steps

1.
2.
3.

## Expected vs Actual

- **Expected**: What should happen.
- **Actual**: What happens instead.

## Environment

- OS:
- Runtime version (Node, Python, etc.):
- Browser (if applicable):
- Relevant config (no secrets):

## Suspected Cause (Optional)

If you have a theory, note it here. The agent will investigate.

## Fix Verification

- [ ] Bug no longer reproduces after the fix
- [ ] Tests added to prevent regression
- [ ] No new errors introduced
- [ ] `CHANGELOG_AI.md` updated

Commands to verify:

```
# lint, test — fill in per your stack
```

""",

"ops/prompts/code_review.md": """\
# Code Review (Agent Task)

## Scope

What files or modules should be reviewed?
- Files:
- Focus area (security / performance / readability / all):

## Review Checklist

- [ ] No hardcoded secrets or credentials
- [ ] Error handling is present and meaningful
- [ ] No unused imports, variables, or dead code
- [ ] Functions are focused (single responsibility)
- [ ] Naming is clear and consistent
- [ ] Edge cases are handled (null, empty, unexpected input)
- [ ] Dependencies added are justified and version-pinned

## What to Flag

- Security risks (injection, exposed secrets, missing validation)
- Performance issues (unnecessary loops, missing pagination, large payloads)
- Maintainability concerns (deeply nested logic, magic numbers, unclear naming)
- Missing tests for critical paths

## Output Format

For each issue found:
```
File: <path>
Line: <number>
Severity: critical | warning | suggestion
Issue: <description>
Fix: <recommended change>
```

""",

"ops/prompts/feature_request.md": """\
# Feature Request

> Copy this template and fill it in before handing the task to an AI agent.

## Context

What is the current system/product? What exists today?

- Product:
- Current behavior:
- Relevant files:

## Objective

What should change? What does success look like?

- Desired behavior:
- User story: *As a [user], I want [feature] so that [benefit].*

## Constraints

- Security / compliance:
- Performance:
- UI / UX:
- Must not break:

## Acceptance Criteria

- [ ] Feature works as described in the objective
- [ ] No regressions in existing functionality
- [ ] Tests added for new behavior
- [ ] `CHANGELOG_AI.md` updated
- [ ] `docs/DECISIONS.md` updated (if an architectural choice was made)

## Verification

Commands to run after implementation:

```
# lint, test, build — fill in per your stack
```

""",

"ops/prompts/refactor_request.md": """\
# Refactor Request

> Copy this template and fill it in before handing the task to an AI agent.

## Goal

What improvement is needed? (Pick one or more: readability, performance, modularity, testability, removing duplication)

- Target:
- Files / modules affected:

## Non-Goals

What must NOT change? (Be explicit — this prevents scope creep.)

-
-

## Constraints

- Existing behavior must be preserved unless explicitly stated otherwise.
- Avoid large formatting-only changes — keep diffs reviewable.
- If the refactor touches shared utilities, verify all consumers still work.

## Verification

- [ ] All existing tests still pass
- [ ] Lint passes
- [ ] No behavior change (unless explicitly intended)
- [ ] `CHANGELOG_AI.md` updated

Commands to verify:

```
# lint, test, build — fill in per your stack
```

""",

"ops/QUALITY_GATES.md": """\
# Quality Gates

Version: 1.0
Last Updated: {{DATE}}

## Definition of Done

A task is not complete until all applicable items pass:

- [ ] Code compiles / builds without errors
- [ ] Linting passes without errors
- [ ] Tests pass (unit, integration as applicable)
- [ ] `CHANGELOG_AI.md` updated with the change
- [ ] No secrets or hardcoded credentials introduced
- [ ] No dependency drift (lockfiles match manifests)
- [ ] `docs/DECISIONS.md` updated if an architectural choice was made

## Project Commands

> Fill these in when you choose your tech stack. AI agents will use these to verify their work.

| Action | Command |
|--------|---------|
| Install | |
| Lint | |
| Format | |
| Test | |
| Build | |
| Audit (deps) | |
| Dev server | |

### Common Stacks (Reference)

**Node.js / Next.js**
```
Install:  npm install
Lint:     npx eslint .
Format:   npx prettier --check .
Test:     npx jest  (or: npx vitest)
Build:    npm run build
Audit:    npm audit
Dev:      npm run dev
```

**Python / FastAPI / Django**
```
Install:  pip install -r requirements.txt
Lint:     ruff check .
Format:   ruff format --check .
Test:     pytest
Build:    (not applicable for most Python projects)
Audit:    pip-audit
Dev:      uvicorn main:app --reload  (or: python manage.py runserver)
```

""",

"ops/RELEASE_CHECKLIST.md": """\
# Release Checklist

Version: 1.0
Last Updated: {{DATE}}

## Pre-Release

- [ ] All quality gates pass (lint, test, build)
- [ ] No secrets or credentials in the codebase (Unix: `git log --all -p --pretty=format: | grep -Ei "password|secret|api[_-]?key"` / PowerShell: `git log --all -p --pretty=format: | Select-String -Pattern "(?i)password|secret|api[_-]?key"`)
- [ ] Dependency changes reviewed and vulnerability-scanned
- [ ] `CHANGELOG_AI.md` is up to date
- [ ] `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` reflect current state
- [ ] Key user flows smoke-tested manually
- [ ] Environment variables documented in `.env.example`
- [ ] Rollback plan documented (for production releases)
- [ ] Database migrations tested (if applicable)
- [ ] Feature flags configured (if applicable)

## Release

- [ ] Tag the release in git (`git tag vX.Y.Z`)
- [ ] Deploy to staging and verify
- [ ] Deploy to production
- [ ] Verify production health (logs, monitoring, key flows)

## Post-Release

- [ ] Monitor error rates and logs for 30 minutes after deploy
- [ ] Confirm rollback plan is still viable
- [ ] Notify stakeholders of the release
- [ ] Close related issues / tickets
- [ ] Archive the release branch (if applicable)
- [ ] Update `ops/LESSONS_LEARNED.md` if anything unexpected happened

""",

"ops/SECURITY_POLICY.md": """\
# Security Policy

Version: 1.0
Last Updated: {{DATE}}

## Goal

Prevent secret leakage, unsafe command execution, and accidental exposure of sensitive data throughout the development lifecycle.

## Secret Management

| Rule | Detail |
|------|--------|
| Storage | Secrets go in `.env` (local) or a platform secret manager (production). |
| Git | `.env` is never committed. `.gitignore` enforces this. |
| Template | `.env.example` contains placeholder keys only — no real values. |
| Rotation | If a secret is accidentally committed, rotate it immediately and scrub git history. |

## Prohibited Content (Never Share in Chat, Logs, or Commits)

- API keys, tokens, passwords, or signing secrets
- Private URLs containing tokens or session IDs
- Production database exports or connection strings
- Customer PII (names, phone numbers, email addresses, payment info)
- Internal infrastructure details (IP addresses, internal hostnames)

## Terminal Safety

- Explain what a command does before running it.
- Require explicit user approval before execution.
- Never run destructive operations without confirmation (`rm -rf`, destructive migrations, `DROP TABLE`, credential changes).
- Prefer `--dry-run` flags when available for risky operations.

## Code Safety

- Never hardcode secrets — always use environment variables.
- Validate and sanitize all external input (user input, API responses).
- Use parameterized queries — never concatenate user input into SQL.
- Keep dependencies updated and run vulnerability scans regularly.

## Privacy

- Prefer privacy/telemetry-off modes where supported.
- Avoid sending proprietary code to third-party AI services unless explicitly approved.
- Minimize data collection — only request what the feature needs.

""",

"README.md": """\
# {{PROJECT_NAME}}

> Built with AI-assisted development using a governed scaffold.

## Quick Start

1. Clone this repo and open it in your IDE (Cursor, VS Code, or any AI-enabled editor).
2. Copy `.env.example` to `.env` and fill in your values.
3. Read `ops/AI_WORKFLOW.md` — this is the source of truth for how AI agents work in this project.
4. Fill in `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` with your project specifics.

## Project Structure

```
docs/           Architecture, decisions, and file map
ops/            Governance policies, workflow rules, prompt templates
ops/prompts/    Reusable prompt templates for common tasks
scripts/        Utility and automation scripts
```

See `docs/FILE_MAP.md` for a plain-English guide to every file.

## For AI Agents

Start with `AGENTS.md` (or `CLAUDE.md` for Claude Code). These files point to the canonical policy in `ops/AI_WORKFLOW.md`.

## Key Rules

- Never commit `.env` — only `.env.example` is tracked.
- All AI changes are logged in `CHANGELOG_AI.md`.
- Decisions and their rationale go in `docs/DECISIONS.md`.

## Maturity and Improvement

This scaffold provides strong governance defaults, but it may not yet match the ecosystem maturity of older, large frameworks or tooling ecosystems.

Improvement is continuous and is led by maintainers together with approved contributors through reviewed pull requests.

## Feedback and Community

If this template helps your project, please use it and share constructive feedback.

- Use issues for bugs and feature requests.
- Use pull requests for improvements.
- Keep feedback specific, respectful, and actionable so the author and community can improve quickly.

## Contribution Terms

By submitting contributions, contributors agree the work is provided under the repository `LICENSE`, with no expectation of payment unless separately agreed in writing by maintainers.

""",

"scripts/.gitkeep": """\

""",

}


# ---------------------------------------------------------------------------
# Color output helpers (works on most terminals including Windows 10+)
# ---------------------------------------------------------------------------

def _supports_color():
    """Check if the terminal supports ANSI colors."""
    if sys.platform == "win32":
        # Windows 10+ supports ANSI if VIRTUAL_TERMINAL_PROCESSING is enabled
        # or if running in Windows Terminal / modern shells
        import os
        return os.environ.get("WT_SESSION") or os.environ.get("TERM_PROGRAM")
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

USE_COLOR = _supports_color()

def _c(code, text):
    """Wrap text in ANSI color codes if supported."""
    if USE_COLOR:
        return f"\033[{code}m{text}\033[0m"
    return text

def green(text):  return _c("32", text)
def yellow(text): return _c("33", text)
def cyan(text):   return _c("36", text)
def bold(text):   return _c("1", text)
def dim(text):    return _c("2", text)

# ---------------------------------------------------------------------------
# Generator logic
# ---------------------------------------------------------------------------

def resolve_placeholders(content: str, project_name: str) -> str:
    """Replace template placeholders with actual values."""
    content = content.replace("{{DATE}}", TODAY)
    content = content.replace("{{PROJECT_NAME}}", project_name)
    return content


def create_scaffold(
    target_dir: Path,
    project_name: str,
    dry_run: bool = False,
    force: bool = False,
):
    """Create the full project scaffold under target_dir."""
    target_dir = target_dir.resolve()
    created_dirs = set()
    created_files = []
    skipped_files = []

    for rel_path, content in FILES.items():
        full_path = target_dir / rel_path
        parent = full_path.parent

        # Create directories
        if parent not in created_dirs and not parent.exists():
            if dry_run:
                print(f"  {cyan('[DIR]')}  {parent.relative_to(target_dir)}/")
            else:
                parent.mkdir(parents=True, exist_ok=True)
            created_dirs.add(parent)

        # Write file
        if full_path.exists() and not force:
            skipped_files.append(rel_path)
            if dry_run:
                print(f"  {dim('[SKIP]')} {rel_path}  {dim('(already exists)')}")
            continue

        resolved = resolve_placeholders(content, project_name)

        if dry_run:
            print(f"  {green('[FILE]')} {rel_path}")
        else:
            full_path.write_text(resolved, encoding="utf-8")
        created_files.append(rel_path)

    return created_files, skipped_files


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a governed AI project with docs, policies, and prompt templates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  python scaffold_project.py                      # create ./project_template/ and scaffold
  python scaffold_project.py /path/to/workspace   # create /path/to/workspace/project_template/
  python scaffold_project.py --name my-project    # create ./my-project/ and scaffold
  python scaffold_project.py --dry-run            # preview without writing files
  python scaffold_project.py --force              # overwrite existing files
""",
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Workspace directory where the scaffold folder is created (default: current directory)",
    )
    parser.add_argument(
        "--name",
        help=f"Scaffold folder name (default: {DEFAULT_PROJECT_FOLDER})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing anything",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files (default: skip existing)",
    )

    args = parser.parse_args()
    workspace = Path(args.target)
    project_name = args.name if args.name else DEFAULT_PROJECT_FOLDER
    target = workspace / project_name

    # Header
    if args.dry_run:
        print(f"\n{bold('=== DRY RUN ===')} Scaffold preview for: {cyan(str(target.resolve()))}\n")
    else:
        print(f"\n{bold('=== Scaffolding project ===')} {cyan(str(target.resolve()))}\n")
        target.mkdir(parents=True, exist_ok=True)

    created, skipped = create_scaffold(
        target,
        project_name=project_name,
        dry_run=args.dry_run,
        force=args.force,
    )

    # Summary
    print(f"\n{bold('--- Summary ---')}")
    print(f"  Created : {green(str(len(created)))} file(s)")
    if skipped:
        print(f"  Skipped : {yellow(str(len(skipped)))} file(s) {dim('(already exist, use --force to overwrite)')}")
    if args.dry_run:
        print(f"\n  {dim('(No files were written — this was a dry run)')}")
    else:
        print(f"\n  {green('Done!')} Your project scaffold is ready.")
        print(f"\n  {bold('Next steps:')}")
        print(f"    1. Fill in docs/ARCHITECTURE.md with your system design")
        print(f"    2. Fill in docs/DECISIONS.md as you make choices")
        print(f"    3. Fill in ops/QUALITY_GATES.md with your stack commands")
    print()


if __name__ == "__main__":
    main()
