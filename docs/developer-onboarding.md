# Developer Onboarding & Contribution Guide

*Standard engineering workflows, development environments, and contribution practices.*

---

## 1. Local Development Standards

### 1.1 Node.js & TypeScript Toolchain
- **Node Version**: `>=20.0.0` (LTS recommended)
- **Package Managers**: Prefer `pnpm` for monorepos, `npm` for standard services.
- **Code Quality**: Run Prettier and ESLint with strict type checking enabled before staging changes:
  ```bash
  npm run lint
  npm test
  ```

### 1.2 Python & FastAPI Environments
- **Python Version**: `>=3.10`
- **Virtual Environments**: Always isolate project dependencies:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -e ".[dev]"
  ```
- **Typing & Formatting**: Enforce strict `mypy` and `ruff` / `black` standards:
  ```bash
  ruff check .
  pytest
  ```

---

## 2. Git & Open Source Contribution Workflow

### 2.1 Branching Strategy
1. Always base feature/fix branches off the latest upstream `main` branch.
2. Use descriptive branch prefixes:
   - `fix/<issue-description>` for bug repairs
   - `feat/<feature-description>` for new capabilities
   - `docs/<topic-description>` for technical documentation
3. Keep commits atomic, well-tested, and accompanied by detailed commit logs.

### 2.2 Conventional Commits & Changelogs
Follow the Conventional Commits specification:
```text
<type>(<scope>): <short summary>

[optional body explaining motivation and technical approach]

[optional footer referencing issues, e.g. Fixes #123]
```
Common types: `feat`, `fix`, `docs`, `test`, `refactor`, `ci`, `chore`.
