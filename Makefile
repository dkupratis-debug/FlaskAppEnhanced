.PHONY: install dev test lint run prod

install:
	python -m venv venv
	.\venv\Scripts\activate && pip install -r requirements.txt

# Install dev dependencies

dev:
	.\venv\Scripts\activate && pip install -r requirements-dev.txt

# Run tests

test:
	.\venv\Scripts\activate && pytest -q

# Lint

lint:
	.\venv\Scripts\activate && ruff check .

# Run dev server

run:
	.\venv\Scripts\activate && python app.py

# Run production server

prod:
	$env:FLASK_ENV="production"; .\venv\Scripts\activate; gunicorn -c gunicorn.conf.py wsgi:app
