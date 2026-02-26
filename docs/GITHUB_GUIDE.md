# GitHub Guide (Using This Repo)

This guide explains where to go in GitHub and what each part means, using `FlaskAppEnhanced` as the example.

## Visual Walkthrough (Optional but Recommended)
To make this guide more intuitive for learners, add screenshots/GIFs in `docs/images/` and link them from this file.

See:
- `docs/images/README.md` (suggested filenames + capture checklist)
- `docs/exercises/CODEOWNERS_REVIEW_EXERCISE.md` (practice PR exercise)

## 1. Code Tab (Main Repository Page)
This is the default page you see.

What to look at:
- File list: browse the code and docs.
- Latest commit line: who changed code most recently and when.
- Branch selector: switch branches.
- `Go to file` (`t` shortcut): quickly find files by name.

Start with these files:
- `README.md` for project overview
- `CONTRIBUTING.md` for workflow
- `.github/workflows/ci.yml` for automation
- `SECURITY.md` for security policy
- `docs/ARCHITECTURE.md` for app request flow
- `docs/VERSIONING_AND_RELEASES.md` for release process

## 1.1 Right Sidebar (Repository Info)
GitHub shows a sidebar with quick links and repo stats. These often include:

- **README**
  - A quick link to the repository's `README.md`.
  - Start here to understand what the project does and how to run it.

- **Security policy**
  - A link to `SECURITY.md` (if present).
  - Explains how vulnerabilities should be reported and any security expectations.

- **Activity**
  - A quick summary page of recent commits and repository changes.
  - Useful for seeing whether a project is actively maintained.

- **Stars**
  - A lightweight "bookmark/like" signal from users.
  - Example: `0 stars` means nobody has starred it yet.

- **Watchers**
  - People who subscribe to notifications for repository activity.
  - Example: `0 watching` means no one is subscribed right now.

- **Forks**
  - Copies of the repository made into other GitHub accounts/orgs.
  - Forks are commonly used to contribute changes via Pull Requests.

Note: star/watch/fork counts are live GitHub stats and change over time.

## 2. Commits and History
Open the commit history to understand change progression.

What to learn:
- Commit messages should explain intent.
- Small commits are easier to review.
- Commit hashes (like `515af33`) uniquely identify snapshots.

## 3. Branches
Branches let you work safely without changing `main`.

Typical flow:
- `main` = stable/default branch
- feature/fix branch = work in progress
- PR merges the branch back into `main`

## 4. Pull Requests (PRs)
PRs are where review happens.

Important PR tabs:
- **Conversation**: summary, comments, CI checks
- **Commits**: commit-by-commit view
- **Files changed**: final diff review

What to include in a good PR:
- What changed
- Why it changed
- How it was tested
- Risks / follow-ups

Practice this with:
- `docs/exercises/CODEOWNERS_REVIEW_EXERCISE.md`
- `docs/PR_REVIEW_CHECKLIST.md`

## 5. Issues
Use issues to track bugs, tasks, and ideas.

Good issues include:
- Reproduction steps
- Expected vs actual behavior
- Logs/screenshots when relevant
- Environment details (OS, Python version)

This repo includes issue templates in `.github/ISSUE_TEMPLATE/`.

## 6. Actions (CI/CD)
The **Actions** tab shows automated workflows.

In this repo:
- `.github/workflows/ci.yml` runs lint and tests on pushes/PRs.

Why this matters:
- Prevents broken code from being merged
- Gives reviewers confidence
- Documents your team's quality checks

## 7. Security Tab
Use the **Security** area and `SECURITY.md` to manage vulnerability reporting and dependency alerts.

What to know:
- `SECURITY.md` tells people how to report vulnerabilities
- Dependabot alerts (if enabled) flag vulnerable dependencies

## 8. Insights Tab
Useful for learning how a repo evolves.

Examples:
- Contributors
- Commit activity
- Traffic (views/clones, if enabled)

## 9. Settings (Maintainers)
Important settings for real projects:
- Branch protection rules
- Required status checks (CI must pass)
- PR review requirements
- Secret management for Actions
- Repo metadata (About description, website, topics)
- Security settings (Dependabot alerts, automated security fixes)

## 10. How to Understand a Repo Quickly
Use this checklist:
1. Read `README.md`
2. Read `CONTRIBUTING.md`
3. Inspect `.github/workflows/ci.yml`
4. Scan `requirements*.txt` / `pyproject.toml`
5. Run tests locally
6. Open recent commits
7. Read open PRs/issues
8. Review `docs/SAFE_SHARING.md` before sharing publicly

## 11. GitHub Terms (Quick Definitions)
- **Repo**: Project storage (code, docs, issues, PRs)
- **Branch**: Independent line of work
- **Commit**: Saved snapshot with a message
- **PR**: Request to merge a branch
- **Review**: Feedback/approval on a PR
- **CI**: Automated checks (tests, lint, build)
- **Merge**: Combine branch changes into target branch
