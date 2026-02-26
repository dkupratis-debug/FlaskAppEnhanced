# Contributing

This repo is intentionally small so new contributors can learn the full GitHub workflow end to end.

## Recommended Git Workflow
1. Fork the repo (or create a branch in the main repo if you have access).
2. Create a feature branch.
3. Make focused changes.
4. Run tests and lint locally.
5. Commit with a clear message.
6. Push your branch.
7. Open a Pull Request (PR).
8. Address review comments and CI failures.
9. Merge after approval.

## Branch Naming
Use descriptive branch names:
- `fix/rate-limit-config`
- `docs/github-guide`
- `test/homepage-headers`

## Commit Messages
Prefer short, specific messages in imperative tense:
- `Fix rate limit config parsing`
- `Add pytest import bootstrap`
- `Document GitHub workflow for beginners`

## Local Checks Before Pushing
```powershell
ruff check .
pytest
```

## Pull Requests
- Keep PRs focused on one goal.
- Explain what changed and why.
- Include test coverage notes.
- Mention risks or follow-up work.

See `.github/PULL_REQUEST_TEMPLATE.md` for the expected PR format.

## How to Read GitHub Changes
When reviewing a PR on GitHub:
1. Open the **Files changed** tab.
2. Read the PR description first (context).
3. Review tests and docs updates.
4. Look for configuration or security-impacting changes.
5. Check CI results in the PR checks section.

## Useful Git Commands
```powershell
git status
git diff
git add <files>
git commit -m "Your message"
git push origin <branch>
```
