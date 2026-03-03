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

Current task:
{{CURRENT_TASK}}

Relevant files (if known):
{{RELEVANT_FILES}}

Output format:
1. Short plan
2. Risks/assumptions
3. Minimal file reads to begin