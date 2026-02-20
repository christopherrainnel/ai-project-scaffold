#!/usr/bin/env python3
#
# This script creates or updates a governed AI project scaffold.
# Default behavior is safe (no overwrites).
# Use --force only when intentionally resetting governance files.
#
"""
Project Governance Scaffold Generator
======================================
Replicates the standard project template structure with all governance files,
docs, prompts, and configuration. Run this to bootstrap a new project.

Usage:
    python scaffold_project.py                     # creates in current directory
    python scaffold_project.py /path/to/project    # creates in specified directory
    python scaffold_project.py --name my-project   # creates ./my-project/ folder
    python scaffold_project.py --dry-run            # preview without writing
    python scaffold_project.py --force              # overwrite existing files
    python scaffold_project.py --venv               # also create .venv (uncomment to enable)
"""

import os
import sys
import argparse
# import subprocess  # uncomment when enabling --venv
# import venv        # uncomment when enabling --venv
from pathlib import Path
from datetime import date

TODAY = date.today().strftime("%Y-%m-%d")

# ---------------------------------------------------------------------------
# File contents — each key is a relative path, value is the file body.
# Dates use TODAY so the scaffold is always fresh.
# ---------------------------------------------------------------------------

FILES = {

# ── Root files ────────────────────────────────────────────────────────────

"README.md": """\
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
""",

"AGENTS.md": """\
# Agent Rules (Read First)

If you are an AI agent or IDE assistant:

1. Read `PROJECT_GOVERNANCE.md`
2. Then read `ops/AI_WORKFLOW.md`
3. Then follow `.github/copilot-instructions.md` (if applicable)

Do not:
- Overwrite governance files without showing a diff and receiving approval
- Modify `.env`
- Introduce dependencies without justification

Governance files are authoritative.
""",

"CHANGELOG_AI.md": f"""\
# AI Change Log

## Format
Date \u2014 Task \u2014 Files Changed \u2014 Commands Run \u2014 Verification \u2014 Notes/Risks

### {TODAY} \u2014 Scaffold installed
Files: ops/*, docs/*, .env.example, CHANGELOG_AI.md
Commands: (none)
Verification: Manual review
Notes: Initial governance baseline
""",

".env.example": """\
# Copy to .env and fill values locally. Do not commit .env.

# Examples (leave blank values):
# API_KEY=
# DATABASE_URL=
# NODE_ENV=development
""",

".gitignore": """\
# Secrets
.env
.env.*
!.env.example

# OS / Editor
.DS_Store
Thumbs.db
*.swp
*.swo
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json
!.vscode/launch.json
.idea/
*.iml

# Logs
*.log
npm-debug.log*
yarn-debug.log*
pnpm-debug.log*

# Build / cache (common)
dist/
build/
out/
.cache/
tmp/
temp/

# Node (common web)
node_modules/
.next/
.vercel/
coverage/

# Python (common data)
__pycache__/
*.py[cod]
.venv/
venv/
.ipynb_checkpoints/

# Excel/VBA exports/backups
~$*.xls*
*.tmp
""",

# ── .github ────────────────────────────────────────────────────────────────

".github/copilot-instructions.md": f"""\
# Project Governance & Scaffold Enforcement
**Version:** 1.0
**Last Updated:** {TODAY}
**Owner:** Project Lead

---

Canonical policy: If `ops/AI_WORKFLOW.md` exists, it is the source of truth; if any conflict arises, stop and ask the user.

## 0. Activation & Audit Rules

### Activation Rule
On session start or first task:
1. Check if the `/ops` folder exists.
2. If missing, **stop and ask the user**:
   > "This workspace does not contain the standard governance scaffold. Do you want me to install it (recommended for production-grade projects) or skip (for small/simple projects like VBA/data analysis)?"
3. **Action:** If approved, proceed with setup. If declined, continue without enforcement.

### Audit Rule (Self-Healing)
On opening any workspace, verify that all required governance files and folders listed in Section 1 exist. If any are missing or have been deleted, immediately trigger the **Activation Rule** workflow to restore the environment integrity.

---

## 1. Required Scaffold Structure
The following directory and file structure **must** be maintained:

```text
ops/
\u251c\u2500\u2500 AI_WORKFLOW.md          # Rules for how AI interacts with this repo
\u251c\u2500\u2500 SECURITY_POLICY.md      # Rules for data handling and secrets
\u251c\u2500\u2500 DATA_CLASSIFICATION.md  # Sensitivity levels of project data
\u251c\u2500\u2500 DEPENDENCY_POLICY.md    # Rules for adding new libraries
\u251c\u2500\u2500 QUALITY_GATES.md        # Standards for code to be accepted
\u251c\u2500\u2500 RELEASE_CHECKLIST.md    # Steps before pushing to production
\u2514\u2500\u2500 prompts/                # Standardized templates for tasks
    \u251c\u2500\u2500 feature_request.md
    \u251c\u2500\u2500 bug_report.md
    \u2514\u2500\u2500 refactor_request.md
docs/
\u251c\u2500\u2500 ARCHITECTURE.md         # High-level system design
\u2514\u2500\u2500 DECISIONS.md            # History of "Why" things were built this way

CHANGELOG_AI.md             # Automated log of all AI modifications
.env.example                # Template for environment variables
```

---

## 2. Enforcement Rules
* **No Overwrites:** If a required folder/file already exists, **DO NOT** overwrite it.
* **Auto-Creation:** If a file is missing from the required scaffold, create it.
* **Update Protocol:** If a file exists but is outdated, show a `diff` and ask the user for permission before modifying.
* **Safety:** Never delete user content. Never modify or read the actual `.env` file (only `.env.example`).

---

## 3. Agent Operating Constraints
When performing tasks, the AI Agent must strictly follow these rules:

### Security & Safety
* **Secrets:** Never request or expose API keys, passwords, or secrets.
* **Environment:** Never paste or log environment variables in chat or logs.
* **Commands:** Never run destructive terminal commands without explicit user approval.

### Code Integrity
* **Dependencies:** Never add a dependency without justification. Always **pin versions** and update lockfiles immediately.
* **Planning:** Always produce a short, step-by-step plan before making multi-file edits.
* **Verification:** Always run `lint`, `test`, or `build` after changes (if tools are available).
* **Version Control:** Commit changes in small, atomic diffs.
* **Logging:** Document every change made in `CHANGELOG_AI.md`.

### Learning & Communication
* **Plain English Explanations:** Always explain the "Why" behind JavaScript errors in plain English, comparing them to Python or Data Science concepts where possible (e.g., comparing JS `Promises` to Python `Asyncio` or JS `Array.map` to Pandas `.apply()`).

---

## 4. Anti-Drift Control
Before implementing any feature or fix:
1. Read `docs/ARCHITECTURE.md`.
2. Read `docs/DECISIONS.md`.
3. Confirm that the proposed changes align with the documented project direction.
4. **If a conflict arises:** Stop and ask the user for clarification before proceeding.

---

## 5. Definition of Done (DoD)
A task is considered **Complete** only if:
- [ ] Code successfully compiles and builds.
- [ ] Linting passes without errors.
- [ ] Tests pass (if applicable).
- [ ] `CHANGELOG_AI.md` is updated with a summary of the work.
- [ ] No secrets or hardcoded credentials were introduced.
- [ ] No dependency drift (lockfiles are synced).
""",

# ── docs/ ──────────────────────────────────────────────────────────────────

"docs/ARCHITECTURE.md": f"""\
# Architecture
Version: 0.1
Last Updated: {TODAY}

## Overview
Describe the system at a high level.

## Components
- UI:
- API:
- Data:
- Integrations:

## Data Flow
Describe how data moves through the system.

## Security Notes
Where secrets live, where auth happens, sensitive boundaries.

## Environments
Local / staging / production differences.
""",

"docs/DECISIONS.md": f"""\
# Decisions (Why Log)
Version: 0.1
Last Updated: {TODAY}

## Format
Date \u2014 Decision \u2014 Why \u2014 Alternatives Considered \u2014 Tradeoffs

### {TODAY} \u2014 Governance scaffold adopted
Why: Reduce drift, improve auditability, enforce secure defaults.
Alternatives: Ad-hoc instructions per project.
Tradeoffs: Slight upfront setup, large reduction in long-term risk.
""",

# ── ops/ ───────────────────────────────────────────────────────────────────

"ops/AI_WORKFLOW.md": f"""\
# AI Workflow (Canonical Policy)
Version: 1.0
Last Updated: {TODAY}
Owner: Project Lead

## Purpose
This file is the canonical governance policy for this repository and must be followed by any AI agent or IDE assistant (VS Code, Cursor, Windsurf, others).

## Session Start: Audit Rule
On opening this workspace (or first task):
1) Verify required governance scaffold exists (see "Scaffold Checklist").
2) If missing items exist, ask:
   "This workspace is missing governance scaffold items. Do you want me to install the missing pieces (recommended) or skip (for small/simple projects)?"
3) If approved: create missing items only. Do not overwrite existing files unless user approves a diff.
4) If a required file exists, do not overwrite it. Only propose updates via diff and request approval.
5) At least once per major milestone, run the Workspace Governance Audit prompt.

## Operating Mode (Required)
1) Plan first (short, step-by-step). Name the files to be changed.
2) Make small, reviewable edits. Avoid unrelated reformatting.
3) Run quality gates (lint/test/build) if available.
4) Summarize: what changed, why, how verified, risks, and next check.
5) Store and add "lesson learned" snippets in 'ops/LESSONS_LEARNED.md' when the issue is likely to repeat.
6) Log the work in `CHANGELOG_AI.md`.

## Safety Rules (Non-Negotiable)
- Secrets: never request, paste, store, or echo secrets (keys, tokens, passwords).
- `.env`: never read or modify `.env`. Only update `.env.example`.
- Terminal: never run destructive commands; require explicit approval for any command execution.
- Data: never request customer PII or sensitive internal data; request redacted/sanitized samples.

## Dependency Discipline
- Do not add dependencies unless justified (why needed, alternatives considered).
- Pin versions and update lockfiles immediately.
- Run vulnerability checks if available (e.g., npm audit/pip-audit) when dependencies change.

## Anti-Drift Control
Before implementing changes:
- Read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
- If proposed work conflicts with recorded decisions, stop and ask.

## Scaffold Checklist
Required paths:
- ops/* (all governance files)
- ops/prompts/*
- docs/ARCHITECTURE.md
- docs/DECISIONS.md
- CHANGELOG_AI.md
- .env.example\
""",

"ops/SECURITY_POLICY.md": f"""\
# Security Policy
Version: 1.0
Last Updated: {TODAY}

## Goals
Prevent secret leakage, unsafe command execution, and accidental inclusion of sensitive data.

## Secrets
- Store secrets ONLY in `.env` (local) or platform secret managers.
- Never commit `.env`.
- Maintain `.env.example` with placeholder keys only.

## Prohibited Content in Chat/Logs
- API keys, tokens, passwords
- Private URLs containing tokens
- Production database exports
- Customer PII (names, phone, email, payment info)

## Terminal Safety
- Commands must be explained before execution.
- Require explicit user approval before running commands.
- Never run destructive operations without confirmation (rm -rf, destructive migrations, credential changes).

## Telemetry/Privacy
- Prefer privacy modes where supported.
- Avoid sending proprietary code snippets to third-party services unnecessarily.
""",

"ops/DATA_CLASSIFICATION.md": f"""\
# Data Classification
Version: 1.0
Last Updated: {TODAY}

## Allowed
- Public documentation
- Synthetic/sample data
- Sanitized logs (no secrets, no PII)

## Restricted (Redaction Required)
- Internal strategy, pricing, unpublished roadmaps
- Contracts/vendor terms (share only if redacted)

## Prohibited
- Secrets/credentials
- Customer PII
- Payment details
- Production database dumps
""",

"ops/DEPENDENCY_POLICY.md": f"""\
# Dependency Policy
Version: 1.0
Last Updated: {TODAY}

## Default Stance
Avoid adding dependencies unless necessary.

## Rules
- Justify every new dependency:
  - What problem it solves
  - Why built-in/local code is insufficient
  - Security/maintenance considerations
- Pin versions.
- Update lockfiles on the same change.
- Run vulnerability checks when dependencies change (if tooling exists).
""",

"ops/QUALITY_GATES.md": f"""\
# Quality Gates
Version: 1.0
Last Updated: {TODAY}

## Definition of Done
- Builds successfully (if applicable)
- Lint passes (if applicable)
- Tests pass (if applicable)
- CHANGELOG_AI.md updated
- No secrets introduced
- No dependency drift (lockfiles aligned)

## Commands (fill in per stack)
- Install:
- Lint:
- Test:
- Build:
- Audit (deps):
""",

"ops/RELEASE_CHECKLIST.md": f"""\
# Release Checklist
Version: 1.0
Last Updated: {TODAY}

## Pre-Release
- [ ] All quality gates pass
- [ ] Secrets verified not committed
- [ ] Dependency changes reviewed + audited
- [ ] CHANGELOG_AI.md up to date
- [ ] Key user flows smoke-tested
- [ ] Rollback plan noted (if production)
""",

"ops/LESSONS_LEARNED.md": """\
""",

# ── ops/prompts/ ───────────────────────────────────────────────────────────

"ops/prompts/bug_report.md": """\
# Bug Report (Agent Task)

## Symptom
What is broken? Include exact error text if any (redacted).

## Reproduction Steps
1)
2)

## Expected vs Actual
Expected:
Actual:

## Environment
OS, runtime versions, relevant configs (no secrets).

## Required Fix Verification
- Tests to add or run:
- Commands:
""",

"ops/prompts/feature_request.md": """\
# Feature Request (Agent Task)

## Context
What is the product/system and current behavior?

## Objective
What should change? What is the success criteria?

## Constraints
- Security/compliance constraints
- Performance constraints
- UI/UX constraints

## Acceptance Criteria
- [ ] ...
- [ ] ...

## Required Verification
List commands/tests to run:
- ...
""",

"ops/prompts/refactor_request.md": """\
# Refactor Request (Agent Task)

## Goal
What improvement is desired (readability, performance, modularity)?

## Non-Goals
What must NOT change?

## Constraints
- Must keep existing behavior unless specified
- Avoid large reformatting

## Verification
- Tests/lint/build:
""",

}

# ---------------------------------------------------------------------------
# Virtual environment creation
# ---------------------------------------------------------------------------
# NOTE: This entire section is commented out. When you are ready to use it:
#   1. Uncomment the two imports at the top:  import subprocess  /  import venv
#   2. Uncomment the function body inside create_venv()
#   3. Uncomment the --venv argparse argument in main()
#   4. Uncomment the venv call block in main()
#   Then run:  python scaffold_project.py --name my-project --venv
# ---------------------------------------------------------------------------

def create_venv(target_dir: Path, dry_run: bool = False):
    """
    Create a Python virtual environment (.venv) inside the target directory.
    """
    pass  # Remove this 'pass' when uncommenting the body below.

    # venv_path = target_dir / ".venv"
    #
    # if venv_path.exists():
    #     print(f"  [SKIP] .venv/  (already exists)")
    #     return False
    #
    # if dry_run:
    #     print(f"  [VENV] .venv/  (would create Python virtual environment)")
    #     return True
    #
    # print(f"  [VENV] Creating Python virtual environment at .venv/ ...")
    # venv.create(str(venv_path), with_pip=True)
    #
    # # Determine the pip path (cross-platform)
    # if sys.platform == "win32":
    #     pip_path = venv_path / "Scripts" / "pip.exe"
    #     activate_hint = r".venv\Scripts\activate"
    # else:
    #     pip_path = venv_path / "bin" / "pip"
    #     activate_hint = "source .venv/bin/activate"
    #
    # # Upgrade pip inside the new venv
    # subprocess.run(
    #     [str(pip_path), "install", "--upgrade", "pip"],
    #     check=True,
    #     capture_output=True,
    # )
    #
    # print(f"  [VENV] .venv/ created successfully (pip upgraded)")
    # print(f"         Activate with:  {activate_hint}")
    # return True


# ---------------------------------------------------------------------------
# Generator logic
# ---------------------------------------------------------------------------

def create_scaffold(target_dir: Path, dry_run: bool = False, force: bool = False):
    """Create the full project scaffold under target_dir."""
    target_dir = target_dir.resolve()
    created_dirs = set()
    created_files = []
    skipped_files = []

    for rel_path, content in FILES.items():
        full_path = target_dir / rel_path
        parent = full_path.parent

        # Create directories
        if parent not in created_dirs and not parent.exists():
            if dry_run:
                print(f"  [DIR]  {parent.relative_to(target_dir)}/")
            else:
                parent.mkdir(parents=True, exist_ok=True)
            created_dirs.add(parent)

        # Write file
        if full_path.exists() and not force:
            skipped_files.append(rel_path)
            if dry_run:
                print(f"  [SKIP] {rel_path}  (already exists)")
            continue

        if dry_run:
            print(f"  [FILE] {rel_path}")
        else:
            full_path.write_text(content, encoding="utf-8")
        created_files.append(rel_path)

    return created_files, skipped_files


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new project with governance files and templates."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target directory (default: current directory)",
    )
    parser.add_argument(
        "--name",
        help="Create a sub-folder with this name inside target and scaffold there",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing anything",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files (default: skip existing)",
    )
    # ── Uncomment the block below when ready to enable --venv ──────────────
    # parser.add_argument(
    #     "--venv",
    #     action="store_true",
    #     help="Also create a .venv Python virtual environment in the project",
    # )

    args = parser.parse_args()
    target = Path(args.target)

    if args.name:
        target = target / args.name

    if args.dry_run:
        print(f"\n=== DRY RUN \u2014 scaffold preview for: {target.resolve()} ===\n")
    else:
        print(f"\n=== Scaffolding project at: {target.resolve()} ===\n")
        target.mkdir(parents=True, exist_ok=True)

    created, skipped = create_scaffold(target, dry_run=args.dry_run, force=args.force)

    # ── Uncomment the block below when ready to enable --venv ──────────────
    # venv_created = False
    # if getattr(args, "venv", False):
    #     venv_created = create_venv(target, dry_run=args.dry_run)

    # Summary
    print(f"\n--- Summary ---")
    print(f"  Created : {len(created)} file(s)")
    if skipped:
        print(f"  Skipped : {len(skipped)} file(s) (already exist, use --force to overwrite)")
    # if venv_created:
    #     print(f"  Venv    : .venv/ created")
    if args.dry_run:
        print(f"\n  (No files were written \u2014 this was a dry run)")
    else:
        print(f"\n  Done! Your project scaffold is ready.")
    print()


if __name__ == "__main__":
    main()