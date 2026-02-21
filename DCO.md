# Developer Certificate of Origin (DCO)

This repository uses a DCO sign-off check for pull request commits.

By signing off a commit, you certify that you have the right to submit the work under the repository license.

Reference:
- https://developercertificate.org/

## How to Sign Off Commits

Use `-s` when committing:

```bash
git commit -s -m "Your commit message"
```

For existing commits in your branch:

```bash
git rebase --signoff origin/main
```
