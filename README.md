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
