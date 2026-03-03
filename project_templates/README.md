# {{PROJECT_NAME}}

> Built with AI-assisted development using a governed scaffold.

## Quick Start

1. Clone this repo and open it in your IDE (Cursor, VS Code, or any AI-enabled editor).
2. Copy `.env.example` to `.env` and fill in your values.
3. Read `ops/AI_WORKFLOW.md` — this is the source of truth for how AI agents work in this project.
4. Fill in `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` with your project specifics.

## Project Structure

```text
docs/           Architecture, decisions, and file map
ops/            Governance policies, workflow rules, prompt templates
ops/prompts/    Reusable prompt templates for common tasks
scripts/        Utility and automation scripts
```

See `docs/FILE_MAP.md` for a plain-English guide to every file.

You can add product folders as needed (`apps/`, `services/`, `packages/`, `infra/`, `tests/`, etc.).

## For AI Agents

Start with `AGENTS.md` (or `CLAUDE.md` for Claude Code). These files point to the canonical policy in `ops/AI_WORKFLOW.md`.
Use `docs/FILE_MAP.md` first for orientation, then fetch only task-relevant files.
<<<<<<< HEAD

Free tier defaults to single-agent operation. Optional Build -> Review flow is supported, with no mandatory planner for simple tasks.
=======
>>>>>>> 179ded47758f459612eecf3c23befa4a6e98bea6

## Key Rules

- Never commit `.env` — only `.env.example` is tracked.
- All AI changes are logged in `CHANGELOG_AI.md`.
- Decisions and their rationale go in `docs/DECISIONS.md`.
- Use `ops/QUALITY_GATES.md` + `.github/workflows/ci.yml` as merge-blocking quality/security gates.
- Keep `docs/PRIVACY.md` and `docs/THREAT_MODEL.md` updated as features evolve.
- Treat governance files (`ops/`, `.github/`, and core governance docs) as protected; only edit them when necessary and log why in `CHANGELOG_AI.md`.
- Use `ops/prompts/SESSION_RESUME.md` when resuming context or switching AI agents.

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
