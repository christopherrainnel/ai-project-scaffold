# Quality Gates

Version: 2.2
Last Updated: 2026-03-07

## Shipping Gate (Required)

Code is not shippable unless all applicable checks pass locally and in CI:

- [ ] Lint
- [ ] Format check
- [ ] Type check
- [ ] Unit tests
- [ ] Dependency vulnerability scan
- [ ] Secret scan
- [ ] Basic SAST scan
- [ ] Build (if applicable)
- [ ] `CHANGELOG_AI.md` updated
- [ ] Relevant governance docs updated (`docs/DECISIONS.md`, `docs/PRIVACY.md`, `docs/TERMS.md`, `docs/THREAT_MODEL.md`, `ops/RUNBOOK.md`, `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md`)

Note: a feature, fix, or doc change is not "done" until `CHANGELOG_AI.md` has a matching entry describing what changed and how it was verified.

## Feature Acceptance Gate (Required Before Merge)

Use this checklist before merging feature work:

### Product Quality

- [ ] Acceptance criteria met.
- [ ] One vertical slice complete end-to-end.
- [ ] Non-goals not accidentally included.
- [ ] Technical Builder POV evidence recorded (implementation boundaries + quality/security verification).
- [ ] User/Consumer Journey stages reviewed (`Discover`, `Acquire Access`, `Verify`, `Deliver`, `Study + Use`, `Support + Recovery`); in-scope stages marked `Complete`.
- [ ] Any non-complete stage has owner-approved defer note in `CHANGELOG_AI.md`.

### Security and Privacy

- [ ] No secrets committed.
- [ ] Input validation and authorization checks in place.
- [ ] Rate limits and abuse controls on public endpoints.
- [ ] Logging avoids secrets and personal data.
- [ ] Data retention/deletion reflected in `docs/PRIVACY.md`.

### Documentation

- [ ] `docs/DECISIONS.md` updated for architectural choices.
- [ ] `docs/TERMS.md` updated if access, entitlement, or operating terms changed.
- [ ] `docs/THREAT_MODEL.md` updated for new attack surfaces.
- [ ] `ops/RUNBOOK.md` updated if operations changed.
- [ ] `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md` updated when user flow, entitlement, delivery, or recovery behavior changed.
- [ ] `CHANGELOG_AI.md` entry added.

### Compliance Wording

- [ ] Language uses "aligned with" or "informed by" - no unsupported compliance claims.

## CI Policy

- CI is mandatory for protected branches.
- Failing checks must block merges.
- Keep CI checks deterministic and fast.
- See `.github/workflows/ci.yml` as the baseline workflow.

## Project Commands (Fill Per Stack)

Prefer the repo-local `.venv_run` environment and `python -m ...` command forms described in `ops/AI_WORKFLOW.md` and `ops/RUNBOOK.md`.

| Action | Command |
|--------|---------|
| Install | |
| Lint | |
| Format check | |
| Type check | |
| Unit test | |
| Build | |
| Dependency scan | |
| Secret scan | |
| SAST scan | |
| Dev server | |

## Reference Commands

### Node.js / Next.js (example)

```
Install:            npm ci
Lint:               npx eslint .
Format check:       npx prettier --check .
Type check:         npx tsc --noEmit
Unit test:          npm test
Build:              npm run build
Dependency scan:    npm audit --audit-level=high
Secret scan:        gitleaks detect --source . --no-git --redact
SAST scan:          semgrep --config auto
Dev server:         npm run dev
```

### Python / FastAPI / Django (example)

```
Install:            pip install -r requirements.txt
Lint:               ruff check .
Format check:       ruff format --check .
Type check:         mypy .
Unit test:          pytest
Build:              (optional for many Python apps)
Dependency scan:    pip-audit
Secret scan:        gitleaks detect --source . --no-git --redact
SAST scan:          semgrep --config auto
Dev server:         python -m uvicorn main:app --host 127.0.0.1 --port 8000
```
