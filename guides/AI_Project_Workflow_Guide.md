# AI Project Workflow Guide

Version: 2.4
Last Updated: 2026-03-03
Owner: Project Lead

---

## What This Guide Covers

This is the complete reference for the AI Project Scaffold system — how it works, why each piece exists, and how to use it day-to-day. This guide documents the **meta-repo** (the scaffold generator itself), not individual projects.

---

## What Changed in v2.4

- Added compliance-ready baseline files:
  - `docs/PRIVACY.md`
  - `docs/THREAT_MODEL.md`
  - `ops/RUNBOOK.md`
  - `ops/DEFINITION_OF_DONE.md`
  - `ops/STANDARDS_BASELINE.md`
  - `.github/workflows/ci.yml`
- Updated security and quality hard gates in `ops/AI_WORKFLOW.md`, `ops/SECURITY_POLICY.md`, and `ops/QUALITY_GATES.md`
- Updated generator behavior: `tools/scaffold_project.py` now loads from `project_templates/` as source of truth, with embedded fallback templates

## What Changed in v2.2

Major update to the scaffold and generator:

- Added **`CLAUDE.md`** — Claude Code now reads this automatically on every session
- Added **`docs/FILE_MAP.md`** — plain-English index of every file in the project
- Added **`ops/prompts/code_review.md`** — structured template for AI code reviews
- Added **`scripts/`** directory with `.gitkeep` placeholder
- Fixed **`AGENTS.md`** — no longer references non-existent `PROJECT_GOVERNANCE.md`
- Professionalized all template content — better structure, tables, guided placeholders
- Removed JS-specific learning preferences from copilot-instructions (now stack-agnostic)
- Added GitHub contribution UX files:
  - `.github/ISSUE_TEMPLATE/01-bug-report.yml`
  - `.github/ISSUE_TEMPLATE/02-feature-request.yml`
  - `.github/ISSUE_TEMPLATE/config.yml`
  - `.github/PULL_REQUEST_TEMPLATE.md`
- Added governance ownership and protection setup files:
  - `.github/CODEOWNERS`
  - `.github/BRANCH_PROTECTION.md`
- Updated **`ops/AI_WORKFLOW.md`** with source-quality rules for legal/security/policy topics
- Updated **`scaffold_project.py`** — generates all 28 files, color output, `{{PROJECT_NAME}}` placeholder support
- Scaffold checklist in `ops/AI_WORKFLOW.md` now lists all required files explicitly

---

## Your Working Mode

**Primary workflow**: Local-first (projects live on your PC or synced drive).
**Tools**: Cursor (primary), VS Code (fallback), Claude Code (terminal), or any AI-enabled editor.
**Governance**: Enforced by files inside the project folder — no external config needed.

---

## Standard Project Scaffold (34 files)

Created by `scaffold_project.py`:

```
README.md                           # Project overview
CLAUDE.md                           # Claude Code auto-read rules
AGENTS.md                           # Universal AI agent entry point
CHANGELOG_AI.md                     # AI change log
.env.example                        # Environment variable template
.gitignore                          # Git exclusions
.github/
  copilot-instructions.md           # VS Code Copilot policy loader
  PULL_REQUEST_TEMPLATE.md          # Pull request checklist
  CODEOWNERS                        # Default code owners
  BRANCH_PROTECTION.md              # Branch protection setup checklist
  ISSUE_TEMPLATE/
    01-bug-report.yml               # Bug intake form
    02-feature-request.yml          # Feature intake form
    config.yml                      # Issue template config
docs/
  ARCHITECTURE.md                   # System design (fill in per project)
  DECISIONS.md                      # Decision log (fill in as you go)
  FILE_MAP.md                       # Plain-English file index
  PRIVACY.md                        # Data inventory, retention, deletion, subprocessors
  THREAT_MODEL.md                   # Assets, threats, mitigations
ops/
  AI_WORKFLOW.md                    # Canonical AI policy (source of truth)
  SECURITY_POLICY.md                # Secret and data handling rules
  DATA_CLASSIFICATION.md            # Data sensitivity levels
  DEPENDENCY_POLICY.md              # Dependency management rules
  QUALITY_GATES.md                  # Definition of done + commands
  DEFINITION_OF_DONE.md             # Reusable security/privacy/testing checklist
  RELEASE_CHECKLIST.md              # Release verification steps
  RUNBOOK.md                        # Ops, logging, and incident basics
  STANDARDS_BASELINE.md             # Official-source standards baseline
  LESSONS_LEARNED.md                # Recurring issues and fixes
  prompts/
    feature_request.md              # Feature request template
    bug_report.md                   # Bug report template
    refactor_request.md             # Refactor request template
    code_review.md                  # Code review template
  workflows/
    ci.yml                          # Merge-blocking quality + security gates
scripts/
  .gitkeep                          # Placeholder for utility scripts
```

---

## Policy Hierarchy — How Agents Find the Rules

Multiple files exist to support different AI tools, but they all defer to one source of truth:

```
CLAUDE.md ─────────────┐
AGENTS.md ─────────────┤──> ops/AI_WORKFLOW.md  (canonical policy)
.github/copilot-       │
  instructions.md ─────┘
                              │
                              ├──> docs/ARCHITECTURE.md  (anti-drift)
                              └──> docs/DECISIONS.md     (anti-drift)
```

| File | Who reads it | Purpose |
|------|-------------|---------|
| `CLAUDE.md` | Claude Code (auto-loaded) | Quick-start rules, points to canonical policy |
| `AGENTS.md` | GitHub Copilot Workspace, Codex, generic agents | Universal entry point |
| `.github/copilot-instructions.md` | VS Code Copilot | IDE-specific policy loader |
| `ops/AI_WORKFLOW.md` | All agents (via the above files) | **Single source of truth** |

If any conflict arises between these files, `ops/AI_WORKFLOW.md` wins.

---

## Daily Development Flow

For every task:

1. **You** describe the objective to the AI agent.
2. **Agent** produces a short plan (files it will touch, approach).
3. **Agent** makes small, reviewable edits. No unrelated reformatting.
4. **Agent** runs quality gates (lint/test/build) if available.
5. **You** review the change.
6. **Agent** updates:
   - `CHANGELOG_AI.md` — what changed, how verified, any risks
   - `ops/LESSONS_LEARNED.md` — only if the issue is likely to recur
   - `docs/DECISIONS.md` — only if an architectural choice was made

---

## Security Rules (Non-Negotiable)

- Never paste secrets into chat or AI prompts.
- Secrets go only in `.env` locally (never committed).
- Only `.env.example` is committed (placeholder keys, no real values).
- Never run destructive terminal commands without explicit approval.
- If a secret is accidentally committed, rotate it and scrub git history.

`.gitignore` is part of the scaffold to prevent accidental commits.

---

## Anti-Drift Rules

Before implementing major changes:
1. Read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
2. If the requested change conflicts with documented decisions, stop and ask.
3. If a new architectural decision is made, log it in `docs/DECISIONS.md`.

## Product Growth Rules

- Agents and users may add product folders as needed (`apps/`, `services/`, `packages/`, `infra/`, `tests/`, etc.).
- Governance files (`ops/`, `.github/`, and core governance docs) are protected: edit only when necessary, with reviewed diffs and changelog entries.

---

## How to Use the Scaffold Generator

**Requirements**: Python 3.8+ (no external dependencies).

### Create a new project

```bash
python tools/scaffold_project.py --name my-project
```

### Scaffold with default folder name

```bash
python tools/scaffold_project.py
```

Creates `./project_template/` and scaffolds files inside it.

### Scaffold in a specific directory

```bash
python tools/scaffold_project.py /path/to/workspace
```

Creates `/path/to/workspace/project_template/` and scaffolds files inside it.

### Preview without writing files

```bash
python tools/scaffold_project.py --dry-run --name my-project
```

### Overwrite existing files (use carefully)

```bash
python tools/scaffold_project.py --force
```

**Default behavior is safe**: existing files are skipped unless `--force` is used.

The `--name` flag sets both the scaffold folder name and the `{{PROJECT_NAME}}` placeholder in `README.md`.

---

## After Scaffolding a New Project

Immediately fill in these three files — they are the foundation for AI-assisted work:

1. **`docs/ARCHITECTURE.md`** — system design, tech stack, components, data flow
2. **`docs/DECISIONS.md`** — record decisions as you make them (AI checks this before proposing changes)
3. **`ops/QUALITY_GATES.md`** — fill in the command table with your stack’s lint/test/build commands

Everything else has sensible defaults and can be customized later.

---

## Appendix: Script Internals

- Primary source of truth is `project_templates/`.
- The generator loads templates from `project_templates/` at runtime; embedded `FILES = { ... }` acts as fallback.
- `{{DATE}}` placeholders are replaced with today’s date at generation time.
- `{{PROJECT_NAME}}` is replaced with the `--name` argument (or the target directory name).
- The script uses no external dependencies — standard library only.
- Color output is auto-detected and works on modern terminals.
