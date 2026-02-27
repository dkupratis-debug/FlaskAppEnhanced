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
