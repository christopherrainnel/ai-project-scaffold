# AI Project Scaffold Generator

A project template and Python tool for Vibe Coders who build products with AI agents. Creates a governed, professional project structure in seconds.

## What This Gives You

Every new project starts with:

- **Agent rules** (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`) — so AI tools follow your project's policies automatically
- **Canonical workflow** (`ops/AI_WORKFLOW.md`) — the single source of truth for how AI operates in your repo
- **Security, dependency, and data policies** — sensible defaults you can customize
- **Architecture and decision docs** — anti-drift anchors that prevent AI from going off-track
- **Prompt templates** — structured templates for feature requests, bug reports, refactors, and code reviews
- **Change log** — automatic tracking of every AI-made change

## Quick Start

```bash
# Scaffold a new project
python tools/scaffold_project.py --name my-project

# Scaffold in the current directory
python tools/scaffold_project.py

# Preview without writing files
python tools/scaffold_project.py --dry-run --name my-project

# Overwrite existing files (use carefully)
python tools/scaffold_project.py --force
```

**Requirements**: Python 3.8+ (no external dependencies).

## What Gets Created

```
my-project/
├── CLAUDE.md                       # Claude Code auto-read rules
├── AGENTS.md                       # Universal AI agent entry point
├── CHANGELOG_AI.md                 # AI change log
├── README.md                       # Project README
├── .env.example                    # Environment variable template
├── .gitignore                      # Git exclusions
├── .github/
│   └── copilot-instructions.md     # VS Code Copilot policy loader
├── docs/
│   ├── ARCHITECTURE.md             # System design (fill in per project)
│   ├── DECISIONS.md                # Decision log (fill in as you go)
│   └── FILE_MAP.md                 # Plain-English file index
├── ops/
│   ├── AI_WORKFLOW.md              # Canonical AI policy (source of truth)
│   ├── SECURITY_POLICY.md          # Secret and data handling rules
│   ├── DATA_CLASSIFICATION.md      # Data sensitivity levels
│   ├── DEPENDENCY_POLICY.md        # Dependency management rules
│   ├── QUALITY_GATES.md            # Definition of done + commands
│   ├── RELEASE_CHECKLIST.md        # Release verification steps
│   ├── LESSONS_LEARNED.md          # Recurring issues and fixes
│   └── prompts/
│       ├── feature_request.md      # Feature request template
│       ├── bug_report.md           # Bug report template
│       ├── refactor_request.md     # Refactor request template
│       └── code_review.md          # Code review template
└── scripts/
    └── .gitkeep                    # Placeholder for utility scripts
```

## Repo Structure (This Repo)

```
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
- **`tools/scaffold_project.py`** — The generator. Embeds all template content and creates projects from scratch.
- **`guides/`** — Documentation on the philosophy, workflow, and usage of this system.

## After Scaffolding a New Project

1. **Rename the project folder** from `my-project` to the actual name of what you are building (e.g., `invoice-tracker`, `habit-app`). Update the `# {{PROJECT_NAME}}` heading in `README.md` to match.
2. Fill in `docs/ARCHITECTURE.md` with your system design.
3. Fill in `docs/DECISIONS.md` as you make architectural choices.
4. Fill in `ops/QUALITY_GATES.md` with your stack's lint/test/build commands.
5. Start building with your AI agent — it will follow the governance rules automatically.

## Growing Your Project

The scaffold gives you the governance skeleton. As you build, your project will grow with your own code and content:

- **Add source folders as needed** — e.g., `src/`, `app/`, `web/`, `api/`, `components/`, `lib/`. Structure these however your framework expects.
- **Add docs only when they earn their keep** — you may add `.md` files to `docs/` (e.g., `docs/API_REFERENCE.md`, `docs/DEPLOYMENT.md`) but only when a document will be actively used and maintained. Avoid creating docs "just in case."
- **Keep `docs/FILE_MAP.md` updated** — whenever you add a significant folder or file, add a one-line entry so anyone (human or AI) can orient quickly.
- **Log new architectural decisions** — every time you choose a framework, database, hosting provider, or major pattern, record it in `docs/DECISIONS.md` so your AI agent does not reverse it later.

> **Rule of thumb**: the `ops/` and `docs/` folders are governance — keep them lean. Everything else is your product — let it grow naturally.

## Guide

See `guides/AI_Project_Workflow_Guide.md` for the complete documentation on:
- How the governance system works
- The agent read order and policy hierarchy
- Daily development flow with AI
- Security rules and anti-drift controls