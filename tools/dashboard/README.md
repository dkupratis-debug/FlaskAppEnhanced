# Local Engagement Dashboard

This folder contains a local-only dashboard that tracks GitHub engagement trends for this repository.

## Who Can Use It

- Anyone who can access this repo can run this tool locally.
- Users only see data their own token is allowed to access.
- This tool does not expose maintainer credentials.

## What It Tracks

- Views and unique visitors (14-day GitHub traffic window)
- Clones and unique cloners (14-day window)
- Open issues and open pull requests
- Discussion count and total discussion comments
- Workflow runs and workflow failures in the last 24 hours

## Security Model

- Runs on `127.0.0.1` only (not exposed publicly by default)
- Uses `GITHUB_TOKEN` from environment (never committed)
- Optional local password gate via `DASHBOARD_PASSWORD`
- Stores snapshots in local SQLite database (`tools/dashboard/data/engagement.db`)

## Required Token Permissions (Recommended)

Use a fine-grained PAT scoped to specific repositories with read-only access:

- `Metadata: Read`
- `Contents: Read`
- `Issues: Read`
- `Pull requests: Read`
- `Actions: Read`
- `Discussions: Read` (if using discussion metrics)

Avoid broad classic tokens unless required by your environment.

## Quick Start (PowerShell)

```powershell
cd C:\Users\kupra\FlaskAppEnhanced

$env:GITHUB_TOKEN = "your_github_token_here"
$env:DASHBOARD_PASSWORD = "choose-a-strong-password"
$env:DASHBOARD_SECRET_KEY = "long-random-secret"

python tools/dashboard/collector.py
python tools/dashboard/app.py
```

Open:

- `http://127.0.0.1:5050`

Expected behavior:
- First collector run prints a stored snapshot summary.
- Dashboard shows cards, deltas, and snapshot history table.
- If `DASHBOARD_PASSWORD` is set, login is required before viewing data.

## Do Not Do This

- Do not commit tokens to git.
- Do not share `.env` values in issues/discussions/screenshots.
- Do not change bind host to `0.0.0.0` unless you fully control network access.

## Daily Use

1. Click `Collect Snapshot`
2. Review metric cards and deltas
3. Compare historical rows in the table
4. Repeat daily/weekly for trend tracking

## Optional Hourly Task (Windows Task Scheduler)

Run this command hourly to collect snapshots automatically:

```powershell
python C:\Users\kupra\FlaskAppEnhanced\tools\dashboard\collector.py
```

## Files

- `tools/dashboard/collector.py` - Fetch + store metrics
- `tools/dashboard/app.py` - Local Flask dashboard
- `tools/dashboard/templates/` - HTML views
