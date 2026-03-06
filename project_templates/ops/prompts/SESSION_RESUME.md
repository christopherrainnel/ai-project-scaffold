# Session Resume (All AI Agents)

Use this template when restarting context or handing off work between AI agents.

## Section 1 - GOVERNANCE BOOT (Required Copy/Paste)

Copy/paste this block at the start of every AI session:

```text
Before anything else this session: read docs/FILE_MAP.md, AGENTS.md, and ops/AI_WORKFLOW.md -
follow the governance rules you find there. For any feature or phase work, produce a dual-lens
plan (Technical Builder POV + User/Consumer POV) and at least one risk with mitigation before
implementing. My task: [REPLACE WITH ACTUAL TASK]
```

<details>
<summary>Expanded Cold-Start Version (Optional)</summary>

## Prompt Template

Resume this project session using strict context minimization.

Rules:
- Do not load the full codebase.
- Load at most 3 source files initially.
- Expand only if needed and explain why.
- Follow governance and security constraints from `ops/AI_WORKFLOW.md`.

Resume sequence (strict order):
1. Read `docs/FILE_MAP.md`
2. Read `ops/AI_WORKFLOW.md`
3. Read the newest `CHANGELOG_AI.md` entry only
4. Read up to 3 task-relevant files
5. Continue from last confirmed next action

Current task:
{{CURRENT_TASK}}

Relevant files (if known):
{{RELEVANT_FILES}}

Handoff block (keep compact):
- Objective:
- Completed:
- Next:
- Risks/Blockers:
- Files touched:

Output format:
1. Short plan
2. Risks/assumptions
3. Minimal file reads to begin

</details>