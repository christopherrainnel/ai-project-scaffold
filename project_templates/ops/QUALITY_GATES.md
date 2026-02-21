# Quality Gates

Version: 1.0
Last Updated: {{DATE}}

## Definition of Done

A task is not complete until all applicable items pass:

- [ ] Code compiles / builds without errors
- [ ] Linting passes without errors
- [ ] Tests pass (unit, integration as applicable)
- [ ] `CHANGELOG_AI.md` updated with the change
- [ ] No secrets or hardcoded credentials introduced
- [ ] No dependency drift (lockfiles match manifests)
- [ ] `docs/DECISIONS.md` updated if an architectural choice was made

## Project Commands

> Fill these in when you choose your tech stack. AI agents will use these to verify their work.

| Action | Command |
|--------|---------|
| Install | |
| Lint | |
| Format | |
| Test | |
| Build | |
| Audit (deps) | |
| Dev server | |

### Common Stacks (Reference)

**Node.js / Next.js**
```
Install:  npm install
Lint:     npx eslint .
Format:   npx prettier --check .
Test:     npx jest  (or: npx vitest)
Build:    npm run build
Audit:    npm audit
Dev:      npm run dev
```

**Python / FastAPI / Django**
```
Install:  pip install -r requirements.txt
Lint:     ruff check .
Format:   ruff format --check .
Test:     pytest
Build:    (not applicable for most Python projects)
Audit:    pip-audit
Dev:      uvicorn main:app --reload  (or: python manage.py runserver)
```
