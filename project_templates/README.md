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
