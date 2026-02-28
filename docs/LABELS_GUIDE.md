# Labels Guide

Use labels to make triage faster and clearer for beginners.

## Core Labels

- `good first issue`: safe, beginner-friendly task
- `learning`: training-focused task or discussion
- `bug`: confirmed defect
- `enhancement`: improvement request
- `documentation`: docs-only change
- `security`: security-related work
- `ci`: workflow, checks, or automation changes
- `dashboard`: local engagement dashboard changes
- `frontend`: templates/static UI changes
- `backend`: Flask/config/runtime logic changes
- `dependencies`: package or version updates

## Auto Labeling

This repository auto-labels pull requests using:

- `.github/labeler.yml`
- `.github/workflows/auto_label.yml`

Manual review is still required, but labels reduce maintainer overhead.

## Triage Rules

1. Add at least one type label (`bug`, `enhancement`, `documentation`).
2. Add audience label when relevant (`good first issue`, `learning`).
3. Keep label set small and consistent.
4. Remove stale/misleading labels before merge.
