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

## `.claude/` - Claude Code Native Settings

| File | Purpose |
|------|---------|
| `.claude/settings.json` | Repo-local Claude Code permission policy that protects `.env` files and asks before risky shell operations |

## `.vscode/` - Optional VS Code Baseline

| File | Purpose |
|------|---------|
| `.vscode/extensions.json` | Recommended extension baseline (advisory-only, non-blocking) |
| `.vscode/settings.json` | Low-noise default editor settings with Python behavior scoped under `[python]` |

## `.cursor/` - Cursor Native Rules

| File | Purpose |
|------|---------|
| `.cursor/rules/00-governance.mdc` | Cursor native rule that loads governance context automatically on every task |

## `.windsurf/` - Windsurf Native Rules

| File | Purpose |
|------|---------|
| `.windsurf/rules/00-governance.md` | Windsurf workspace rule that enforces governance loading and canonical workflow reference |

## `.clinerules/` - Cline Native Rules and Hooks

| File | Purpose |
|------|---------|
| `.clinerules/01-governance.md` | Cline workspace rules file that enforces governance loading on every task |
| `.clinerules/hooks/TaskStart` | Example Cline hook that injects governance context when a task starts |
| `.clinerules/hooks/PreToolUse` | Example Cline hook that blocks `.env` access and obvious destructive commands |

## `.githooks/` - Optional Local Advisory Hook

| File | Purpose |
|------|---------|
| `.githooks/pre-commit.advisory` | Optional warning-first pre-commit wrapper for local advisory checks |

## `docs/` - Project Knowledge

| File | Purpose |
|------|---------|
| `ARCHITECTURE.md` | High-level system design, components, data flow |
| `DECISIONS.md` | Decision log - what was chosen, why, and what was rejected |
| `FILE_MAP.md` | This file - plain-English index of the entire project |
| `IDE_ENFORCEMENT.md` | Exact layout and positioning for repo-native IDE enforcement assets |
| `PRIVACY.md` | Data inventory, subprocessors, retention, and deletion process |
| `TERMS.md` | Plain-language terms stub for access, delivery, or membership projects |
| `THREAT_MODEL.md` | Lightweight threat model (assets, threats, mitigations) |
| `USER_CONSUMER_JOURNEY_CHECKLIST.md` | Project-specific checklist for validating the real user journey before release |

## `ops/` - Governance and Workflow

| File | Purpose |
|------|---------|
| `AI_WORKFLOW.md` | **Canonical policy** - the single source of truth for AI agent behavior, including workstation context checks and human practical testing gates |
| `SECURITY_POLICY.md` | Rules for secrets, data handling, and terminal safety |
| `DATA_CLASSIFICATION.md` | What data can be shared, what must be redacted, what is prohibited |
| `DEPENDENCY_POLICY.md` | Rules for adding, pinning, and auditing dependencies |
| `QUALITY_GATES.md` | Shipping gate + feature acceptance gate + stack-specific command placeholders, including workstation re-adoption and human validation completion checks |
| `DEFINITION_OF_DONE.md` | Pointer file that directs users to the authoritative checklists in `ops/QUALITY_GATES.md` |
| `RUNBOOK.md` | Operations guide, monitoring, incident basics, and workstation re-adoption SOP for local resume on a changed device |
| `STANDARDS_BASELINE.md` | Current standards and official-source references to consult |
| `RELEASE_CHECKLIST.md` | Pre-release and post-release verification steps |
| `LESSONS_LEARNED.md` | Recurring mistakes and their fixes - grows over time |

## `ops/prompts/` - Reusable Agent Prompts

| File | Purpose |
|------|---------|
| `SESSION_RESUME.md` | GOVERNANCE BOOT + low-token resume template that requires a workstation context check before trusting prior local state |
| `feature_request.md` | Structured template for requesting new features |
| `bug_report.md` | Structured template for reporting and fixing bugs |
| `refactor_request.md` | Structured template for refactoring tasks |
| `code_review.md` | Structured template for AI-assisted code reviews |

## `.github/` - Repository Automation and Contribution UX

| File | Purpose |
|------|---------|
| `copilot-instructions.md` | VS Code Copilot policy loader - references `ops/AI_WORKFLOW.md` |
| `dependabot.yml` | Automated update PRs for GitHub Actions and dependencies |
| `workflows/ci.yml` | Baseline CI gate workflow (lint/test/scan/sast/secret scan) |
| `ISSUE_TEMPLATE/01-bug-report.yml` | Structured bug intake form for consistent, reproducible reports |
| `ISSUE_TEMPLATE/02-feature-request.yml` | Structured feature request form with acceptance criteria |
| `ISSUE_TEMPLATE/config.yml` | Issue template config (disables blank issues by default) |
| `PULL_REQUEST_TEMPLATE.md` | Standard pull request checklist and verification prompt |
| `CODEOWNERS` | Default code ownership and required reviewer routing |
| `BRANCH_PROTECTION.md` | Checklist for configuring branch protection in GitHub settings |

## `scripts/` - Automation

| File | Purpose |
|------|---------|
| `scripts/local_preflight_advisory.py` | Optional local drift/tooling advisory check; strict mode only when `SCF_STRICT_LOCAL_CHECKS=1` |
