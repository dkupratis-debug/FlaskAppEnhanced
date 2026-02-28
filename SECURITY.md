# Security Policy

## Supported Versions
This is a demo project used for training and safe workflow examples.

## Reporting a Vulnerability

Please do not post vulnerabilities publicly in Issues or Discussions.

Report security issues through the repository security reporting flow:
- GitHub `Security` tab -> `Report a vulnerability`
- or the security policy URL: `https://github.com/dkupratis-debug/FlaskAppEnhanced/security/policy`

Include:
- affected file/area
- reproduction steps
- impact summary
- suggested fix (if available)

## Deployment Checklist
- Set a strong `SECRET_KEY` via environment variables.
- Run behind HTTPS so `SESSION_COOKIE_SECURE=True` works as intended.
- Set `RATELIMIT_STORAGE_URI` to Redis in production.
- Review CSRF exemptions; remove them for state-changing endpoints.
- Keep dependencies updated and review security advisories.
- Restrict CORS if you add API usage from browsers.
- Set `LOG_FILE` to rotate logs in production.

## Local Dashboard Safety
The engagement dashboard in `tools/dashboard/` is local-only tooling.

- It binds to `127.0.0.1` by default.
- It requires each user to provide their own token locally.
- Maintainer tokens are never shared through this repository.

Token guidance:
- Prefer fine-grained personal access tokens.
- Restrict token access to only the repositories being monitored.
- Use read-only permissions where possible.
- Rotate or revoke tokens immediately if exposed.

Never share:
- `GITHUB_TOKEN` values
- `.env` files
- terminal screenshots containing secrets
