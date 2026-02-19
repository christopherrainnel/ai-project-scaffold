# Project Governance & Scaffold Enforcement
**Version:** 1.0
**Last Updated:** 2026-02-19
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
├── AI_WORKFLOW.md          # Rules for how AI interacts with this repo
├── SECURITY_POLICY.md      # Rules for data handling and secrets
├── DATA_CLASSIFICATION.md  # Sensitivity levels of project data
├── DEPENDENCY_POLICY.md    # Rules for adding new libraries
├── QUALITY_GATES.md        # Standards for code to be accepted
├── RELEASE_CHECKLIST.md    # Steps before pushing to production
└── prompts/                # Standardized templates for tasks
    ├── feature_request.md
    ├── bug_report.md
    └── refactor_request.md
docs/
├── ARCHITECTURE.md         # High-level system design
└── DECISIONS.md            # History of "Why" things were built this way

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
