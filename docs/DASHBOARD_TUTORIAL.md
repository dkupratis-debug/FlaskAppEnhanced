# Local Engagement Dashboard Tutorial

This tutorial shows exactly how to run and use the local dashboard.

## 1. Create a GitHub Token

1. Open GitHub -> profile picture -> `Settings`.
2. Click `Developer settings`.
3. Click `Personal access tokens` -> `Tokens (classic)` -> `Generate new token`.
4. Set expiration and enable `repo` scope.
5. Copy token once and keep it private.

## 2. Open PowerShell in Repo

```powershell
cd C:\Users\kupra\FlaskAppEnhanced
```

## 3. Set Environment Variables

```powershell
$env:GITHUB_TOKEN = "paste_token_here"
$env:DASHBOARD_PASSWORD = "your-local-password"
$env:DASHBOARD_SECRET_KEY = "long-random-secret-value"
```

## 4. Collect First Snapshot

```powershell
python tools/dashboard/collector.py
```

Expected output includes:

- `Stored snapshot:`
- views/clones totals
- open issues/prs
- local DB path

## 5. Start Dashboard

```powershell
python tools/dashboard/app.py
```

Then open:

- `http://127.0.0.1:5050`

## 6. What to Click

1. Login with `DASHBOARD_PASSWORD`.
2. Click `Collect Snapshot`.
3. Check top cards:
   - views/visitors
   - clones/cloners
   - open issues and PRs
   - workflow failures
4. Check `Delta` values to see movement from prior snapshot.
5. Review the table for timeline history.

## 7. Recommended Routine

- Daily: click `Collect Snapshot` once.
- Weekly: compare current row vs 7 days ago.
- Monthly: summarize growth and workflow failure rate.

## 8. Security Checklist

- Keep dashboard local: `127.0.0.1` only.
- Never commit your token.
- Rotate token if accidentally exposed.
- Use a unique dashboard password.
- Log out when done.

## 9. Troubleshooting

- `401/403` errors: token missing/expired/scope issue.
- No traffic data: GitHub traffic may lag; check again later.
- Login loop: ensure `DASHBOARD_PASSWORD` is set before starting app.
