# Release Checklist

Version: 1.0
Last Updated: {{DATE}}

## Pre-Release

- [ ] All quality gates pass (lint, test, build)
- [ ] No secrets or credentials in the codebase (`git log --all -p | grep -i "password\|secret\|api_key"`)
- [ ] Dependency changes reviewed and vulnerability-scanned
- [ ] `CHANGELOG_AI.md` is up to date
- [ ] `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` reflect current state
- [ ] Key user flows smoke-tested manually
- [ ] Environment variables documented in `.env.example`
- [ ] Rollback plan documented (for production releases)
- [ ] Database migrations tested (if applicable)
- [ ] Feature flags configured (if applicable)

## Release

- [ ] Tag the release in git (`git tag vX.Y.Z`)
- [ ] Deploy to staging and verify
- [ ] Deploy to production
- [ ] Verify production health (logs, monitoring, key flows)

## Post-Release

- [ ] Monitor error rates and logs for 30 minutes after deploy
- [ ] Confirm rollback plan is still viable
- [ ] Notify stakeholders of the release
- [ ] Close related issues / tickets
- [ ] Archive the release branch (if applicable)
- [ ] Update `ops/LESSONS_LEARNED.md` if anything unexpected happened
