# Rule Model

> Starter rule model for a generated governed project.

## Rule Layers

- Core workflow rules from `AGENTS.md`, `docs/FILE_MAP.md`, and `ops/AI_WORKFLOW.md`
- Structured policy packs from `docs/POLICY_PACKS.json`
- Tool profiles from `docs/TOOL_ALLOWLIST_PROFILES.json`
- Optional project-specific rules when the operator adds them

## Rule Intent

Rules should:
- require planning before risky work
- prefer small, reviewable diffs
- protect governance files and secrets
- guide verification and documentation closeout

## Editing Rule Boundaries

- Keep rules specific, reviewable, and easy to verify
- Do not add project-specific claims until the operator defines them
