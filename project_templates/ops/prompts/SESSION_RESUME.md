# Session Resume (All AI Agents)

Use this template when restarting context or handing off work between AI agents.

## Prompt Template

Resume this project session using strict context minimization.

Read order:
1. `docs/FILE_MAP.md`
2. `ops/AI_WORKFLOW.md`
3. Only the files required for the current task

Rules:
- Do not load the full codebase.
- Load at most 3 source files initially.
- Expand only if needed and explain why.
- Follow governance and security constraints from `ops/AI_WORKFLOW.md`.

Strict resume sequence:
1. Confirm latest entry in `CHANGELOG_AI.md` relevant to the task.
2. Restate the next concrete action in one sentence.
3. Read only files required to execute that next action.

Current task:
{{CURRENT_TASK}}

Relevant files (if known):
{{RELEVANT_FILES}}

Compact handoff block (optional):
```
Last completed step:
Next action:
Open risks/assumptions:
Required files (max 3 to start):
```

Output format:
1. Short plan
2. Risks/assumptions
3. Minimal file reads to begin