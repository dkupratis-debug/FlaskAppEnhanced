# FlaskAppEnhanced

[![CI](https://github.com/dkupratis-debug/FlaskAppEnhanced/actions/workflows/ci.yml/badge.svg)](https://github.com/dkupratis-debug/FlaskAppEnhanced/actions/workflows/ci.yml)
[![Release](https://github.com/dkupratis-debug/FlaskAppEnhanced/actions/workflows/release.yml/badge.svg)](https://github.com/dkupratis-debug/FlaskAppEnhanced/actions/workflows/release.yml)
[![Package (GHCR)](https://github.com/dkupratis-debug/FlaskAppEnhanced/actions/workflows/package.yml/badge.svg)](https://github.com/dkupratis-debug/FlaskAppEnhanced/actions/workflows/package.yml)

Small Flask app scaffold with basic security features, tests, and CI.

This repository is also set up as a GitHub learning example: you can use it to understand common repo files, workflows, and where to click in GitHub.

Quick links:
- App docs and setup: `README.md`
- Start here (single doc entry): `docs/START_HERE.md`
- Public launchpad page: `/launch`
- Docs index: `docs/INDEX.md`
- Role-based onboarding: `docs/START_HERE_BY_ROLE.md`
- GitHub walkthrough: `docs/GITHUB_GUIDE.md`
- CI troubleshooting: `docs/CI_TROUBLESHOOTING_FLOW.md`
- Broken-to-fixed scenarios: `docs/BROKEN_TO_FIXED_SCENARIOS.md`
- Quality scorecard: `docs/QUALITY_SCORECARD.md`
- Engagement playbook: `docs/ENGAGEMENT_PLAYBOOK.md`
- Discussions guide: `docs/DISCUSSIONS_GUIDE.md`
- Local engagement dashboard tutorial: `docs/DASHBOARD_TUTORIAL.md`
- Good first issues backlog: `docs/GOOD_FIRST_ISSUES.md`
- Labels and triage guide: `docs/LABELS_GUIDE.md`
- Weekly check-in template: `docs/templates/WEEKLY_CHECKIN_TEMPLATE.md`
- Start Here discussion: `https://github.com/dkupratis-debug/FlaskAppEnhanced/discussions/29`
- Contributing workflow: `CONTRIBUTING.md`
- Security reporting: `SECURITY.md`
- Security best practices: `docs/SECURITY_BEST_PRACTICES.md`
- Engagement automation: `docs/ENGAGEMENT_AUTOMATION.md`
- Dashboard security guide: `docs/DASHBOARD_SECURITY_GUIDE.md`

## Table of Contents
- [Features](#features)
- [Quick Start (Local)](#quick-start-local)
- [Run as an Installed Package](#run-as-an-installed-package)
- [Run with Docker](#run-with-docker)
- [Development Commands](#development-commands)
- [Project Structure](#project-structure)
- [Environment](#environment)
- [Production Run (Example)](#production-run-example)
- [Deploy a Live Demo](#deploy-a-live-demo)
- [Troubleshooting](#troubleshooting)
- [Documentation Navigation](#documentation-navigation)
- [Learning Path](#learning-path)
- [Learning Tracks](#learning-tracks)
- [Start Here by Role](#start-here-by-role)
- [Interactive Learning Dashboard](#interactive-learning-dashboard)
- [Interactive Learning Lab](#interactive-learning-lab)
- [Public Launchpad](#public-launchpad)
- [CI Troubleshooting Flow](#ci-troubleshooting-flow)
- [Broken to Fixed Scenarios](#broken-to-fixed-scenarios)
- [First 10 Minutes (Beginner Click Guide)](#first-10-minutes-beginner-click-guide)
- [Practice Examples](#practice-examples)
- [FAQ](#faq)
- [Quality Scorecard](#quality-scorecard)
- [Training Operations](#training-operations)
- [Security Posture](#security-posture)
- [Sharing for Learning](#sharing-for-learning)
- [Public Launch Checklist](#public-launch-checklist)
- [Analytics and Privacy](#analytics-and-privacy)
- [Local Engagement Dashboard (Maintainer)](#local-engagement-dashboard-maintainer)
- [Learn GitHub Using This Repo](#learn-github-using-this-repo)
- [Documentation Standards](#documentation-standards)
- [Docs QA Automation](#docs-qa-automation)
- [GitHub Page Anatomy (Quick Reference)](#github-page-anatomy-quick-reference)
- [Security Notes](#security-notes)

## Features
- Homepage at `/`
- Health check at `/health`
- CSRF-protected form at `/submit`
- JSON API example at `/api/echo`
- Rate limiting via `Flask-Limiter`
- Security headers and request IDs
- GitHub Actions CI (`.github/workflows/ci.yml`)
- GitHub Release automation (`.github/workflows/release.yml`)
- GitHub Container Registry package workflow (`.github/workflows/package.yml`)

## Quick Start (Local)
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit:
- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/health`

Quick test after startup:
```powershell
curl http://127.0.0.1:5000/health
```

## Run as an Installed Package
You can also install and run this as a Python package:

```powershell
pip install .
flaskappenhanced
```

Alternative:
```powershell
python -m app
```

## Run with Docker
Build and run locally with Docker:

```powershell
docker build -t flaskappenhanced:local .
docker run --rm -p 8000:8000 -e SECRET_KEY=change-me flaskappenhanced:local
```

Then visit:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/health`

This repo also publishes a container image to GitHub Container Registry (GHCR) via `.github/workflows/package.yml`.

Example GHCR image (replace tag as needed):
```powershell
docker pull ghcr.io/dkupratis-debug/flaskappenhanced:latest
docker run --rm -p 8000:8000 -e SECRET_KEY=change-me ghcr.io/dkupratis-debug/flaskappenhanced:latest
```

## Development Commands
```powershell
pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
ruff check .
pytest
```

One-line local package build check:
```powershell
python -m build
```

One-command local build helper:
```powershell
.\tools\build_local.ps1
```

If Windows reports `Access is denied` under `%LOCALAPPDATA%\\Temp`, run:
```powershell
New-Item -ItemType Directory -Force .tmp\build-temp | Out-Null
$env:TEMP = (Resolve-Path .tmp\build-temp).Path
$env:TMP = $env:TEMP
python -m build --no-isolation
```

Additional checks:
- Markdown lint config: `.markdownlint.yml`
- YAML lint config: `.yamllint.yml`
- Link-check ignore list: `.lycheeignore`

Task runners:
- `Makefile` for Unix/macOS (`make test`, `make lint`, etc.)
- `tasks.ps1` for PowerShell (`.\tasks.ps1 test`, `.\tasks.ps1 lint`, etc.)

## Project Structure
- `app/` - Flask app package, routes, templates, static files
- `tests/` - Pytest test suite
- `.github/workflows/` - CI and release automation
- `docs/` - GitHub UI and contributor learning docs
- `config.py` - Environment-based config classes
- `requirements*.txt` - Runtime and development dependencies
- `pyproject.toml` - Project metadata, tooling, packaging configuration

## Environment
Copy `.env.example` to `.env` and update values as needed. `python-dotenv` loads `.env` automatically if installed.

Useful variables:
- `FLASK_ENV=development|production`
- `SECRET_KEY=...`
- `RATELIMIT_DEFAULT=200 per day;50 per hour`
- `RATELIMIT_STORAGE_URI=memory://` (use Redis in production)
- `LOG_FILE=logs/app.log`

## Production Run (Example)
```powershell
pip install -r requirements.txt
$env:FLASK_ENV="production"
$env:SECRET_KEY="change-me"
gunicorn -c gunicorn.conf.py wsgi:app
```

## Deploy a Live Demo
This repository includes a starter Render blueprint in `render.yaml` so you can create a real demo URL and add it to GitHub `About -> Website`.

Start here:
- `docs/DEPLOY_DEMO.md` (deployment steps and safety notes)
- `render.yaml` (starter configuration)

## Troubleshooting
### GitHub shows an older commit
GitHub only shows new code after `git add` + `git commit` + `git push`.

### GitHub shows a different account on the commit
Commit attribution comes from your local git `user.name` / `user.email`, not just the repo owner.

### `pytest` warnings about cache permissions
This repo disables pytest's cache provider in `pyproject.toml` to avoid noisy permission warnings in restricted environments.

### Rate limiting in production
`memory://` works for local demos, but use Redis in production (`RATELIMIT_STORAGE_URI`) for accurate limits across processes.

### Releases vs Packages on GitHub
- `Releases` in this repo contains versioned source/wheel artifacts (for example `v0.2.0`)
- `Packages` is for registry-published packages (this repo publishes a container image to GHCR via Actions)

## Documentation Navigation
Use this order if you want the clearest learning sequence:

1. `docs/START_HERE.md`
2. `docs/FIRST_10_MINUTES.md`
3. `docs/GITHUB_GUIDE.md`
4. `docs/PRACTICE_EXAMPLES.md`
5. `docs/CI_TROUBLESHOOTING_FLOW.md`
6. `docs/TRAINING_OPERATIONS.md` (maintainers)

## Learning Path
Use this repo as a hands-on GitHub + Flask lab.

### Beginner path (60-90 minutes)
1. Read `README.md` and `docs/GITHUB_GUIDE.md`
2. Run the app locally and open `/health`
3. Run `pytest` and `ruff check .`
4. Create a branch and make a tiny README change
5. Push branch and open a PR
6. Watch the CI run in GitHub Actions
7. Merge the PR (if allowed in your fork)
8. Inspect the commit history, release page, and package workflow
9. (Optional) Deploy a demo app and add the URL to the repo `About` section

### Reviewer path
1. Open a PR
2. Use `docs/PR_REVIEW_CHECKLIST.md`
3. Review code, tests, config, docs, and security impact
4. Check CI and release/package workflows

## Learning Tracks
For structured training paths, use:
- `docs/LEARNING_TRACKS.md`

Tracks included:
- Beginner
- Intermediate
- Maintainer

## Start Here by Role
Use role-based onboarding paths with exact first steps:
- `docs/START_HERE_BY_ROLE.md`

## Interactive Learning Dashboard
For an interactive in-app guide, open:
- `/learn`

This page provides:
- track selection (Beginner, Intermediate, Maintainer)
- next action and expected result
- progress checklist saved in browser (`localStorage`)
- quick links to Start Here, weekly challenge, Actions, Releases, and help flow

## Interactive Learning Lab
For guided simulation demos, open:
- `/learn-lab`

This page includes:
- first PR simulation
- failing CI fix simulation
- release/tag flow simulation
- command and expected-output walk-throughs

## Public Launchpad
For a share-friendly entry page with guided calls to action, open:
- `/launch`

This page includes:
- learner onboarding cards
- community and discussion entry points
- contribution links
- quality/security links

## CI Troubleshooting Flow
When any required GitHub check fails, use:
- `docs/CI_TROUBLESHOOTING_FLOW.md`

## Broken to Fixed Scenarios
For structured "failure -> diagnosis -> fix" drills, use:
- `docs/BROKEN_TO_FIXED_SCENARIOS.md`

## First 10 Minutes (Beginner Click Guide)
If you are brand new to GitHub, start with:
- `docs/FIRST_10_MINUTES.md`

This is a click-by-click walkthrough that shows exactly where to go first:
- repo homepage / README
- pinned `Start Here` issue
- workshop issues
- Actions
- Releases
- Packages

## Practice Examples
For guided exercises (beginner to intermediate), use:
- `docs/PRACTICE_EXAMPLES.md`

This file gives exact tasks, success checks, and a recommended order.

## FAQ
For common learner questions, use:
- `docs/FAQ.md`

## Quality Scorecard
For a plain-English quality and security posture snapshot, use:
- `docs/QUALITY_SCORECARD.md`

## Training Operations
For maintainers running this repo as a training program, use:
- `docs/TRAINING_OPERATIONS.md`
- `docs/LEARNER_PROGRESS_TEMPLATE.md`

## Security Posture
Current hardening posture includes:

- Protected `main` branch with required checks
- Required review/approval flow before merge
- Dependabot alerts and security updates
- Secret scanning + push protection
- Code scanning via CodeQL
- Private vulnerability reporting enabled
- Local dashboard guidance in `docs/DASHBOARD_SECURITY_GUIDE.md`

## Sharing for Learning
To share this repo with learners effectively:

1. Send the repo link plus a short goal:
   - "Learn GitHub PRs, Actions, Releases, and Packages using a small Flask app."
2. Tell learners where to start:
   - `README.md`
   - `docs/GITHUB_GUIDE.md`
   - `CONTRIBUTING.md`
3. Give them a first task:
   - "Change a README line and open a PR"
4. Ask them to inspect:
   - `Actions` tab
   - `Releases` tab
   - `Packages` section
5. Use forks for practice so they can safely merge in their own copy

Read `docs/SAFE_SHARING.md` before posting publicly (especially on social media).
For a ready-to-use post template, use:
- `docs/FACEBOOK_SHARE_GUIDE.md`

## Public Launch Checklist
Before making this repo public or sharing it widely, use:
- `docs/PUBLIC_LAUNCH_CHECKLIST.md`
- `docs/SAFE_SHARING.md`

These docs explain how to share safely while keeping your repo protected.

## Analytics and Privacy
If you want to understand how people use the repo or demo app, start with:
- `docs/ANALYTICS_AND_PRIVACY.md`

Short version:
- Use GitHub `Insights -> Traffic` for repo-level traffic (views/clones/referrers)
- Use app logs for demo usage patterns
- Prefer aggregate, privacy-first analytics over invasive user tracking

## Local Engagement Dashboard (Maintainer)
If you want a local-only metrics dashboard for this repository:

- Tutorial: `docs/DASHBOARD_TUTORIAL.md`
- Security: `docs/DASHBOARD_SECURITY_GUIDE.md`
- Tooling: `tools/dashboard/README.md`
- Collector command: `python tools/dashboard/collector.py`
- Local web UI: `python tools/dashboard/app.py` then open `http://127.0.0.1:5050`

Important access model:
- The dashboard code is public in this repo.
- Metrics access depends on the token each user provides locally.
- Do not share your token, `.env`, or local dashboard database.

Minimum safe setup:
1. Use a fine-grained GitHub token restricted to selected repos only.
2. Grant read-only permissions needed for metrics.
3. Set `DASHBOARD_PASSWORD` and `DASHBOARD_SECRET_KEY`.
4. Keep dashboard bound to `127.0.0.1` only.

## Learn GitHub Using This Repo
Start here:
- `README.md` (project overview)
- `docs/FIRST_10_MINUTES.md` (fast beginner click guide)
- `docs/PRACTICE_EXAMPLES.md` (guided exercises with success checks)
- `docs/LEARNING_TRACKS.md` (structured training paths)
- `docs/FAQ.md` (common questions and fixes)
- `docs/TRAINING_OPERATIONS.md` (weekly/monthly training routine)
- `docs/LEARNER_PROGRESS_TEMPLATE.md` (progress tracking template)
- `docs/COACHING_REPLY_TEMPLATES.md` (support reply templates)
- `docs/templates/WEEKLY_DISCUSSION_PROMPT.md` (weekly engagement post template)
- `docs/templates/MONTHLY_RECAP_TEMPLATE.md` (monthly recap template)
- `docs/templates/LEARNER_HELP_RESPONSE_TEMPLATE.md` (Q&A response template)
- `CONTRIBUTING.md` (branching, commit, PR flow)
- `docs/GITHUB_GUIDE.md` (GitHub UI walkthrough)
- `docs/PR_REVIEW_CHECKLIST.md` (how to review PRs)
- `docs/ARCHITECTURE.md` (request flow and components)
- `docs/VERSIONING_AND_RELEASES.md` (version/tag/release flow)
- `docs/SAFE_SHARING.md` (how to share safely)
- `docs/FACEBOOK_SHARE_GUIDE.md` (social post template + follow-up text)
- `docs/PUBLIC_LAUNCH_CHECKLIST.md` (how to prepare for public sharing)
- `docs/ANALYTICS_AND_PRIVACY.md` (tracking usage ethically)
- `docs/DEPLOY_DEMO.md` (how to get a live demo URL)
- `docs/exercises/CODEOWNERS_REVIEW_EXERCISE.md` (guided practice PR)
- `.github/workflows/ci.yml` (automation)
- `.github/PULL_REQUEST_TEMPLATE.md` (PR structure)
- `.github/ISSUE_TEMPLATE/` (issue forms)
- `SECURITY.md` (security policy)

## Documentation Standards
For contributors updating docs:

- `docs/DOCUMENTATION_STANDARDS.md`

## Docs QA Automation
Automated docs checks are configured to prevent navigation/render regressions:

- Workflow: `.github/workflows/docs_quality.yml`
- Script: `tools/docs_audit.py`

Current checks:
1. Required docs exist
2. Required docs are linked in `docs/INDEX.md`
3. Markdown fences are balanced

## GitHub Setup Status (Example Repo)
This repository is configured as a practical GitHub example and includes:

- `About` section with description, homepage, and topics
- Branch protection on `main` (PR review + required CI + admin enforcement)
- CI, Release, and GHCR package workflows
- Dependabot alerts and automated security fixes
- Issue/PR templates, `CODEOWNERS`, `CONTRIBUTING.md`, and `SECURITY.md`
- `CODE_OF_CONDUCT.md` and `SUPPORT.md`

## Visual Walkthrough Assets
Screenshot/GIF placeholders and capture plan live in:
- `docs/images/README.md`
- `docs/images/CAPTURE_CHECKLIST.md`
- `docs/images/LEARN_DASHBOARD_CAPTURE.md`
- `docs/images/REPO_FLOW_MAP.md`

Add screenshots there to make the GitHub guide more visual for friends and learners.

### Maintainer Workflow (Current)
Because `main` is protected (including admins), changes should go through:
1. Create a branch
2. Push branch
3. Open PR
4. Wait for CI
5. Merge PR

## GitHub Page Anatomy (Quick Reference)
When you open this repository on GitHub, you will usually see:

- `README`
  - Project overview and setup instructions (`README.md`)
- `Security policy`
  - Vulnerability reporting guidance (`SECURITY.md`)
- `Activity`
  - Recent repository changes and maintenance signals
- `Stars`
  - How many users bookmarked/liked the repo
- `Watchers`
  - How many users are subscribed to repo notifications
- `Forks`
  - How many copies of the repo exist in other accounts (often used for contributions)

These counts (`Stars`, `Watchers`, `Forks`) are GitHub UI stats and update automatically over time.

## Security Notes
- CSRF enabled for HTML form submissions (`Flask-WTF`)
- `/api/echo` is CSRF-exempt intentionally as a demo JSON endpoint
- Request IDs are added to logs and responses via `X-Request-Id`
- Rate-limit storage should be Redis in production for accuracy
- Ongoing maintainer hardening guide: `docs/SECURITY_BEST_PRACTICES.md`
