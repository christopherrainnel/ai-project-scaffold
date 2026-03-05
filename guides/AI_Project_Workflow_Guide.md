# AI Project Workflow Guide

Version: 2.9
Last Updated: 2026-03-05
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

## What Changed in v2.5

- Added cross-agent context-efficiency standards:
  - Read `docs/FILE_MAP.md` first for orientation
  - Avoid full-codebase preload by default
  - Token budget rule: load no more than 3 source files per task unless explicitly required
- Added `ops/prompts/SESSION_RESUME.md` for standardized context restore and agent handoff
- Updated policy loaders (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`) to align on FILE_MAP-first behavior

## What Changed in v2.8

- Added two-mode code review boundary:
  - `Mode A: Discovery` (findings only, no edits)
  - `Mode B: Fix` (edits only after explicit approval)
- Updated `ops/prompts/SESSION_RESUME.md` with strict low-token resume sequence:
  - confirm latest relevant `CHANGELOG_AI.md` entry
  - restate next concrete action
  - load minimal required files only
- Added compact handoff block format for session recovery.

## What Changed in v2.9

- Added Product Readiness Polish Gate to pre-release workflow:
  - UI quality pass
  - legal-page alignment check
  - release professionalism pass
  - explicit human approval for AI-assisted legal drafting
- Added legal text guidance: default to pattern-based synthesis; use verbatim reuse only when clearly permissible and attributable.

## What Changed in v2.11

- Aligned free-tier journey terminology to current lifecycle naming:
  - `Acquire Access` (instead of `Buy (if applicable)`)
  - `Study + Use` naming consistency in gate language
- Updated phase/release closure guidance so journey evidence is mapped to the active journey variant (`paid consumer`, `self-use`, `team/internal`).
- Added lightweight Dual-Lens Planning Gate language to keep implementation scope tied to both technical and user outcomes.

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
- Updated **`scaffold_project.py`** — generates the full scaffold template set, color output, `{{PROJECT_NAME}}` placeholder support
- Scaffold checklist in `ops/AI_WORKFLOW.md` now lists all required files explicitly

---

## Your Working Mode

**Primary workflow**: Local-first (projects live on your PC or synced drive).
**Tools**: Cursor (primary), VS Code (fallback), Claude Code (terminal), or any AI-enabled editor.
**Governance**: Enforced by files inside the project folder — no external config needed.

---

## Standard Project Scaffold

Created by `scaffold_project.py`:

```text
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
    SESSION_RESUME.md              # Session resume template (governance + FILE_MAP + current task)
    feature_request.md              # Feature request template
    bug_report.md                   # Bug report template
    refactor_request.md             # Refactor request template
    code_review.md                  # Code review template
.github/workflows/
  ci.yml                            # Merge-blocking quality + security gates
scripts/
  .gitkeep                          # Placeholder for utility scripts
```

---

## Policy Hierarchy — How Agents Find the Rules

Multiple files exist to support different AI tools, but they all defer to one source of truth:

```text
CLAUDE.md ─────────────┐
AGENTS.md ─────────────┤──> docs/FILE_MAP.md       (orientation-first)
.github/copilot-       │            │
  instructions.md ─────┘            └──> ops/AI_WORKFLOW.md  (canonical policy)
                                         │
                                         ├──> docs/ARCHITECTURE.md  (anti-drift)
                                         └──> docs/DECISIONS.md     (anti-drift)
```

| File | Who reads it | Purpose |
| ---- | ------------- | ------- |
| `CLAUDE.md` | Claude Code (auto-loaded) | Quick-start rules, points to canonical policy |
| `AGENTS.md` | GitHub Copilot Workspace, Codex, generic agents | Universal entry point |
| `.github/copilot-instructions.md` | VS Code Copilot | IDE-specific policy loader |
| `ops/AI_WORKFLOW.md` | All agents (via the above files) | **Single source of truth** |

If any conflict arises between these files, `ops/AI_WORKFLOW.md` wins.

---

## Daily Development Flow

For every task:

1. **You** describe the objective to the AI agent.
2. **Agent** uses default Build -> Review for simple tasks; adds a short plan for complex/high-risk work.
3. **Agent** makes small, reviewable edits. No unrelated reformatting.
4. **Agent** runs quality gates (lint/test/build) if available.
5. **You** review the change.
6. **Agent** updates:
   - `CHANGELOG_AI.md` — what changed, how verified, any risks
   - `ops/LESSONS_LEARNED.md` — only if the issue is likely to recur
   - `docs/DECISIONS.md` — only if an architectural choice was made

---

## Multi-Agent Support (Free Tier)

The free tier defaults to **single-agent operation**. This is the fastest path for most tasks.

**Optional Build -> Review flow**: For tasks where a second-pass review adds value (refactors, security-sensitive changes, multi-file edits), you can ask the agent to add a Review step after building. No mandatory planner is required — use a short plan only when complexity or risk justifies it.

Multi-agent orchestration (Plan -> Build -> Review with automatic activation/deactivation) is available in the [AI-guided tier (Tier1)](https://github.com/christopherrainnel/ai-project-scaffold-tier1).

---

## When to Escalate to Tier1

The free scaffold covers single-developer, single-agent projects well. Consider upgrading to Tier1 when:

| Signal | Why Tier1 helps |
| ------ | --------------- |
| You regularly need multi-agent workflows (Plan -> Build -> Review) | Tier1 auto-recommends and auto-deactivates multi-agent mode based on task complexity |
| New projects stall at the "blank page" phase | Bootstrap Protocol asks the right questions and derives scope + stack before coding |
| You want deterministic incomplete-detection for project scope | `PROJECT_BRIEF.md` + `STACK_SUMMARY.md` gate prevents building without defined outcomes |
| Architecture decisions keep getting revisited | `TRIGGERS.md` defines explicit escalation thresholds |
| You work across multiple stacks and need consistent Run Order conventions | `STACK_SUMMARY.md` records canonical run commands per project |

Tier1 is additive — everything in the free tier still works. The upgrade adds guided intake, structured scope, and multi-agent orchestration.

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
