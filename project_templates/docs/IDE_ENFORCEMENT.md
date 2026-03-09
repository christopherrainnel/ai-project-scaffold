# IDE-Native Enforcement

This scaffold includes repo-native enforcement files to reduce workflow drift where current tools support them.

## Enforcement Model

- Primary where supported: `.claude/settings.json`, `.cursor/rules/`, `.windsurf/rules/`, and `.clinerules/`.
- Canonical policy: `ops/AI_WORKFLOW.md` stays the source of truth.
- Fallback/shared onboarding: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, and `ops/prompts/SESSION_RESUME.md`.
- Tool-specific loaders should stay tool-specific and easy for their host app to prioritize, but they should remain thin and point back to the canonical workflow instead of copying it.
- During active editing sessions, the current working-tree governance files are authoritative; agents should not defer to older committed or remote copies.
- Copilot coverage is helpful but weaker than native rule and hook systems.

## Included Package

| Path | Purpose |
|------|---------|
| `.claude/settings.json` | Shared Claude Code permission policy to hide `.env` files and ask before risky shell operations |
| `.cursor/rules/00-governance.mdc` | Always-on Cursor rule that reinforces scaffold workflow expectations |
| `.windsurf/rules/00-governance.md` | Lightweight workspace rule for Windsurf |
| `.clinerules/01-governance.md` | Base Cline workspace rule |
| `.clinerules/hooks/TaskStart` | Example project hook that injects governance context at task start |
| `.clinerules/hooks/PreToolUse` | Example project hook that blocks `.env` access and obvious destructive commands |

## VS Code Baseline Extensions

Use this lightweight baseline for local feedback in VS Code:

- Core (big-company publishers): `ms-python.python`, `ms-python.vscode-pylance`, `GitHub.vscode-pull-request-github`, `GitHub.vscode-github-actions`, `ms-vscode.powershell`, `redhat.vscode-yaml`
- Vetted niche (2 only): `charliermarsh.ruff`, `SonarSource.sonarlint-vscode`
- Optional AI layer (not baseline-required): `GitHub.copilot`, `GitHub.copilot-chat`

Signal mapping to current governance gates:

- Python + Pylance + Ruff improve local lint/format/type readiness before CLI checks.
- SonarLint adds early local bug and security-smell triage before PR.
- GitHub PR/Actions extensions improve CI and PR visibility in-editor.

Rule: editor extensions assist quality and security feedback, but do not replace required CLI and CI gates in `ops/QUALITY_GATES.md`.

## Portable Hardwiring Profile (Optional)

To reduce setup drift with low compatibility risk, this scaffold ships optional local assets:

- `.vscode/extensions.json` for editor recommendations only.
- `.vscode/settings.json` for low-noise defaults with Python-specific behavior scoped under `[python]`.
- `scripts/local_preflight_advisory.py` as advisory preflight (warning-first).
- `.githooks/pre-commit.advisory` as an optional wrapper hook.

Default behavior is advisory-only (`exit 0` on warnings). Strict enforcement is opt-in via `SCF_STRICT_LOCAL_CHECKS=1`.

Compatibility if/else profile:

- If Python indicators exist (`pyproject.toml` or `requirements*.txt`), Python advisories run.
- Else, Python-specific advisories are skipped.
- If hooks are not enabled (`git config --get core.hooksPath`), no blocking behavior is introduced.
## Scaffold Rules

- Keep the scaffold fresh, generic, and ready for a user's new AI-assisted project.
- Use accurate language: these files auto-load where supported and reduce workflow drift; they do not guarantee perfect enforcement in every tool.
- Optional installer support and wrapper/runtime enforcement belong to later product phases, not the baseline template.


