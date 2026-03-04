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

**Version:** 2.0
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
- **Risk register**: Add a short risk list for feature work.
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
.pytest_cache/
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

- Plan + risk register before feature code.
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

- **Plan before code**: Create a short plan and risk register for feature work.
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
| `.gitignore` | Keeps secrets, build artifacts (`__pycache__`, `node_modules`, etc.), and OS files out of version control |

## `docs/` — Project Knowledge

| File | Purpose |
|------|---------|
| `ARCHITECTURE.md` | High-level system design, components, data flow |
| `DECISIONS.md` | Decision log — what was chosen, why, and what was rejected |
| `FILE_MAP.md` | This file — plain-English index of the entire project |
| `PRIVACY.md` | Data inventory, subprocessors, retention, and deletion process |
| `THREAT_MODEL.md` | Lightweight threat model (assets, threats, mitigations) |

## `ops/` — Governance and Workflow

| File | Purpose |
|------|---------|
| `AI_WORKFLOW.md` | **Canonical policy** — the single source of truth for AI agent behavior |
| `SECURITY_POLICY.md` | Rules for secrets, data handling, and terminal safety |
| `DATA_CLASSIFICATION.md` | What data can be shared, what must be redacted, what is prohibited |
| `DEPENDENCY_POLICY.md` | Rules for adding, pinning, and auditing dependencies |
| `QUALITY_GATES.md` | Definition of done + stack-specific commands (lint, test, build) |
| `DEFINITION_OF_DONE.md` | Reusable checklist for future features |
| `RUNBOOK.md` | Operations guide, monitoring, and incident basics |
| `STANDARDS_BASELINE.md` | Current standards and official-source references to consult |
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
| `dependabot.yml` | Automated update PRs for GitHub Actions and dependencies |
| `workflows/ci.yml` | Merge-blocking quality + security workflow for configured and applicable checks |
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

Version: 2.0
Last Updated: {{DATE}}
Owner: Project Lead

---

## Purpose

This file is the **single source of truth** for how AI agents and IDE assistants operate in this repository.

Applies to: Claude Code, Cursor, VS Code Copilot, Windsurf, and any other AI-assisted tool.

This workflow is **security-first, privacy-first, and production-minded**. It is not legal advice.

---

## 1) Session Start (Hard Gate)

Before first code changes in a new feature/session:

1. Confirm governance scaffold completeness (Section 10).
2. Ask the minimum discovery questions needed to avoid building the wrong thing (see `ops/STANDARDS_BASELINE.md`).
3. Produce a short implementation plan plus a risk register.
4. If governance files are missing, ask to create missing files only; do not overwrite without approval.

---

## 2) Mandatory Operating Loop

Every task follows this loop:

1. **Plan** — scope, files, tests, risks.
2. **Execute** — small diffs only, no unrelated reformatting.
3. **Verify** — run applicable quality gates.
4. **Document** — update docs impacted by the change.
5. **Summarize** — include verification evidence and residual risks.
6. **Log** — update `CHANGELOG_AI.md`.

---

## 3) Non-Negotiable Rules

1. **Plan before code**: no feature implementation without a short plan + risk register.
2. **Security gates before shipping**: CI must fail on configured and applicable checks in `.github/workflows/ci.yml` (lint/format/typecheck/tests, vulnerability scan, secret scan, and basic SAST).
3. **No secrets in code**: never commit secrets, tokens, API keys, private URLs.
4. **Least privilege by default**: explicit roles/permissions and deny-by-default.
5. **Minimize and protect data**: collect minimum data; use encryption in transit and managed encryption at rest.
6. **Payments**: never handle raw card data; use hosted checkout/tokenization only.
7. **AI safety controls**: treat user input as hostile; guard against prompt injection; use tool allowlists and confirmation for sensitive actions.
8. **Legal baseline required**: align with official sources and record effective dates; never claim certification/compliance.

---

## 4) Security & Privacy Baseline

- Never read/modify `.env`; update `.env.example` only.
- Use input validation at every boundary.
- Apply secure headers where applicable (CSP, HSTS, frame protections, MIME protections).
- Implement rate limiting and abuse controls for public endpoints.
- Do not log PII/secrets.
- Define retention and deletion process in `docs/PRIVACY.md`.

---

## 5) AI Feature Baseline (When AI Is Used)

- Keep system/tool instructions isolated from user content.
- Require explicit confirmation for destructive or external actions.
- Restrict tool execution by allowlist.
- Redact sensitive data before sending to model providers.
- Store metadata or hashes where possible instead of full prompt/response logs.

---

## 6) Dependency & Supply Chain Discipline

- Add dependencies only with rationale.
- Pin versions and maintain lockfiles.
- Enable dependency vulnerability scanning.
- Enable secret scanning in pre-commit and CI.
- Generate SBOM when feasible.

---

## 7) Anti-Drift Control

Before implementation:

1. Read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
2. If change conflicts with documented decisions, stop and ask.
3. Log new architecture decisions in `docs/DECISIONS.md`.

---

## 8) High-Risk Fail-Safe

If the feature involves children, health data, regulated industry requirements, or direct payment handling:

1. Pause implementation.
2. Propose a safer reduced MVP scope.
3. Require legal/compliance review and DPIA/PIA-style assessment.
4. Resume only after minimization controls are documented.

---

## 9) Definition of Done

Use `ops/DEFINITION_OF_DONE.md` and `ops/QUALITY_GATES.md`.

A task is complete only when applicable checks pass and required docs are updated.

---

## 10) Scaffold Checklist

Required governance files:

```
CLAUDE.md
AGENTS.md
CHANGELOG_AI.md
.env.example
.gitignore
.github/copilot-instructions.md
.github/workflows/ci.yml
.github/ISSUE_TEMPLATE/01-bug-report.yml
.github/ISSUE_TEMPLATE/02-feature-request.yml
.github/ISSUE_TEMPLATE/config.yml
.github/PULL_REQUEST_TEMPLATE.md
.github/CODEOWNERS
.github/BRANCH_PROTECTION.md
docs/ARCHITECTURE.md
docs/DECISIONS.md
docs/FILE_MAP.md
docs/PRIVACY.md
docs/THREAT_MODEL.md
ops/AI_WORKFLOW.md
ops/SECURITY_POLICY.md
ops/DATA_CLASSIFICATION.md
ops/DEPENDENCY_POLICY.md
ops/QUALITY_GATES.md
ops/DEFINITION_OF_DONE.md
ops/RUNBOOK.md
ops/STANDARDS_BASELINE.md
ops/RELEASE_CHECKLIST.md
ops/LESSONS_LEARNED.md
ops/prompts/feature_request.md
ops/prompts/bug_report.md
ops/prompts/refactor_request.md
ops/prompts/code_review.md
```
""",
    "ops/DATA_CLASSIFICATION.md": """\
# Data Classification

Version: 2.0
Last Updated: {{DATE}}

> Use this guide to decide what can be shared with AI tools, logs, and repositories.

## Public

- Open-source code and docs
- Synthetic/mock datasets
- Redacted error logs
- Public API documentation

## Internal

- Non-public roadmap and pricing material
- Internal architecture and runbooks
- Aggregated analytics without direct identifiers

## Confidential

- Customer account metadata
- Non-public business contracts
- Deployment and infrastructure internals

## Regulated / Restricted (Highest)

- Secrets and credentials
- Personal data (name, email, phone, address, location, identifiers)
- Payment data (never store raw card data)
- Health, children, or other sensitive-category data
- Session tokens, auth cookies, private keys

## Handling Rules by Class

| Class | AI Sharing | Logging | Git Commit |
|------|------------|---------|------------|
| Public | Allowed | Allowed | Allowed |
| Internal | Redacted only | Minimal | Allowed with care |
| Confidential | Prefer no; redact if required | Metadata-only | Avoid unless necessary |
| Regulated/Restricted | Do not share by default | Avoid payload logging | Never commit raw values |

## Retention & Deletion

- Every collected data class must have an owner, retention period, and deletion path in `docs/PRIVACY.md`.
- If uncertain, default to shorter retention.

## Incident Response for Misclassification

1. Stop sharing immediately.
2. Revoke/rotate impacted secrets.
3. Remove exposed data from git history and logs where possible.
4. Document incident in `ops/RUNBOOK.md` and add follow-up controls.
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

Version: 2.0
Last Updated: {{DATE}}

## Shipping Gate (Required)

Code is not shippable unless all applicable checks pass locally and in CI.

- [ ] Lint
- [ ] Format check
- [ ] Type check
- [ ] Unit tests
- [ ] Dependency vulnerability scan
- [ ] Secret scan
- [ ] Basic SAST scan
- [ ] Build (if applicable)
- [ ] `CHANGELOG_AI.md` updated
- [ ] Relevant governance docs updated (`docs/DECISIONS.md`, `docs/PRIVACY.md`, `docs/THREAT_MODEL.md`, `ops/RUNBOOK.md`)

## CI Policy

- CI is mandatory for protected branches.
- Failing configured and applicable checks must block merges.
- Keep CI checks deterministic and fast.
- See `.github/workflows/ci.yml` as the baseline workflow.

## Project Commands (Fill Per Stack)

| Action | Command |
|--------|---------|
| Install | |
| Lint | |
| Format check | |
| Type check | |
| Unit test | |
| Build | |
| Dependency scan | |
| Secret scan | |
| SAST scan | |
| Dev server | |

## Reference Commands

### Node.js / Next.js (example)

```
Install:            npm ci
Lint:               npx eslint .
Format check:       npx prettier --check .
Type check:         npx tsc --noEmit
Unit test:          npm test
Build:              npm run build
Dependency scan:    npm audit --audit-level=high
Secret scan:        gitleaks detect --source . --no-git --redact
SAST scan:          semgrep --config auto
Dev server:         npm run dev
```

### Python / FastAPI / Django (example)

```
Install:            pip install -r requirements.txt
Lint:               ruff check .
Format check:       ruff format --check .
Type check:         mypy .
Unit test:          pytest
Build:              (optional for many Python apps)
Dependency scan:    pip-audit
Secret scan:        gitleaks detect --source . --no-git --redact
SAST scan:          semgrep --config auto
Dev server:         uvicorn main:app --reload
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

Version: 2.0
Last Updated: {{DATE}}

## Goal

Maintain a secure-by-default baseline for MVP delivery without custom security complexity.

## Core Rules

1. **No secrets in repository or client code.**
2. **Least privilege by default.** Explicit permissions and deny-by-default access.
3. **Data minimization.** Collect and retain only what is needed for the feature.
4. **Managed services over custom crypto/auth.** Prefer proven providers.

## Secret Management

| Rule | Detail |
|------|--------|
| Storage | Secrets in `.env` (local) and managed secret store (non-local). |
| Git | `.env` is never committed. Only `.env.example` is tracked. |
| Rotation | Rotate immediately after any suspected exposure. |
| Environment split | Separate keys per dev/stage/prod. |

## Access Control

- Use explicit roles/permissions.
- Deny-by-default endpoint behavior.
- Prefer managed auth (OIDC/OAuth) when accounts are needed.
- Use short-lived tokens/sessions with secure cookie settings when applicable.

## App & API Controls

- Input validation and output encoding at all trust boundaries.
- CSRF protection when cookie auth is used.
- Secure headers: CSP, HSTS, frame protections, and MIME protections (when applicable).
- Rate limiting and abuse controls for public interfaces.
- Upload controls: MIME/type checks, size limits, private storage, malware scanning strategy.

## Data Protection

- Encrypt in transit (TLS).
- Use provider-managed encryption at rest.
- Do not log secrets or full sensitive payloads.
- Define retention/deletion in `docs/PRIVACY.md`.

## Payments Baseline

- Never process raw card number/CVV in app code.
- Use hosted checkout/tokenization with a PCI-compliant payment provider.

## AI Safety Controls (If AI Features Exist)

- Treat user prompts and uploads as hostile input.
- Isolate system/tool prompts from user content.
- Require explicit user confirmation for sensitive actions.
- Apply tool/action allowlists and safe-fail behavior.

## Prohibited Content in Chat/Logs/Commits

- API keys, tokens, passwords, private URLs with auth material
- Production database exports/connection strings
- Customer PII and regulated data unless explicitly approved and redacted
- Internal infrastructure-sensitive data (hostnames/IP topology)
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

You can add product folders as needed (`apps/`, `services/`, `packages/`, `infra/`, `tests/`, etc.).

## For AI Agents

Start with `AGENTS.md` (or `CLAUDE.md` for Claude Code). These files point to the canonical policy in `ops/AI_WORKFLOW.md`.

## Key Rules

- Never commit `.env` — only `.env.example` is tracked.
- All AI changes are logged in `CHANGELOG_AI.md`.
- Decisions and their rationale go in `docs/DECISIONS.md`.
- Use `ops/QUALITY_GATES.md` + `.github/workflows/ci.yml` as merge-blocking quality/security gates for all configured and applicable checks.
- Keep `docs/PRIVACY.md` and `docs/THREAT_MODEL.md` updated as features evolve.
- Treat governance files (`ops/`, `.github/`, and core governance docs) as protected; only edit them when necessary and log why in `CHANGELOG_AI.md`.

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
    ".github/dependabot.yml": """\
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "security"

  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "security"
""",
    ".github/workflows/ci.yml": """\
name: CI Gates

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read
  security-events: write

jobs:
  quality-and-security:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Setup Node (if package.json exists)
        if: hashFiles('**/package.json') != ''
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: npm

      - name: Setup Python (if requirements exist)
        if: hashFiles('**/requirements*.txt', '**/pyproject.toml') != ''
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Node install
        if: hashFiles('**/package.json') != ''
        run: npm ci

      - name: Node lint
        if: hashFiles('**/package.json') != ''
        run: npm run lint --if-present

      - name: Node format check
        if: hashFiles('**/package.json') != ''
        run: npm run format:check --if-present

      - name: Node typecheck
        if: hashFiles('**/package.json') != ''
        run: npm run typecheck --if-present

      - name: Node test
        if: hashFiles('**/package.json') != ''
        run: npm test --if-present

      - name: Node build
        if: hashFiles('**/package.json') != ''
        run: npm run build --if-present

      - name: Node dependency audit
        if: hashFiles('**/package.json') != ''
        run: npm audit --audit-level=high

      - name: Python install deps
        if: hashFiles('**/requirements*.txt') != ''
        run: |
          req_file=$(ls requirements*.txt | head -n 1)
          pip install -r "$req_file"

      - name: Python install quality tools
        if: hashFiles('**/requirements*.txt', '**/pyproject.toml') != ''
        run: pip install ruff mypy pytest pip-audit bandit

      - name: Python lint (ruff)
        if: hashFiles('**/requirements*.txt', '**/pyproject.toml') != ''
        run: python -m ruff check .

      - name: Python format check (ruff)
        if: hashFiles('**/requirements*.txt', '**/pyproject.toml') != ''
        run: python -m ruff format --check .

      - name: Python type check (mypy)
        if: hashFiles('**/requirements*.txt', '**/pyproject.toml') != ''
        run: mypy --ignore-missing-imports --no-strict-optional .

      - name: Python tests
        if: hashFiles('tests/**/*.py') != ''
        run: pytest

      - name: Python dependency audit
        if: hashFiles('**/requirements*.txt', '**/pyproject.toml') != ''
        run: |
          req_file=$(ls requirements*.txt 2>/dev/null | head -n 1)
          if [ -n "$req_file" ]; then
            python -m pip_audit -r "$req_file"
          else
            python -m pip_audit
          fi

      - name: Secret scan (gitleaks)
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Basic SAST scan (bandit)
        if: hashFiles('**/*.py') != ''
        run: python -m bandit -r . -lll

      - name: Basic SAST scan (semgrep)
        uses: returntocorp/semgrep-action@v1
        with:
          config: auto
""",
    "docs/PRIVACY.md": """\
# Privacy Baseline

Version: 0.1
Last Updated: {{DATE}}

> This document is a practical privacy baseline for MVP teams. It is not legal advice.

## Data Inventory

| Data Category | Purpose | Required? | Storage Location | Shared With | Retention | Deletion Method |
|---------------|---------|-----------|------------------|-------------|-----------|-----------------|
| Account email | | | | | | |
| Profile name | | | | | | |
| App content/uploads | | | | | | |
| Payment metadata (non-card) | | | | | | |
| Logs/telemetry metadata | | | | | | |

## Legal/Jurisdiction Snapshot

- Target users: <!-- EU/UK/US/CA/other -->
- Regulated context: <!-- none / health / finance / education / other -->
- Applicable baseline laws (as relevant): GDPR/UK GDPR, CCPA/CPRA, ePrivacy/cookie rules, COPPA.

## Collection Principles

- Collect the minimum data needed for the feature.
- Do not collect sensitive categories unless there is a clear product need and additional controls.
- Do not process raw card data in app code.

## User Rights Process (MVP)

- Access/export request process: <!-- email + manual SLA -->
- Deletion request process: <!-- email + manual/automated flow -->
- Correction process: <!-- how user can correct profile data -->
- SLA target: <!-- e.g., 30 days -->

## Subprocessors

| Vendor | Purpose | Data Shared | DPA/Terms Checked | Region |
|--------|---------|-------------|-------------------|--------|
| | | | | |

## Cookies / Analytics

- Default to privacy-preserving analytics.
- If non-essential cookies are used, add consent flow where legally required.

## Security Controls Supporting Privacy

- Encryption in transit (TLS)
- Managed encryption at rest
- Access controls with least privilege
- Redaction/no-PII logging policy

## Review Cadence

- Review this file at each release with user-facing data changes.
""",
    "docs/THREAT_MODEL.md": """\
# Threat Model (Lightweight)

Version: 0.1
Last Updated: {{DATE}}

## Scope

- Product area: <!-- API / Web app / worker -->
- In-scope environments: <!-- local/stage/prod -->

## Critical Assets

- User identity/session
- Application data
- Secrets and credentials
- Payment/session metadata

## Trust Boundaries

- Client ↔ API
- API ↔ Database
- API ↔ Third-party services
- CI/CD ↔ Repository/Secrets

## Top Threats and Mitigations

| Threat | Example | Mitigation | Status |
|--------|---------|------------|--------|
| Injection | SQL/command/template injection | Input validation, parameterized queries, escaping | |
| Auth bypass | Broken auth/authorization | Managed auth, RBAC, deny-by-default checks | |
| Secrets exposure | Key in repo/logs | Secret scanning, `.env.example` only, redaction | |
| Data leakage | PII in logs or responses | Data minimization, no-PII logging, response filtering | |
| Abuse/DoS | Endpoint flood | Rate limits, abuse monitoring | |
| Prompt injection (AI) | User text manipulates tools | Tool allowlist, confirmation gates, context isolation | |

## Security Tests

- Unit tests for auth and permission checks
- Input validation tests at every external boundary
- CI SAST + dependency + secret scanning

## Residual Risks

- <!-- List known risks accepted for MVP and planned next step -->
""",
    "ops/DEFINITION_OF_DONE.md": """\
# Definition of Done (Future Features)

Version: 1.0
Last Updated: {{DATE}}

Use this checklist before merging feature work.

## Product Quality

- [ ] Acceptance criteria are met.
- [ ] One vertical slice is complete end-to-end.
- [ ] Non-goals were not accidentally included.

## Engineering Quality

- [ ] Lint, format, typecheck, tests, and build pass.
- [ ] CI workflow passes on pull request.
- [ ] Changes are small, focused, and reviewed.

## Security & Privacy

- [ ] No secrets are committed.
- [ ] Input validation and authorization checks are in place.
- [ ] Rate limits/abuse controls are added for public endpoints.
- [ ] Logging avoids secrets and personal data.
- [ ] Data retention/deletion impacts are reflected in `docs/PRIVACY.md`.

## Documentation & Operations

- [ ] `docs/DECISIONS.md` updated for architectural choices.
- [ ] `docs/THREAT_MODEL.md` updated for new attack surfaces.
- [ ] `ops/RUNBOOK.md` updated if operations changed.
- [ ] `CHANGELOG_AI.md` entry added.

## Compliance Wording Rule

- [ ] Language uses "aligned with" or "informed by" standards.
- [ ] No certification/compliance claims are made without proof.
""",
    "ops/RUNBOOK.md": """\
# Runbook (Operations Basics)

Version: 0.1
Last Updated: {{DATE}}

## Environments

| Environment | URL/Endpoint | Owner | Notes |
|-------------|--------------|-------|-------|
| Dev | | | |
| Stage | | | |
| Prod | | | |

## Monitoring Baseline

- Structured logs enabled
- Error tracking configured
- Basic service health checks
- No secrets/PII in logs

## Incident Severity (Simple)

- **SEV-1**: major outage/data-impacting issue
- **SEV-2**: partial outage or major feature degraded
- **SEV-3**: minor issue with workaround

## Incident Response Steps

1. Acknowledge and assign incident owner.
2. Stabilize service (rollback/feature flag/isolation).
3. Assess privacy/security impact.
4. Communicate status internally.
5. Resolve and verify.
6. Record post-incident actions in `ops/LESSONS_LEARNED.md`.

## Security/Privacy Incident Minimum Actions

- Rotate exposed secrets immediately.
- Disable compromised credentials/tokens.
- Preserve logs/evidence for review.
- Document impact, scope, and remediation.

## Backup and Restore Notes

- Backup schedule: <!-- define -->
- Restore procedure: <!-- define -->
- Last restore test date: <!-- define -->
""",
    "ops/STANDARDS_BASELINE.md": """\
# Standards Baseline (Official Sources)

Version: 1.0
Last Updated: {{DATE}}

> Use this checklist before finalizing architecture or compliance-related recommendations.
> Always verify the latest updates on official pages and record the date reviewed.

## Security Baseline

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/

## Privacy & Data Protection

- GDPR (EU): https://gdpr.eu/
- UK GDPR + DPA guidance (ICO): https://ico.org.uk/
- CCPA/CPRA (California): https://oag.ca.gov/privacy/ccpa
- ePrivacy/cookies overview (EU): https://eur-lex.europa.eu/

## Children’s Data

- COPPA (FTC): https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa

## Payments

- PCI SSC (PCI DSS): https://www.pcisecuritystandards.org/

## Security Management References

- ISO/IEC 27001 overview: https://www.iso.org/isoiec-27001-information-security.html
- SOC for Service Organizations (AICPA overview): https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2

## Required Usage Rule

When advice touches legal/privacy/security/payment topics:

1. Cite the official source URL used.
2. Record "Reviewed on: YYYY-MM-DD" in output/docs.
3. If uncertain, choose safer defaults and explicitly call out uncertainty.
4. Recommend professional legal/compliance review for sensitive or regulated use cases.
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


def green(text):
    return _c("32", text)


def yellow(text):
    return _c("33", text)


def cyan(text):
    return _c("36", text)


def bold(text):
    return _c("1", text)


def dim(text):
    return _c("2", text)


# ---------------------------------------------------------------------------
# Generator logic
# ---------------------------------------------------------------------------


def resolve_placeholders(content: str, project_name: str) -> str:
    """Replace template placeholders with actual values."""
    content = content.replace("{{DATE}}", TODAY)
    content = content.replace("{{PROJECT_NAME}}", project_name)
    return content


def load_templates() -> dict:
    """Load templates from project_templates/ when available, else fallback to embedded FILES."""
    script_dir = Path(__file__).resolve().parent
    template_root = script_dir.parent / "project_templates"

    if not template_root.exists():
        return FILES

    loaded = {}
    for file_path in sorted(template_root.rglob("*")):
        if file_path.is_file():
            rel_path = file_path.relative_to(template_root).as_posix()
            loaded[rel_path] = file_path.read_text(encoding="utf-8")

    return loaded if loaded else FILES


# Keep FILES aligned with on-disk templates when this repository includes
# project_templates/. This preserves embedded fallback behavior for single-file
# distribution while ensuring local tests and scaffolding use canonical content.
FILES = load_templates()


def create_scaffold(
    target_dir: Path,
    project_name: str,
    templates: dict = None,
    dry_run: bool = False,
    force: bool = False,
):
    """Create the full project scaffold under target_dir."""
    if templates is None:
        templates = FILES
    target_dir = target_dir.resolve()
    created_dirs = set()
    created_files = []
    skipped_files = []

    for rel_path, content in templates.items():
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
        print(
            f"\n{bold('=== DRY RUN ===')} Scaffold preview for: {cyan(str(target.resolve()))}\n"
        )
    else:
        print(
            f"\n{bold('=== Scaffolding project ===')} {cyan(str(target.resolve()))}\n"
        )
        target.mkdir(parents=True, exist_ok=True)

    created, skipped = create_scaffold(
        target,
        templates=load_templates(),
        project_name=project_name,
        dry_run=args.dry_run,
        force=args.force,
    )

    # Summary
    print(f"\n{bold('--- Summary ---')}")
    print(f"  Created : {green(str(len(created)))} file(s)")
    if skipped:
        print(
            f"  Skipped : {yellow(str(len(skipped)))} file(s) {dim('(already exist, use --force to overwrite)')}"
        )
    if args.dry_run:
        print(f"\n  {dim('(No files were written — this was a dry run)')}")
    else:
        print(f"\n  {green('Done!')} Your project scaffold is ready.")
        print(f"\n  {bold('Next steps:')}")
        print("    1. Fill in docs/ARCHITECTURE.md with your system design")
        print("    2. Fill in docs/DECISIONS.md as you make choices")
        print("    3. Fill in ops/QUALITY_GATES.md with your stack commands")
    print()


if __name__ == "__main__":
    main()
    # When running as a bundled .exe, pause so the user can read the output
    if getattr(sys, "frozen", False):
        input("\nPress Enter to exit...")
