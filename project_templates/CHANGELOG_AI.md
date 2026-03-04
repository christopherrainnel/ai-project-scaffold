# AI Change Log

> Every AI-made change is recorded here. Entries are newest-first.

## Entry Format

```
### YYYY-MM-DD — [Short task description]
**Files**: list of files changed
**Commands**: commands run (or "none")
**Verification**: how the change was verified
**Notes/Risks**: anything to watch out for
```

---

### 2026-03-04 — Enforced CI gates + wording consistency hardening

**Files**: `.github/workflows/ci.yml`, `project_templates/.github/workflows/ci.yml`, `README.md`, `project_templates/README.md`, `project_templates/ops/AI_WORKFLOW.md`, `project_templates/ops/QUALITY_GATES.md`, `build_exe.py`, `tools/scaffold_project.py`, `project_templates/CHANGELOG_AI.md`
**Commands**: `python -m ruff check ...`; `python -m ruff format --check ...`; `mypy --ignore-missing-imports --no-strict-optional ...`; `python -m bandit -r ... -lll`; `python -m unittest discover -s tests -v`; `git grep` mismatch checks
**Verification**: Local lint/format/typecheck/SAST/tests pass; template CI and embedded fallback CI now remove non-blocking behavior and enforce configured/applicable gates.
**Notes/Risks**: Template dependency audit relies on dependency manifests (`requirements*.txt` or `pyproject.toml`) to provide actionable vulnerability scanning.

---

### 2026-03-04 — Repo alignment: CI-policy wording, roadmap, and release trust note

**Files**: `README.md`, `project_templates/README.md`, `project_templates/ops/AI_WORKFLOW.md`, `project_templates/ops/QUALITY_GATES.md`, `tools/scaffold_project.py`, `project_templates/CHANGELOG_AI.md`
**Commands**: `git grep` consistency checks; `python -m unittest discover -s tests -v`
**Verification**: Confirmed docs no longer overstate merge-blocking gates versus test-only CI baseline; sponsorship links remained consistent in scoped files.
**Notes/Risks**: Additional gates (lint/typecheck/scan/SAST) remain recommended and require explicit CI configuration to become enforced.

---

### {{DATE}} — Project scaffold created

**Files**: All governance, docs, and config files.
**Commands**: `python scaffold_project.py` (or manual setup)
**Verification**: Manual review of generated files.
**Notes/Risks**: Initial baseline. Fill in `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` next.

---

<!-- Add new entries above this line, newest first -->
