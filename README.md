# FlaskAppEnhanced

Small Flask app scaffold with basic security features, tests, and CI.

This repository is also set up as a GitHub learning example: you can use it to understand common repo files, workflows, and where to click in GitHub.

## Features
- Homepage at `/`
- Health check at `/health`
- CSRF-protected form at `/submit`
- JSON API example at `/api/echo`
- Rate limiting via `Flask-Limiter`
- Security headers and request IDs
- GitHub Actions CI (`.github/workflows/ci.yml`)

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

## Development Commands
```powershell
pip install -r requirements-dev.txt
ruff check .
pytest
```

Task runners:
- `Makefile` for Unix/macOS (`make test`, `make lint`, etc.)
- `tasks.ps1` for PowerShell (`.\tasks.ps1 test`, `.\tasks.ps1 lint`, etc.)

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
