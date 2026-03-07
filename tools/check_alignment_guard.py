import argparse
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, Set


ROOT_DOC_FILES: Set[str] = {
    "README.md",
    "RELEASE_NOTES.md",
    "guides/AI_Project_Workflow_Guide.md",
}

FREE_FORBIDDEN_TEMPLATE_PATHS: Set[str] = {
    "project_templates/.cursor",
    "project_templates/.windsurf",
    "project_templates/.clinerules",
    "project_templates/docs/IDE_ENFORCEMENT.md",
    "project_templates/docs/[redacted-tiering-item].md",
    "project_templates/docs/[redacted-tiering-item].md",
    "project_templates/docs/[redacted-tiering-item]",
    "project_templates/ops/prompts/[redacted-tiering-item].md",
}

FREE_FORBIDDEN_TERMS: Dict[str, Set[str]] = {
    "project_templates/ops/AI_WORKFLOW.md": {
        "Run Bootstrap gate",
    }
}

# Small mapping table: when a template path changes, at least one mapped root doc
# must also change in the same PR.
ALIGNMENT_EXACT_MAP: Dict[str, Set[str]] = {
    "project_templates/README.md": {"README.md"},
    "project_templates/ops/AI_WORKFLOW.md": {
        "README.md",
        "guides/AI_Project_Workflow_Guide.md",
    },
    "project_templates/ops/prompts/SESSION_RESUME.md": {
        "RELEASE_NOTES.md",
        "guides/AI_Project_Workflow_Guide.md",
    },
    "project_templates/ops/prompts/code_review.md": {
        "RELEASE_NOTES.md",
        "guides/AI_Project_Workflow_Guide.md",
    },
    "project_templates/ops/prompts/[redacted-tiering-item].md": {
        "README.md",
        "RELEASE_NOTES.md",
        "guides/AI_Project_Workflow_Guide.md",
    },
}

ALIGNMENT_PREFIX_MAP: Dict[str, Set[str]] = {
    "project_templates/ops/": {"RELEASE_NOTES.md", "guides/AI_Project_Workflow_Guide.md"},
    "project_templates/docs/": {"README.md", "guides/AI_Project_Workflow_Guide.md"},
}


def _git(args: Iterable[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout


def _normalize(path: str) -> str:
    return path.replace("\\", "/").strip()


def _resolve_base(base: str) -> str:
    if base and set(base) == {"0"}:
        return _git(["rev-list", "--max-parents=0", "HEAD"]).splitlines()[0].strip()
    return base


def _changed_files(base: str, head: str) -> Set[str]:
    output = _git(["diff", "--name-only", base, head])
    return {_normalize(line) for line in output.splitlines() if line.strip()}


def _validate_free_tier_invariants() -> list[str]:
    violations: list[str] = []

    for path in sorted(FREE_FORBIDDEN_TEMPLATE_PATHS):
        if Path(path).exists():
            violations.append(f"Free tier must not contain `{path}` (tier1-exclusive artifact).")

    for file_path, forbidden_terms in FREE_FORBIDDEN_TERMS.items():
        path_obj = Path(file_path)
        if not path_obj.exists():
            continue
        content = path_obj.read_text(encoding="utf-8")
        for term in sorted(forbidden_terms):
            if term in content:
                violations.append(f"Free tier file `{file_path}` contains tier1-only marker `{term}`.")

    return violations


def _validate(changed: Set[str]) -> list[str]:
    violations: list[str] = []
    violations.extend(_validate_free_tier_invariants())

    template_changed = any(path.startswith("project_templates/") for path in changed)
    if not template_changed:
        return violations

    root_docs_changed = bool(ROOT_DOC_FILES.intersection(changed))
    if not root_docs_changed:
        violations.append(
            "`project_templates/` changed, but no root alignment docs were updated "
            "(`README.md`, `RELEASE_NOTES.md`, or `guides/AI_Project_Workflow_Guide.md`)."
        )

    template_files_changed = sorted(path for path in changed if path.startswith("project_templates/"))
    for template_path in template_files_changed:
        required_roots = ALIGNMENT_EXACT_MAP.get(template_path)
        if required_roots is None:
            required_roots = set()
            for prefix, mapped_roots in ALIGNMENT_PREFIX_MAP.items():
                if template_path.startswith(prefix):
                    required_roots.update(mapped_roots)

        if required_roots and not (required_roots & changed):
            expected = ", ".join(f"`{item}`" for item in sorted(required_roots))
            violations.append(f"`{template_path}` changed without corresponding root update ({expected}).")

    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Fail when project_templates updates are not accompanied by root-level "
            "alignment documentation updates."
        )
    )
    parser.add_argument("--base", required=True, help="Base git SHA")
    parser.add_argument("--head", required=True, help="Head git SHA")
    args = parser.parse_args()

    base = _resolve_base(args.base)
    head = args.head

    try:
        changed = _changed_files(base, head)
    except Exception as exc:  # pragma: no cover - defensive for CI shell variance
        print(f"Alignment guard failed to compute changed files: {exc}", file=sys.stderr)
        return 2

    violations = _validate(changed)
    if not violations:
        print("Alignment guard passed.")
        return 0

    print("Alignment guard failed:")
    for item in violations:
        print(f"- {item}")

    print("Changed files:")
    for path in sorted(changed):
        print(f"  - {path}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
