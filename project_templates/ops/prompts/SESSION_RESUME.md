# Session Resume Prompt

Version: 2.1
Last Updated: 2026-03-09

Use this file only when a session did not start with an explicit governance-loading first prompt.

## Section 1 - Preferred Restart Prompt

Paste or adapt this at the start of a new session:

```text
Before anything else this session: use the current working-tree governance files, not older committed or remote copies. Read docs/FILE_MAP.md, AGENTS.md, and ops/AI_WORKFLOW.md first. Run the Workstation Context Check from ops/AI_WORKFLOW.md before implementation and before treating this as a safe resume. Compare the current repo root path, OS/shell/runtime context, .venv_run health when relevant, git hooksPath, and any absolute-path or local-overlay assumptions from prior notes. If any of those changed or cannot be confirmed, treat this as a workstation change and re-adopt local commands, path assumptions, hooks, and file mapping before feature work. If this task touches paid/free or entitlement boundaries and guides/TIERING_POLICY.local.md or guides/TIERING_POLICY.md exists, read it too. Then open only the files needed for this task, and if resuming, read only the newest relevant CHANGELOG_AI.md entry. If this task affects features, phases, public UX, entitlement, or release QA, produce a dual-lens plan (Technical Builder POV plus User/Consumer POV) and at least one concrete risk with mitigation before implementing. If this task affects paid access, legal, privacy, or policy wording, also read docs/PRIVACY.md and docs/TERMS.md. If required human practical testing remains after AI-runnable verification, mark the work Awaiting human validation and pause for the user's result. My task: [TASK]
```

## Section 2 - Minimum Resume Rules

> **Note:** The First-Session Plan Gate does not apply on resume - it only fires when [redacted-tiering-item] is missing and CHANGELOG_AI has no entries (Tier1 scaffold feature).

- Treat `ops/AI_WORKFLOW.md` as canonical.
- Use `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md` as thin loaders, not competing policy sources.
- Run the `Workstation Context Check` before reading recent work as if it is still safe local context.
- Keep initial context small and expand only when the workflow triggers require it.
- If a tiering overlay exists and the task touches paid/free or entitlement boundaries, read it before editing.
- For local app or test work, prefer repo-local `.venv_run` and `python -m ...` commands.
- Never read or modify `.env`; only update `.env.example`.
- Treat governance files as protected and do not overwrite them without approval.
- If required human practical testing remains after `AI-runnable verification`, mark the work `Awaiting human validation` and pause.
- Close every task with applicable checks plus a `CHANGELOG_AI.md` entry in real projects created from this scaffold.

## Section 3 - Resume Handoff Format

When continuing previous work, keep the handoff compact:

```text
Objective: [what is being completed]
Completed: [done items only]
Next: [single best next action]
Blockers/Risks: [only active blockers or residual risk]
Files: [only touched or immediately relevant files]
Verification: [checks run or still required]
```
