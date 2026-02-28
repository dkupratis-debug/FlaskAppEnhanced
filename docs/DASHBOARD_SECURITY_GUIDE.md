# Dashboard Security Guide

Use this guide when running `tools/dashboard/` so users can monitor engagement safely.

## 1. Access Model (Plain English)

- The dashboard code is in the repo and can be viewed by repo users.
- Data visibility is controlled by each user's GitHub token.
- If a token cannot access a repo, the dashboard cannot fetch its stats.

## 2. Recommended Token Type

Use a fine-grained personal access token (PAT) with:

- repository access limited to selected repos only
- read-only permissions for required data APIs

Recommended permissions:

- `Metadata: Read`
- `Contents: Read`
- `Issues: Read`
- `Pull requests: Read`
- `Actions: Read`
- `Discussions: Read` (optional, needed for discussion metrics)

## 3. Secure Local Setup (PowerShell)

```powershell
cd C:\Users\kupra\FlaskAppEnhanced

$env:GITHUB_TOKEN = "your_fine_grained_token"
$env:DASHBOARD_PASSWORD = "strong_local_password"
$env:DASHBOARD_SECRET_KEY = "long_random_secret"

python tools/dashboard/collector.py
python tools/dashboard/app.py
```

Open:

- `http://127.0.0.1:5050`

## 4. Hard Rules

- Keep host binding on `127.0.0.1` (local only).
- Never commit `.env` or token values.
- Never post tokens in issues, PRs, discussions, or chat.
- Rotate token immediately if leaked.

## 5. What This Protects

- Prevents accidental public exposure of your analytics dashboard
- Limits blast radius if a token leaks
- Keeps repo users from seeing data outside their token scope

## 6. Operational Checklist

Before sharing this dashboard with others:

1. Confirm `.gitignore` excludes local DB files.
2. Confirm users know they must create their own token.
3. Confirm docs point to this file and `tools/dashboard/README.md`.
4. Confirm `DASHBOARD_PASSWORD` is required in your instructions.
