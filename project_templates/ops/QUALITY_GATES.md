# Quality Gates

Version: 2.0
Last Updated: {{DATE}}

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
- [ ] Relevant governance docs updated (`docs/DECISIONS.md`, `docs/PRIVACY.md`, `docs/THREAT_MODEL.md`, `ops/RUNBOOK.md`)

## CI Policy

- CI is mandatory for protected branches.
- Failing checks must block merges.
- Keep CI checks deterministic and fast.
- See `.github/workflows/ci.yml` as the baseline workflow.

## Project Commands (Fill Per Stack)

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
Dev server:         uvicorn main:app --reload
```
