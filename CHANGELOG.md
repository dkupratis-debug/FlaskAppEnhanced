# Changelog

All notable changes to this project will be documented in this file.

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
