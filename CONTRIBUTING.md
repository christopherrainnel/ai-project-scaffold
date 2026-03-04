# Contributing

## Ground Rules

- Be respectful and constructive.
- Keep pull requests focused and small.
- Avoid unrelated formatting-only changes.
- Never commit secrets (`.env`, keys, tokens, credentials).

## Roles and Trust Model

- `Maintainer`: repository admin/write member responsible for final merge decisions.
- `Approved contributor`: a community member granted elevated repository permissions by maintainers after consistent, high-quality contributions.
- `External contributor`: any contributor without elevated repository permissions.

All changes to `main` must go through pull requests and maintainer review.

## License and Compensation Terms

By submitting a contribution (including pull requests, commits, or patches), you agree that:

- Your contribution is provided under this repository's license (`LICENSE`).
- You have the legal right to submit the contribution.
- The maintainers may use, modify, and redistribute your contribution under that license on a royalty-free, no-charge basis.
- No payment or other compensation is owed for your contribution unless a separate written agreement is made in advance with the maintainers.

## DCO Sign-Off Requirement

This repository requires DCO sign-off on pull request commits.

- Add sign-off when committing: `git commit -s -m "message"`
- If needed, re-sign existing commits: `git rebase --signoff origin/main`
- See `DCO.md` for details.

## Development Setup

1. Fork and clone the repository.
2. Create a feature branch from `main`.
3. Use Python 3.8+.
4. Run tests before opening a pull request:

```bash
python -m unittest discover -s tests -v
```

## Issue and PR Workflow

- Use `.github/ISSUE_TEMPLATE/01-bug-report.yml` for bugs.
- Use `.github/ISSUE_TEMPLATE/02-feature-request.yml` for feature proposals.
- Use `.github/PULL_REQUEST_TEMPLATE.md` for pull requests.

## Pull Request Checklist

- [ ] Change is scoped to one purpose.
- [ ] Documentation updated if behavior changed.
- [ ] If `project_templates/` changed, update at least one root alignment doc (`README.md`, `RELEASE_NOTES.md`, or `guides/AI_Project_Workflow_Guide.md`) to reflect the feature change.
- [ ] Follow template-to-root mapping expectations enforced by `tools/check_alignment_guard.py` (file-specific alignment checks).
- [ ] Tests added or updated where relevant.
- [ ] `project_templates/` and `tools/scaffold_project.py` remain in sync (`project_templates/` is source of truth; update scaffold script to match).
- [ ] No secrets or credentials introduced.
- [ ] This contribution follows current official platform/documentation guidance where applicable.

## Commit Guidance

- Use clear, imperative commit messages (example: `Add CI check for template parity`).
- Reference issues when applicable.

## Security Issues

Do not open public issues for vulnerabilities. Follow `SECURITY.md`.
