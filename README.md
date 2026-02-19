# Project Governance Template

Enterprise-ready project scaffold with AI governance, security policies, anti-drift controls, and audit logging.

## What this repo provides
- Canonical AI policy: `ops/AI_WORKFLOW.md`
- VS Code Copilot policy loader: `.github/copilot-instructions.md`
- Governance scaffold: `ops/` and `docs/`
- AI change log: `CHANGELOG_AI.md`
- Environment template: `.env.example`

## How to use
1) Click **Use this template** to create a new repo from this template.
2) Open the new repo in your IDE.
3) Follow `ops/AI_WORKFLOW.md` for workflow and safety rules.
4) Update `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` for the specific project.

## Notes
- Never commit `.env`. Only commit `.env.example`.
