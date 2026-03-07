# AI Project Scaffold Generator

> **Free & open source.** Fully usable as-is. For an AI-guided version that eliminates blank-page paralysis and scopes a 7-day deliverable before you write a line of code, see the [AI-guided tier](https://github.com/christopherrainnel/ai-project-scaffold-tier1).

A project template and Python tool for Vibe Coders who build products with AI agents. Creates a governed, professional project structure in seconds.

## Scope and Disclaimer

- This repository is an AI-assisted starter template for engineering workflow and repository hygiene.
- It is **not** legal, regulatory, or compliance advice.
- You are responsible for adapting policies to your organization, jurisdiction, and risk profile.

## What This Gives You

Every new project starts with:

- **Agent rules** (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`) — so AI tools follow your project's policies automatically
- **Free enforcement baseline** (`.claude/settings.json` + loader docs) — focused governance loading for Claude and VS Code Copilot/Codex workflows
- **Single-agent default + optional Build -> Review flow** — fast path for simple tasks, with planning used only when complexity/risk requires it
- **Context-efficient agent startup** — read `docs/FILE_MAP.md` first, fetch only task-relevant files, and avoid full-codebase preload
- **Canonical workflow** (`ops/AI_WORKFLOW.md`) — the single source of truth for how AI operates in your repo
- **Two-mode code-review boundary** — default to findings-only review first, apply fixes only after explicit approval
- **Product readiness polish gate** — pre-release UI/legal/professionalism checks with mandatory human approval for AI-assisted legal drafting
- **Security, dependency, and data policies** — sensible defaults you can customize
- **Architecture and decision docs** — anti-drift anchors that prevent AI from going off-track
- **Operational policy docs** (`docs/TERMS.md`, `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md`) — plain-language terms and journey-stage release evidence tracking
- **Prompt templates** — structured templates for session resume, feature requests, bug reports, refactors, and code reviews
- **GOVERNANCE BOOT session-start prompt** — a required copy/paste prompt that forces policy loading before implementation
- **Strict resume sequence** — `SESSION_RESUME` enforces low-token restart order with next-action recovery
- **Change log** — automatic tracking of every AI-made change

## Tier Boundary (Free vs Tier1)

- `both`: Governance baseline (agent rules, AI workflow, quality/security gates, decision logs, privacy/threat modeling, changelog discipline)
- `free` (this repo): Bootstrap-less scaffold with single-agent default and optional Build -> Review flow
- `tier1`: Bootstrap Protocol plus tier1-only files (`docs/PROJECT_BRIEF.md`, `docs/STACK_SUMMARY.md`, `docs/TRIGGERS.md`, `ops/prompts/project_bootstrap.md`)

Free policy note: `project_templates/docs/USER_CONSUMER_JOURNEY_CHECKLIST.md` is intentionally kept as a stable baseline in free. Future checklist-component expansions are Tier1+ only.

This split is intentional: both repos stay aligned on governance quality, while Tier1 remains the guided-entry upgrade path.

## Template Alignment Note (v2.15)

Free template policy now keeps a focused baseline: `.claude/settings.json` plus loader docs (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`). Cursor/Windsurf/Cline native rule packs and `IDE_ENFORCEMENT.md` are Tier1-only. `docs/TERMS.md` remains in free.

## Quick Start

```bash
# Scaffold a new project
python tools/scaffold_project.py --name my-project

# Scaffold into ./project_template/ (default folder)
python tools/scaffold_project.py

# Preview without writing files
python tools/scaffold_project.py --dry-run --name my-project

# Overwrite existing files (use carefully)
python tools/scaffold_project.py --force
```

**Requirements**: Python 3.8+ (no external dependencies).

## Required: Start Every AI Session With This Prompt

```text
Before anything else this session: read docs/FILE_MAP.md, AGENTS.md, and ops/AI_WORKFLOW.md -
follow the governance rules you find there. For any feature or phase work, produce a dual-lens
plan (Technical Builder POV + User/Consumer POV) and at least one risk with mitigation before
implementing. My task: [REPLACE WITH ACTUAL TASK]
```

### Windows: standalone .exe (no Python required)

Download `project_scaffold.exe` from the [latest release](https://github.com/christopherrainnel/ai-project-scaffold/releases/latest), place it in the folder where you want your project, and double-click it.
If a release is not published yet or the artifact is unavailable, build locally using `python build_exe.py`.

To build the `.exe` yourself: `python build_exe.py` (requires `pip install pyinstaller`).

## What Gets Created

```text
my-project/
├── CLAUDE.md                       # Claude Code auto-read rules
├── AGENTS.md                       # Universal AI agent entry point
├── CHANGELOG_AI.md                 # AI change log
├── README.md                       # Project README
├── .env.example                    # Environment variable template
├── .gitignore                      # Git exclusions
├── .claude/
│   └── settings.json               # Claude native permission policy
├── .github/
│   ├── copilot-instructions.md     # VS Code Copilot policy loader
│   ├── PULL_REQUEST_TEMPLATE.md    # Pull request checklist
│   ├── CODEOWNERS                  # Default code owners
│   ├── BRANCH_PROTECTION.md        # Branch protection setup checklist
│   ├── dependabot.yml              # Automated dependency/action update PRs
│   └── ISSUE_TEMPLATE/
│       ├── 01-bug-report.yml       # Bug intake form
│       ├── 02-feature-request.yml  # Feature intake form
│       └── config.yml              # Issue template config
├── docs/
│   ├── ARCHITECTURE.md             # System design (fill in per project)
│   ├── DECISIONS.md                # Decision log (fill in as you go)
│   ├── FILE_MAP.md                 # Plain-English file index
│   ├── PRIVACY.md                  # Data inventory, retention, deletion, subprocessors
│   ├── TERMS.md                    # Plain-language operating terms stub
│   ├── THREAT_MODEL.md             # Assets, threats, mitigations
│   └── USER_CONSUMER_JOURNEY_CHECKLIST.md  # Journey-stage release evidence checklist
├── ops/
│   ├── AI_WORKFLOW.md              # Canonical AI policy (source of truth)
│   ├── SECURITY_POLICY.md          # Secret and data handling rules
│   ├── DATA_CLASSIFICATION.md      # Data sensitivity levels
│   ├── DEPENDENCY_POLICY.md        # Dependency management rules
│   ├── QUALITY_GATES.md            # Shipping gate + feature acceptance gate + commands
│   ├── DEFINITION_OF_DONE.md       # Pointer to authoritative checklists in QUALITY_GATES
│   ├── RUNBOOK.md                  # Ops, logging, and incident basics
│   ├── STANDARDS_BASELINE.md       # Official-source standards cross-check baseline
│   ├── RELEASE_CHECKLIST.md        # Release verification steps
│   ├── LESSONS_LEARNED.md          # Recurring issues and fixes
│   └── prompts/
│       ├── SESSION_RESUME.md      # Resume-context prompt (governance + FILE_MAP + current task)
│       ├── feature_request.md      # Feature request template
│       ├── bug_report.md           # Bug report template
│       ├── refactor_request.md     # Refactor request template
│       └── code_review.md          # Code review template
├── .github/workflows/
│   └── ci.yml                      # Merge-blocking quality + security gates
└── scripts/
    └── .gitkeep                    # Placeholder for utility scripts
```

## Repo Structure (This Repo)

```text
PROJECT CREATION/
├── README.md                       # This file
├── guides/
│   └── AI_Project_Workflow_Guide.md  # Full documentation on how and why
├── project_templates/              # Canonical template (reference copy)
│   └── (all files above)
└── tools/
    └── scaffold_project.py         # The generator script
```

- **`project_templates/`** — The gold-standard reference. Edit these files to update what gets generated.
- **`tools/scaffold_project.py`** — The generator. Uses `project_templates/` as source of truth (with embedded fallback).
- **`guides/`** — Documentation on the philosophy, workflow, and usage of this system.

## After Scaffolding a New Project

1. **Rename the project folder** from `my-project` to the actual name of what you are building (e.g., `invoice-tracker`, `habit-app`). Update the `# {{PROJECT_NAME}}` heading in `README.md` to match.
2. Fill in `docs/ARCHITECTURE.md` with your system design.
3. Fill in `docs/DECISIONS.md` as you make architectural choices.
4. Fill in `ops/QUALITY_GATES.md` with your stack's lint/test/build commands.
5. Start building with your AI agent — it will follow the governance rules automatically.
6. When resuming a conversation or switching agents, use `ops/prompts/SESSION_RESUME.md` to restore only the minimum required context.

## Growing Your Project

The scaffold gives you the governance skeleton. As you build, your project will grow with your own code and content:

- **Add source folders as needed** — e.g., `src/`, `app/`, `web/`, `api/`, `components/`, `lib/`. Structure these however your framework expects.
- **Add docs only when they earn their keep** — you may add `.md` files to `docs/` (e.g., `docs/API_REFERENCE.md`, `docs/DEPLOYMENT.md`) but only when a document will be actively used and maintained. Avoid creating docs "just in case."
- **Keep `docs/FILE_MAP.md` updated** — whenever you add a significant folder or file, add a one-line entry so anyone (human or AI) can orient quickly.
- **Log new architectural decisions** — every time you choose a framework, database, hosting provider, or major pattern, record it in `docs/DECISIONS.md` so your AI agent does not reverse it later.
- **Agents may create product folders freely** — e.g., `apps/`, `services/`, `packages/`, `infra/`, `tests/`, `assets/` — when required by product scope.
- **Treat governance files as protected** — avoid editing `ops/`, `.github/`, and core `docs/` governance files unless the change is necessary, reviewed, and logged.

> **Rule of thumb**: the `ops/` and `docs/` folders are governance — keep them lean. Everything else is your product — let it grow naturally.

## Guide

See `guides/AI_Project_Workflow_Guide.md` for the complete documentation on:

- How the governance system works
- The cross-agent read order and policy hierarchy (`FILE_MAP.md` first)
- Daily development flow with AI
- Security rules and anti-drift controls

## Maturity

This project is useful in practice, but it is still early compared with long-established ecosystems and does not yet match their maturity/adoption level.

We improve this repo continuously through maintainer review and contributions from approved contributors (see `CONTRIBUTING.md`).

## Roadmap (Brief)

- **Current focus (A): Access Hub**
- **Next focus (3): VS Code extension companion**
- **Later hardening (2): GitHub App model**

## Feedback

Use this template, share what works, and report what does not.

- Please keep feedback constructive, specific, and respectful.
- Open issues for bugs/feature requests.
- Open pull requests for concrete improvements.

## Project Governance (This Repo)

- Security reporting: see `SECURITY.md`
- Contribution guidelines: see `CONTRIBUTING.md`
- Community standards: see `CODE_OF_CONDUCT.md`
- Issue forms and PR checklist: see `.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`
- Code owners: see `.github/CODEOWNERS`
- Branch protection setup: see `.github/BRANCH_PROTECTION.md`
- DCO sign-off policy: see `DCO.md`
- Dependabot updates: see `.github/dependabot.yml`
- License: MIT (`LICENSE`)

## Contribution Terms

Contributions are governed by `LICENSE` (MIT). By submitting a contribution, contributors agree it is provided under that license and is unpaid unless separately agreed in writing.

## Level Up: AI-Guided Tier

This free scaffold gives you governance and structure. If you want **an agent that guides you from day one** — asks the right questions, derives your stack from constraints, defines a 7-day vertical slice before coding, and keeps you from overbuilding — the [AI-guided tier](https://github.com/christopherrainnel/ai-project-scaffold-tier1) adds that. Access via sponsorship or other payment methods.

**Support / Sponsor:** [GitHub Sponsors](https://github.com/sponsors/christopherrainnel) · [Patreon](https://www.patreon.com/posts/standard-one-tip-152177425?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link)

- **This tier**: MIT, fully usable, no strings attached.
- **That tier**: Bootstrap Protocol, deterministic incomplete detection, Run Order conventions, and trigger-based architecture escalation.
