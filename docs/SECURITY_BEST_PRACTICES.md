# Security Best Practices Guide

Use this guide to keep `FlaskAppEnhanced` safe while it remains public and training-friendly.

## 1. Access and Identity

1. Keep collaborator access minimal.
1. Give trusted helpers `Write` only, not `Admin`.
1. Use 2FA on every account with repo access.
1. Review collaborators monthly and remove stale access.

## 2. Branch Protection Baseline (main)

Keep these controls enabled:

- Require pull requests for all changes.
- Require at least 1 approving review.
- Require approval after last push (`require_last_push_approval=true`).
- Require status checks:
  - `test`
  - `precommit`
  - `markdownlint`
  - `yamllint`
  - `links`
- Enforce for admins.
- Require linear history.
- Block force pushes and branch deletion.
- Require conversation resolution.

## 3. Release and Tag Safety

Release tags are trust anchors. Protect them:

- Keep tag ruleset active for `refs/tags/v*`.
- Block tag `update` and `deletion`.
- Publish releases only from reviewed PRs on `main`.

## 4. Secrets and Credentials

1. Never commit secrets (`.env`, API keys, tokens, passwords).
1. Keep `SECRET_KEY` strong in production.
1. Rotate compromised secrets immediately.
1. Use GitHub Actions secrets for CI/deploy values.
1. Keep secret scanning and push protection enabled.

## 5. Discussions and Community Safety

1. Keep `#29` pinned in Announcements as the entry point.
1. Use `Q&A` for beginner help and route support there.
1. Remove exposed secrets from posts immediately.
1. Close spam/abuse threads quickly and document moderation actions.

Only maintainers/collaborators with sufficient permissions should close or moderate discussions.

## 6. Dependency and Workflow Security

1. Keep Dependabot alerts enabled.
1. Merge security updates quickly after CI passes.
1. Pin GitHub Actions to trusted versions and keep them updated.
1. Use least-privilege workflow permissions in Actions.

## 7. Vulnerability Reporting Workflow

1. Reporter submits via private security reporting (`SECURITY.md` policy path).
1. Maintainer reproduces and triages severity.
1. Patch on a private branch if needed.
1. Merge fix through protected PR process.
1. Publish release notes with mitigation guidance.

Do not ask reporters to post vulnerabilities publicly in Issues or Discussions.

## 8. Regular Security Checklist (Weekly)

1. Check open Dependabot alerts.
1. Review open PRs for stale/unreviewed changes.
1. Verify branch protection is still intact.
1. Review latest workflow runs for suspicious failures.
1. Confirm pinned Start Here discussion is still pinned.
1. Verify no sensitive data appears in issues/discussions/PR logs.

## 9. What This Protects vs Does Not

This setup protects:

- Unauthorized direct changes to `main`
- Accidental merges of failing/broken changes
- Silent release-tag tampering
- Common secret leaks in commits

This setup does not prevent:

- Manual copying of public code
- Screenshots or reposts of public content
- Social engineering of trusted maintainers

Security depends on both technical controls and disciplined maintainer behavior.
