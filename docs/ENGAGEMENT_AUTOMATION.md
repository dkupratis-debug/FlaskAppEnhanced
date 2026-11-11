# Engagement Automation

This repo includes automation to keep community activity and hands-on practice moving.

## 1) Playground Branch Generator

Workflow file:
- `.github/workflows/playground_branch_generator.yml`

What it does:
1. Manually generates a branch with one intentional failure scenario.
1. Scenarios:
   - `markdownlint`
   - `test`
   - `yamllint`
   - `links`
1. Pushes branch to origin.
1. Optionally opens a PR automatically.

Use case:
- Safe learner drills for "find failure -> fix -> green CI".

## 2) Auto Label Workflow

Workflow files:
- `.github/workflows/auto_label.yml`
- `.github/labeler.yml`

What it does:
1. Applies labels to PRs based on changed file patterns.
1. Helps beginners and reviewers quickly understand PR scope.
1. Supports faster triage without replacing manual review.

## 3) Docs Quality Workflow

Workflow file:
- `.github/workflows/docs_quality.yml`

What it does:
1. Runs a docs audit script on pushes/PRs to `main`.
1. Verifies required docs exist and are linked in `docs/INDEX.md`.
1. Verifies markdown fences are balanced (prevents common render/parse issues).

Script:
- `tools/docs_audit.py`

## Safety Notes

- These workflows are for training operations, not production deployment.
- Never include secrets in generated content.
- Keep branch protection active on `main`.
