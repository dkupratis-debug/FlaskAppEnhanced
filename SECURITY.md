# Security Policy

## Supported Versions
This is a demo project. If you find a vulnerability, please report it via GitHub Issues.

## Deployment Checklist
- Set a strong `SECRET_KEY` via environment variables.
- Run behind HTTPS so `SESSION_COOKIE_SECURE=True` works as intended.
- Set `RATELIMIT_STORAGE_URI` to Redis in production.
- Review CSRF exemptions; remove them for state-changing endpoints.
- Keep dependencies updated and review security advisories.
- Restrict CORS if you add API usage from browsers.
- Set `LOG_FILE` to rotate logs in production.

## Reporting
Open an issue with steps to reproduce and impact details.
