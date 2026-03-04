#!/usr/bin/env python3
"""
Build project_scaffold.exe
==========================
Bundles tools/scaffold_project.py into a single standalone .exe
using PyInstaller. The .exe is placed in the repo root.

Prerequisites:
    pip install pyinstaller

Usage:
    python build_exe.py
"""

import subprocess
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "tools" / "scaffold_project.py"
EXE_NAME = "project_scaffold"
DIST_DIR = ROOT / "dist"
BUILD_DIR = ROOT / "build"


def main():
    # Verify PyInstaller is installed
    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    print(f"\n=== Building {EXE_NAME}.exe ===\n")
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--onefile",
            "--name",
            EXE_NAME,
            "--distpath",
            str(DIST_DIR),
            "--workpath",
            str(BUILD_DIR),
            "--specpath",
            str(BUILD_DIR),
            "--add-data",
            f"{ROOT / 'project_templates'};project_templates",
            "--clean",
            str(SCRIPT),
        ]
    )

    # Move .exe to repo root
    built_exe = DIST_DIR / f"{EXE_NAME}.exe"
    target_exe = ROOT / f"{EXE_NAME}.exe"
    if built_exe.exists():
        shutil.move(str(built_exe), str(target_exe))
        print("\n=== Done! ===")
        print(f"  {target_exe}")
        print(
            "\nUsers can double-click this .exe to scaffold a project in the same folder.\n"
        )
    else:
        print("ERROR: Build succeeded but .exe not found in dist/", file=sys.stderr)
        sys.exit(1)

    # Clean up build artifacts (best-effort; OneDrive may lock folders)
    for d in [DIST_DIR, BUILD_DIR]:
        if d.exists():
            try:
                shutil.rmtree(d)
            except PermissionError:
                print(
                    f"  Note: Could not remove {d.name}/ (may be locked by OneDrive). Safe to delete manually."
                )


if __name__ == "__main__":
    main()
