# Dependency Policy

Version: 1.0
Last Updated: {{DATE}}

## Default Stance

Prefer built-in solutions. Every dependency is a maintenance and security liability. Only add one when the cost of writing it yourself clearly outweighs the cost of the dependency.

## Before Adding a Dependency

Answer these questions:

1. **What problem does it solve?**
2. **Can this be done with built-in language/framework features?**
3. **Is the package actively maintained?** (Check: last commit, open issues, bus factor)
4. **What is the license?** (Avoid GPL in proprietary projects; MIT/Apache-2.0 preferred)
5. **What is the install size and dependency tree?** (Avoid packages that pull in hundreds of sub-dependencies)

## Rules

- **Pin exact versions** in the manifest (`package.json`, `requirements.txt`, `pyproject.toml`).
- **Update lockfiles** in the same commit as the dependency change.
- **Run vulnerability scans** after adding or updating dependencies:
  - Node: `npm audit` or `pnpm audit`
  - Python: `pip-audit` or `safety check`
- **Document the justification** in the commit message or in `docs/DECISIONS.md` for significant additions.

## Removing Dependencies

Periodically review for unused packages:
- Node: `npx depcheck`
- Python: `pip-extra-reqs` or manual review

Remove anything that is no longer imported or used.
