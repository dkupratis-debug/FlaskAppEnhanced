# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

- No changes yet.

## [0.3.0] - 2026-02-28

### Added
- Local dashboard security guide (`docs/DASHBOARD_SECURITY_GUIDE.md`)
- Labels guide (`docs/LABELS_GUIDE.md`)
- Good first issues backlog (`docs/GOOD_FIRST_ISSUES.md`)
- Starter-task issue template (`.github/ISSUE_TEMPLATE/starter_task.yml`)
- Auto-label workflow and config (`.github/workflows/auto_label.yml`, `.github/labeler.yml`)
- Monthly recap issue workflow (`.github/workflows/monthly_recap_issue.yml`)

### Changed
- Expanded `README.md` with security posture and onboarding links
- Expanded `SUPPORT.md` with best-effort response targets
- Expanded `docs/ENGAGEMENT_AUTOMATION.md` with monthly recap and auto-label details

## [0.2.4] - 2026-02-27

### Added
- New `Interactive Learning Dashboard` section in `README.md` for the `/learn` route
- Screenshot capture guide for the dashboard in `docs/images/LEARN_DASHBOARD_CAPTURE.md`

### Changed
- Updated `docs/FIRST_10_MINUTES.md` to include a direct `/learn` walkthrough step
- Expanded `docs/images/README.md` with `learn-dashboard.png` guidance
- Strengthened `/learn` test assertions in `tests/test_app.py` to verify key UI script markers

## [0.2.3] - 2026-02-26

### Fixed
- Added a release workflow guard to fail if Git tag and `pyproject.toml` version do not match

### Added
- `docs/PR_REVIEW_CHECKLIST.md` for teaching GitHub/code review workflow
- `CODE_OF_CONDUCT.md`
- `SUPPORT.md`

### Changed
- Improved `README.md` with learning path, sharing guidance, and reviewer references

## [0.2.2] - 2026-02-26

### Changed
- Polished `README.md` with badges, GHCR examples, and maintainer workflow guidance
- Documentation-only release tag (note: package assets remained `0.2.1`)

## [0.2.1] - 2026-02-26

### Changed
- Bumped `Flask` from `3.0.2` to `3.1.3` via Dependabot PR #1
- Expanded `README.md` with Docker run instructions and GitHub setup status notes
- Added GHCR package workflow and Docker image support

### Security
- Enabled Dependabot vulnerability alerts and automated security fixes on GitHub
- Added branch protection for `main` (required CI check + PR review)

## [0.2.0] - 2026-02-26

### Added
- GitHub learning documentation (`CONTRIBUTING.md`, `docs/GITHUB_GUIDE.md`)
- GitHub templates (`CODEOWNERS`, issue template, PR template)
- Packaging metadata and package build support via `pyproject.toml`
- `MANIFEST.in` and package data inclusion for templates/static files
- `app.__main__` entrypoint (`python -m app`)

### Changed
- Improved `README.md` with GitHub page anatomy guidance
- Hardened CI workflow permissions (`contents: read`)
- Expanded config defaults for safer production behavior
- Improved tests and pytest import reliability

### Fixed
- Request-ID logging filter crash outside request context during app startup
- Rate limit default parsing for `Flask-Limiter`
