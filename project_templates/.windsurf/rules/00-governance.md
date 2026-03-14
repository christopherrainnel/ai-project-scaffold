# Workspace Governance Rule

- Use the current working-tree governance files in this repo, not older committed or remote copies.
- Plan before code. State what you will change, why, and one concrete risk with mitigation before editing.
- Start with only the files needed for the task, usually 3 or fewer first. Expand only when needed.
- Never read or modify `.env`; update `.env.example` only.
- Never expose secrets, private URLs, keys, or tokens.
- Never run destructive commands or destructive git operations without explicit user approval.
- Never run `git commit` or `git push` without explicit user instruction.
- Never add dependencies without justification, version pinning, and lockfile updates.
- Treat governance files as protected; do not overwrite them without approval.
- Verify after changes with the relevant checks.
- If required human practical testing remains, mark the work `Awaiting human validation` and pause.
- Close completed tasks with a `CHANGELOG_AI.md` entry in real projects created from this scaffold.
- Use `AGENTS.md`, `docs/FILE_MAP.md`, and `ops/AI_WORKFLOW.md` for the full workflow and trigger-based reads.
- For feature, architecture, UX, or release work, also read `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, and `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md`.
- For legal or privacy work, also read `docs/PRIVACY.md` and `docs/TERMS.md`.
- `ops/AI_WORKFLOW.md` remains canonical if anything here is abbreviated or conflicts.
