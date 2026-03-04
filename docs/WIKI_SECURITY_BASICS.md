# Security Basics

This page summarizes practical security rules for contributors and learners.

## Core Rules

- Never commit passwords, tokens, or API keys.
- Use pull requests instead of direct pushes to `main`.
- Keep dependencies updated.
- Review workflow/action versions for security updates.

## Repository Controls

- Branch protection enabled on `main`.
- Required CI checks before merge.
- Security policy documented in `SECURITY.md`.
- Dependabot alerts enabled.
- Secret scanning and push protection enabled.

## Safe Sharing Guidance

- Public repositories can be copied, so do not store sensitive data in code.
- Keep secrets in GitHub Actions secrets or local environment variables.
- Rotate tokens if exposure is suspected.

## If You Suspect a Vulnerability

1. Do not post sensitive details publicly.
2. Use the repository security reporting path in `SECURITY.md`.
3. Revoke/rotate any potentially exposed credentials immediately.
