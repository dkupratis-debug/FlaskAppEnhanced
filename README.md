# FlaskAppEnhanced

Small Flask app scaffold with basic security features, tests, and CI.

This repository is also set up as a GitHub learning example: you can use it to understand common repo files, workflows, and where to click in GitHub.

## Table of Contents
- [Features](#features)
- [Quick Start (Local)](#quick-start-local)
- [Run as an Installed Package](#run-as-an-installed-package)
- [Development Commands](#development-commands)
- [Project Structure](#project-structure)
- [Environment](#environment)
- [Production Run (Example)](#production-run-example)
- [Troubleshooting](#troubleshooting)
- [Learn GitHub Using This Repo](#learn-github-using-this-repo)
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

## Development Commands
```powershell
pip install -r requirements-dev.txt
ruff check .
pytest
```

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

## Learn GitHub Using This Repo
Start here:
- `README.md` (project overview)
- `CONTRIBUTING.md` (branching, commit, PR flow)
- `docs/GITHUB_GUIDE.md` (GitHub UI walkthrough)
- `.github/workflows/ci.yml` (automation)
- `.github/PULL_REQUEST_TEMPLATE.md` (PR structure)
- `.github/ISSUE_TEMPLATE/` (issue forms)
- `SECURITY.md` (security policy)

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
