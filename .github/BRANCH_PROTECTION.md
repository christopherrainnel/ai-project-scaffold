# Branch Protection Checklist (`main`)

Use this checklist in GitHub repository settings to enforce safe merges.

## Recommended Minimum

- [ ] Require a pull request before merging.
- [ ] Require at least 1 approving review.
- [ ] Dismiss stale approvals when new commits are pushed.
- [ ] Require status checks to pass before merging.
- [ ] Require branches to be up to date before merging.
- [ ] Include administrators in these rules.
- [ ] Restrict direct pushes to `main`.

## Status Checks to Require

- [ ] `test (ubuntu-latest, 3.10)`
- [ ] `test (ubuntu-latest, 3.12)`
- [ ] `test (windows-latest, 3.10)`
- [ ] `test (windows-latest, 3.12)`
- [ ] `DCO sign-off check`

## Optional (Recommended for Growth)

- [ ] Require conversation resolution before merging.
- [ ] Require signed commits.
- [ ] Require linear history.
- [ ] Restrict who can dismiss pull request reviews.
