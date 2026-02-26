# Changelog

All notable changes to this project will be documented in this file.

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
