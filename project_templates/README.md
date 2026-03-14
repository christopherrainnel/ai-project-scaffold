# {{PROJECT_NAME}}

> Built with AI-assisted development using a governed starter scaffold.

## Tier Scope

This starter is the `free` template.
It includes the safety, maintenance, and governance baseline needed for a professional project start.
It does not include tier1 bootstrap-planning artifacts.

## Quick Start

1. Open the repo in your IDE.
2. If the project needs local environment values, copy `.env.example` to `.env` and fill them in.
3. Read `AGENTS.md`.
4. Read `docs/FILE_MAP.md`.
5. Read `ops/AI_WORKFLOW.md`.
6. Start building with small, reviewable tasks.

## IDE-Native Enforcement

This starter includes repo-native governance loaders for Claude, Cursor, Windsurf, Cline, and Copilot.
`ops/AI_WORKFLOW.md` remains canonical.

## Project Structure

- `docs/` - architecture, decisions, file map, privacy, terms, threat model
- `ops/` - workflow, quality gates, security/data/dependency policy, prompts
- `scripts/` - local advisory helpers
- `.github/` - CI and contribution templates

## Key Rules

- Never commit `.env`.
- Log AI-delivered work in `CHANGELOG_AI.md`.
- Put durable choices in `docs/DECISIONS.md`.
- Use `ops/QUALITY_GATES.md` before treating work as done.
- Treat governance files as protected.
