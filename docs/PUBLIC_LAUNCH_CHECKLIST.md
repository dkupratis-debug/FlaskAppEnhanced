# Public Launch Checklist

Use this checklist before sharing the repository publicly (for example on Facebook, LinkedIn, or with a class/workshop).

## 1. Security and Access
- Confirm no secrets are committed (`.env`, tokens, API keys)
- Review collaborators and remove unnecessary write/admin access
- Confirm branch protection is enabled on `main`
- Confirm CI checks are required before merge
- Confirm admin enforcement is enabled (if you want no direct pushes)
- Enable 2FA/passkeys on your GitHub account

## 2. GitHub Repo Presentation
- Add a clear `About` description
- Add a `Website` URL (repo URL or live demo URL)
- Add useful topics (flask, python, github-actions, security, etc.)
- Ensure `README.md` is polished and current
- Ensure `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, and `CODE_OF_CONDUCT.md` exist

## 3. Learning Experience
- Add a visible "Start Here" link (README or pinned issue)
- Verify workshop issues exist and are labeled clearly
- Verify `docs/GITHUB_GUIDE.md` and `docs/PR_REVIEW_CHECKLIST.md` are linked from README
- Add screenshots/GIFs in `docs/images/` for a more intuitive walkthrough

## 4. Actions, Releases, and Packages
- Confirm recent `CI` workflow runs are green
- Confirm `Release` workflow is working
- Confirm `Package (GHCR)` workflow is working
- Confirm latest release assets match the version tag

## 5. Demo Safety (If Sharing a Live App)
- Set a strong `SECRET_KEY`
- Keep rate limiting enabled
- Set `TRUST_PROXY_COUNT` correctly behind a reverse proxy
- Review logs for abuse or errors
- Use Redis for rate limiting in higher traffic scenarios

## 6. Social Sharing Post (Simple Template)
- What it is: "A small Flask app + GitHub learning repo"
- What people can learn: "PRs, Actions, Releases, Packages, branch protection"
- Where to start: `README.md` + `docs/GITHUB_GUIDE.md`
- What to do: "Fork it and make a tiny README PR"

## 7. After Going Public
- Watch GitHub traffic insights
- Watch Dependabot alerts
- Review new issues/PRs
- Tighten settings if needed (spam/abuse, access, Actions permissions)
