# Dependency Policy
Version: 1.0
Last Updated: 2026-02-19

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
