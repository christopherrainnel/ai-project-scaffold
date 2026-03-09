#!/usr/bin/env python
"""Advisory local preflight for portable scaffold workstations.

Default behavior is warning-only (exit 0).
Set SCF_STRICT_LOCAL_CHECKS=1 to fail on detected risks.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import List


REPO_ROOT = Path(__file__).resolve().parents[1]


def _run_git(args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def _python_indicators(root: Path) -> bool:
    if (root / "pyproject.toml").exists():
        return True
    if any(root.glob("requirements*.txt")):
        return True
    return False


def _is_strict() -> bool:
    return os.getenv("SCF_STRICT_LOCAL_CHECKS", "").strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }


def main() -> int:
    warnings: List[str] = []

    status = _run_git(["status", "--short"])
    if status.returncode == 0 and status.stdout.strip():
        warnings.append("git working tree is not clean")

    fetch = _run_git(["fetch", "--prune"])
    if fetch.returncode != 0:
        warnings.append(
            "git fetch --prune failed (network/auth or remote config issue)"
        )

    upstream = _run_git(["rev-list", "--left-right", "--count", "HEAD...@{upstream}"])
    if upstream.returncode == 0:
        raw = upstream.stdout.strip().split()
        if len(raw) == 2:
            try:
                ahead = int(raw[0])
                behind = int(raw[1])
                if behind > 0:
                    warnings.append(
                        f"local branch is behind upstream by {behind} commit(s)"
                    )
                if ahead > 0:
                    warnings.append(
                        f"local branch is ahead of upstream by {ahead} commit(s)"
                    )
            except ValueError:
                warnings.append("unable to parse upstream divergence counts")

    if _python_indicators(REPO_ROOT):
        if not (
            (REPO_ROOT / ".venv_run" / "Scripts" / "python.exe").exists()
            or (REPO_ROOT / ".venv_run" / "bin" / "python").exists()
        ):
            warnings.append(
                "python indicators found but repo-local .venv_run is missing"
            )
        for tool in ("ruff", "pytest", "mypy"):
            if shutil.which(tool) is None:
                warnings.append(f"python tool not found on PATH: {tool}")

    if warnings:
        print("[scaffold-advisory] Local preflight found issues:")
        for item in warnings:
            print(f"- {item}")
        print(
            "[scaffold-advisory] Advisory mode: continue allowed. Set SCF_STRICT_LOCAL_CHECKS=1 to enforce."
        )
        return 1 if _is_strict() else 0

    print("[scaffold-advisory] Local preflight: no advisory issues detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
