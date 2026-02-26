# FlaskAppEnhanced

Minimal Flask app scaffold.

## Features
- Homepage at `/`
- Health check at `/health`
- Config scaffold in `config.py`

## Run locally
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then visit http://127.0.0.1:5000/ and http://127.0.0.1:5000/health.

## Environment
Copy `.env.example` to `.env` and update values as needed.

## Run in production
```powershell
pip install -r requirements.txt
$env:FLASK_ENV="production"
$env:SECRET_KEY="change-me"
gunicorn -c gunicorn.conf.py wsgi:app
```

## Dev tooling
```powershell
pip install -r requirements-dev.txt
ruff check .
pytest
```

## Security additions
This scaffold includes:
- Rate limiting via `Flask-Limiter` (defaults from `RATELIMIT_DEFAULT`).
- CSRF protection via `Flask-WTF` for form submissions.
- Request IDs added to logs/headers via `X-Request-Id`.
- JSON logs for easy ingestion.
 - JSON API example with CSRF exemption.

### Tuning rate limits
Set `RATELIMIT_DEFAULT` (e.g., `100 per hour`) and switch storage to Redis in production:
`RATELIMIT_STORAGE_URI=redis://:password@host:6379/0`

### CSRF in templates
`layout.html` includes a CSRF meta tag you can read in JS. For HTML forms, add:
`<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">`

### Sample form
Visit `/submit` to see a CSRF-protected form that posts to `/submit`.

### JSON API example
POST `/api/echo` with JSON to see echo behavior. This route is CSRF-exempt by design.

### Log rotation
Set `LOG_FILE` to enable rotating file logs. Use `LOG_MAX_BYTES` and `LOG_BACKUP_COUNT` to tune size/retention.
