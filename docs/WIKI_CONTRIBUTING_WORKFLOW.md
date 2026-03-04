# Contributing Workflow

This page explains the recommended contribution path.

## Standard Flow

1. Create a branch from `main`.
2. Make focused changes.
3. Run checks locally if possible:
   - `ruff check .`
   - `pytest -q`
   - `python tools/docs_audit.py`
4. Commit with a clear message.
5. Push branch and open a pull request.
6. Address CI failures and review feedback.
7. Merge when all requirements are green.

## Pull Request Checklist

- Scope is clear and small.
- Documentation updated when behavior changes.
- Tests added/updated for code changes.
- No secrets or credentials in commits.

## Branch Protection Notes

- Direct pushes to `main` are blocked.
- Required status checks must pass.
- Review requirements are enforced.

## Help and Support

- Ask in Discussions for learning questions.
- Open an Issue for bugs or clear improvements.
