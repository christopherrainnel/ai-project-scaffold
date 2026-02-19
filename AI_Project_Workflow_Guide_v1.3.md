# AI Project Workflow Guide (v1.3 — scripted scaffold)

Version: 1.3  
Last Updated: 2026-02-19  
Owner: Project Lead  

---

## What changed in this version

This guide is updated to match the **current automated scaffold generator** (`scaffold_project.py`) and the current directory expectations.

Key updates reflected from the script:
- Adds a robust **`.gitignore`** at repo root.
- Adds **`ops/LESSONS_LEARNED.md`** and updates workflow to store repeatable learnings there.
- Uses **`AGENTS.md`** as the **read-first agent rules pointer** (root-level).
- Keeps environment creation **out of scope for now**: the `--venv` feature is present but fully commented out (not executed).  

---

## Your working mode

Primary workflow: **Local-first** (projects live on your PC / synced drive).  
Tools: Cursor (primary) + VS Code (fallback).  
Governance is enforced by files **inside the project folder**.

---

## Standard project scaffold (current)

Created by `scaffold_project.py`:

```text
README.md
AGENTS.md
CHANGELOG_AI.md
.env.example
.gitignore
.github/
  copilot-instructions.md
docs/
  ARCHITECTURE.md
  DECISIONS.md
ops/
  AI_WORKFLOW.md
  SECURITY_POLICY.md
  DATA_CLASSIFICATION.md
  DEPENDENCY_POLICY.md
  QUALITY_GATES.md
  RELEASE_CHECKLIST.md
  LESSONS_LEARNED.md
  prompts/
    feature_request.md
    bug_report.md
    refactor_request.md
```

Notes:
- `AGENTS.md` is at the **repo root** and is meant to be seen early by agents/tools.
- `ops/LESSONS_LEARNED.md` is intentionally lightweight; only store lessons that are likely to repeat.

---

## Canonical “rules” order (practical)

When an agent starts work, it should read in this order:

1) `AGENTS.md` (read-first pointer + learning preference)  
2) `ops/AI_WORKFLOW.md` (canonical operational policy)  
3) `.github/copilot-instructions.md` (VS Code Copilot loader / enforcement wrapper)  
4) `docs/ARCHITECTURE.md` + `docs/DECISIONS.md` (anti-drift anchors)

---

## Expected daily development flow

For every task:

1) You describe the objective to the agent.  
2) Agent produces a short plan (files it will touch).  
3) Agent edits files in small, reviewable diffs.  
4) Agent runs checks if applicable (lint/test/build).  
5) You review the change.  
6) Agent updates:
   - `CHANGELOG_AI.md` (what changed + verification)
   - `ops/LESSONS_LEARNED.md` (only if the issue will likely repeat)

---

## Security rules (non-negotiable)

- Never paste secrets into chat.  
- Secrets go only in `.env` locally (never committed).  
- Only `.env.example` is committed (placeholders only).  
- Never run destructive terminal commands without explicit approval.

`.gitignore` is part of the scaffold to prevent accidental commits of secrets, caches, and build artifacts.

---

## Anti-drift rules

Before implementing major changes:
- Read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
- If the requested change conflicts with documented direction, stop and ask.

---

## How to use the scaffold generator (automation)

The generator supports these modes:

### Create scaffold in the current directory
```bash
python scaffold_project.py
```

### Create scaffold in a specific directory
```bash
python scaffold_project.py /path/to/project
```

### Create a new project folder and scaffold inside it
```bash
python scaffold_project.py --name my-project
```

### Preview what would happen (no files written)
```bash
python scaffold_project.py --dry-run
```

### Overwrite existing files (use carefully)
```bash
python scaffold_project.py --force
```

Default behavior is safe: **if a file exists, it is skipped** unless `--force` is used.

---

## Environment creation is not enabled yet

The script contains a planned `--venv` feature, but it is **fully commented out** and currently does nothing.  
When you decide to enable it later, you will:
- uncomment imports and argparse flag
- uncomment the venv creation logic
- then run with `--venv`

Until then: treat environment creation as **out of scope**.

---

## What you should do now (minimum)

1) Keep `scaffold_project.py` in your template folder/repo.  
2) Use it to create new projects consistently.  
3) For each new project, immediately fill:
   - `docs/ARCHITECTURE.md`
   - `docs/DECISIONS.md`
   - `ops/QUALITY_GATES.md` (stack-specific commands)

---

## Appendix: What’s inside the automation script (reference)

- The scaffold file map is defined in `FILES = { ... }`, including `.gitignore`, `.env.example`, and governance docs.  
- `ops/AI_WORKFLOW.md` includes the “lessons learned” logging rule and points to `ops/LESSONS_LEARNED.md`.  
- Virtual environment creation is present but disabled (commented out).  
