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

## Safety Notes

- These workflows are for training operations, not production deployment.
- Never include secrets in generated content.
- Keep branch protection active on `main`.
