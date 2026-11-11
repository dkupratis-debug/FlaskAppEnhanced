# Call the venv interpreter directly. No shell activation, so the same
# targets work on Linux, macOS, and Windows.
ifeq ($(OS),Windows_NT)
PY_BOOT := python
PY := venv/Scripts/python.exe
ENV_RUN := set FLASK_ENV=production&&
else
PY_BOOT := $(shell command -v python3 >/dev/null 2>&1 && echo python3 || echo python)
PY := venv/bin/python
ENV_RUN := FLASK_ENV=production
endif

.PHONY: install dev test lint run prod

install:
	$(PY_BOOT) -m venv venv
	$(PY) -m pip install -r requirements.txt

dev:
	$(PY) -m pip install -r requirements-dev.txt

test:
	$(PY) -m pytest -q

lint:
	$(PY) -m ruff check .

run:
	$(PY) app.py

prod:
	$(ENV_RUN) $(PY) -m gunicorn -c gunicorn.conf.py wsgi:app
