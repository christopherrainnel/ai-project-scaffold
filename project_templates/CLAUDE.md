# Project Rules (Claude Code)

> Claude Code reads this file automatically.
> Use it together with `.claude/settings.json`. For full policy, see `ops/AI_WORKFLOW.md`.
> During active editing sessions, use the current working-tree versions of governance files.

## Claude Startup

1. Read this file.
2. Read `docs/FILE_MAP.md`.
3. Read `ops/AI_WORKFLOW.md`.
4. If the task touches paid/free or entitlement boundaries and a local overlay exists, read `guides/TIERING_POLICY.local.md` or `guides/TIERING_POLICY.md`.
5. Run the `Workstation Context Check` from `ops/AI_WORKFLOW.md` before safe resume.
6. If needed, read the newest relevant `CHANGELOG_AI.md` entry only.

If the session did not begin with a governance-loading prompt, use `ops/prompts/SESSION_RESUME.md` Section 1.

## Claude-Specific Enforcement

- `ops/AI_WORKFLOW.md` remains canonical.
- If required human practical testing remains after `AI-runnable verification`, mark the work `Awaiting human validation` and pause.
- Keep this loader thin; do not restate the full policy here.
