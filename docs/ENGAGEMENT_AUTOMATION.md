# Engagement Automation

This repo includes automation to keep community activity and hands-on practice moving.

## 1) Weekly Leaderboard Workflow

Workflow file:
- `.github/workflows/weekly_leaderboard.yml`

What it does:
1. Runs weekly (and manually via `workflow_dispatch`).
1. Collects last-7-day activity for:
   - pull requests opened
   - pull requests merged
   - issues opened
   - discussions created
1. Calculates a simple score and creates a weekly leaderboard issue.

Scoring:
- PR opened = 3
- PR merged = 5
- Issue opened = 1
- Discussion started = 2

## 2) Playground Branch Generator

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

## 3) Monthly Recap Issue Workflow

Workflow file:
- `.github/workflows/monthly_recap_issue.yml`

What it does:
1. Runs monthly (and manually with `workflow_dispatch`).
1. Opens a recap issue with:
   - open issues count
   - open PR count
   - recent workflow failure signal
   - first-time contributor PR count (30-day window)
   - unique non-bot PR contributors (30-day window)
1. Adds a checklist for owner review and operations hygiene.

Use case:
- Repeatable monthly cadence and transparent progress logging.

## 4) Auto Label Workflow

Workflow files:
- `.github/workflows/auto_label.yml`
- `.github/labeler.yml`

What it does:
1. Applies labels to PRs based on changed file patterns.
1. Helps beginners and reviewers quickly understand PR scope.
1. Supports faster triage without replacing manual review.

## 5) Weekly Check-In Issue Workflow

Workflow file:
- `.github/workflows/weekly_checkin_issue.yml`

What it does:
1. Runs weekly (and manually with `workflow_dispatch`).
1. Opens a learner check-in issue with standard progress prompts.
1. Improves visibility into blockers and response SLAs.

Template used:
- `docs/templates/WEEKLY_CHECKIN_TEMPLATE.md`

## 6) Docs Quality Workflow

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
