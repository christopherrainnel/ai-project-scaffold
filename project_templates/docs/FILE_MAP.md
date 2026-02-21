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
