# CODEOWNERS Review Exercise

This exercise teaches learners how code review and `CODEOWNERS` work in GitHub.

## Goal
Open a PR that changes a small file and walk through a realistic review process:
- PR description
- CI checks
- code review checklist
- merge decision

## Exercise Steps
1. Fork this repo (recommended) or create a branch
2. Create a branch, for example:
   - `exercise/readme-one-line-change`
3. Make one small change in `README.md`
4. Commit with a clear message
5. Open a PR
6. Use `docs/PR_REVIEW_CHECKLIST.md` to self-review
7. Watch CI in the `Actions` tab
8. Merge after checks pass

## What to Observe
- `CODEOWNERS` signals who is expected to review
- PR checks show whether code is safe to merge
- `Files changed` is where reviewers spend most of their time

## Variation (Reviewer Practice)
Have a friend:
- open a PR in their fork
- send you the PR link
- you leave line comments and a summary review

## Teaching Tip
Use a tiny docs-only PR first so learners focus on GitHub workflow, not code complexity.
