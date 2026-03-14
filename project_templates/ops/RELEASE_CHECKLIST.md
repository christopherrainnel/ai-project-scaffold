# Release Checklist

Version: 1.0
Last Updated: {{DATE}}

## Pre-Release

- [ ] All quality gates pass (lint, test, build)
- [ ] No secrets or credentials in the codebase (Unix: `git log --all -p --pretty=format: | grep -Ei "password|secret|api[_-]?key"` / PowerShell: `git log --all -p --pretty=format: | Select-String -Pattern "(?i)password|secret|api[_-]?key"`)
- [ ] Dependency changes reviewed and vulnerability-scanned
- [ ] `CHANGELOG_AI.md` is up to date
- [ ] `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` reflect current state
- [ ] Key user flows smoke-tested manually
- [ ] Environment variables documented in `.env.example`
- [ ] Rollback plan documented (for production releases)
- [ ] Database migrations tested (if applicable)
- [ ] Feature flags configured (if applicable)

## Product Readiness Polish Gate

- [ ] UI quality pass completed for key user-facing pages (no stale placeholders, broken copy, or obvious UX regressions)
- [ ] Legal pages are aligned with implemented behavior (privacy/terms/disclaimers reviewed)
- [ ] Any AI-assisted legal drafting has explicit human approval before release
- [ ] Release professionalism pass completed (naming, links, changelog clarity, and consistent product language)

## User Journey Completion Gate

- [ ] User/Consumer Journey Completion Gate completed (`Discover -> Acquire Access -> Verify -> Deliver -> Study/Use -> Support/Recovery`)
- [ ] Journey variant is explicitly mapped for release scope (`paid consumer`, `self-use`, or `team/internal`) and assumptions are documented when evidence is partial
- [ ] Any incomplete journey stage has a documented owner, mitigation plan, and target date

## Tier1 Model-Orchestration Readiness

- [ ] Model-selection strategy is documented for release-critical tasks (quality/cost/latency rationale)
- [ ] Chosen model strategy is validated on representative release scenarios
- [ ] Human approval checkpoints are preserved for legal wording and final release decisions

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
