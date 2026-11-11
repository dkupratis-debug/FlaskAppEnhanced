import logging
import re
from pathlib import Path

import pytest

import config
from app import create_app

BROWSER_ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"


def _csrf_token(client):
    page = client.get("/submit")
    assert page.status_code == 200
    match = re.search(br'name="csrf_token" value="([^"]+)"', page.data)
    assert match, page.data
    return match.group(1).decode()


def test_home():
    app = create_app()
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"FlaskAppEnhanced" in res.data
    assert b"Health check" in res.data
    assert res.headers["X-Content-Type-Options"] == "nosniff"
    assert res.headers["X-Frame-Options"] == "DENY"
    assert "X-Request-Id" in res.headers


def test_health():
    app = create_app()
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_api_echo():
    app = create_app()
    client = app.test_client()
    res = client.post("/api/echo", json={"hello": "world"})
    assert res.status_code == 200
    assert res.get_json() == {"received": {"hello": "world"}}


def test_submit_form_page_includes_csrf_field():
    app = create_app()
    client = app.test_client()
    res = client.get("/submit")
    assert res.status_code == 200
    assert b'name="csrf_token"' in res.data
    assert res.headers["X-Content-Type-Options"] == "nosniff"


def test_learn_dashboard_page_loads():
    app = create_app()
    client = app.test_client()
    res = client.get("/learn")
    assert res.status_code == 200
    assert b"Learning Dashboard" in res.data
    assert b"Choose a track" in res.data
    assert b"/static/learn.js" in res.data


def test_learn_lab_page_loads():
    app = create_app()
    client = app.test_client()
    res = client.get("/learn-lab")
    assert res.status_code == 200
    assert b"Interactive Learning Lab" in res.data
    assert b"Simulation Mode" in res.data
    assert b"Copy command" in res.data
    assert b"/static/learn_lab.js" in res.data


def test_launch_page_loads():
    app = create_app()
    client = app.test_client()
    res = client.get("/launch")
    assert res.status_code == 200
    assert b"FlaskAppEnhanced Launchpad" in res.data
    assert b"Community" in res.data


def test_production_requires_non_default_secret_key(monkeypatch):
    monkeypatch.setenv("FLASK_ENV", "production")
    monkeypatch.delenv("SECRET_KEY", raising=False)
    with pytest.raises(RuntimeError, match="Production requires a strong SECRET_KEY"):
        create_app()


def test_missing_csrf_token_returns_400():
    app = create_app()
    app.config["PROPAGATE_EXCEPTIONS"] = False
    client = app.test_client()

    html = client.post("/submit", data={"name": "Ada"}, headers={"Accept": "text/html"})
    assert html.status_code == 400
    assert html.content_type.startswith("text/html")
    assert b"The CSRF token is missing." in html.data
    assert b"Bad Request" in html.data
    assert html.headers["X-Request-Id"]
    assert html.headers["X-Content-Type-Options"] == "nosniff"

    api = client.post(
        "/submit", data={"name": "Ada"}, headers={"Accept": "application/json"}
    )
    assert api.status_code == 400
    assert api.get_json() == {"error": "The CSRF token is missing."}
    assert api.headers["X-Request-Id"]


def test_invalid_csrf_token_returns_400():
    app = create_app()
    app.config["PROPAGATE_EXCEPTIONS"] = False
    client = app.test_client()
    _csrf_token(client)

    html = client.post(
        "/submit",
        data={"name": "Ada", "csrf_token": "not-a-valid-token"},
        headers={"Accept": "text/html"},
    )
    assert html.status_code == 400
    assert b"The CSRF token is invalid." in html.data
    assert html.headers["X-Request-Id"]

    api = client.post(
        "/submit",
        data={"name": "Ada", "csrf_token": "not-a-valid-token"},
        headers={"Accept": "application/json"},
    )
    assert api.status_code == 400
    assert api.get_json() == {"error": "The CSRF token is invalid."}


def test_request_id_header_when_before_request_did_not_run():
    app = create_app()
    funcs = app.before_request_funcs[None]
    app.before_request_funcs[None] = [
        fn for fn in funcs if getattr(fn, "__name__", "") != "attach_request_id"
    ]
    client = app.test_client()

    echoed = client.get("/health", headers={"X-Request-Id": "fixed-id"})
    assert echoed.status_code == 200
    assert echoed.headers["X-Request-Id"] == "fixed-id"

    generated = client.get("/health")
    assert generated.status_code == 200
    assert generated.headers["X-Request-Id"]
    assert generated.headers["X-Request-Id"] != "fixed-id"


def test_learn_pages_use_external_scripts_under_strict_csp():
    app = create_app()
    client = app.test_client()
    pages = {
        "/learn": "/static/learn.js",
        "/learn-lab": "/static/learn_lab.js",
    }
    for path, script_path in pages.items():
        res = client.get(path)
        assert res.status_code == 200
        assert script_path.encode() in res.data
        assert b"<script>" not in res.data
        csp = res.headers["Content-Security-Policy"]
        assert csp == "default-src 'self'"
        assert "unsafe-inline" not in csp
        script = client.get(script_path)
        assert script.status_code == 200
        assert script.content_type.startswith("text/javascript") or script.content_type.startswith(
            "application/javascript"
        )

    learn_js = client.get("/static/learn.js").data
    assert b"const tracks" in learn_js
    assert b"localStorage" in learn_js
    lab_js = client.get("/static/learn_lab.js").data
    assert b"const scenarios" in lab_js
    assert b"flaskappenhanced-learn-lab-progress" in lab_js


def _logged_remote(app, forwarded_for):
    found = []

    class Capture(logging.Handler):
        def emit(self, record):
            if record.getMessage() == "request":
                found.append(record.remote)

    app.logger.addHandler(Capture())
    app.test_client().get("/health", headers={"X-Forwarded-For": forwarded_for})
    assert found
    return found[-1]


def test_request_log_ignores_forwarded_for_unless_proxy_is_trusted(monkeypatch):
    app = create_app()
    assert app.config["TRUST_PROXY_COUNT"] == 0
    assert _logged_remote(app, "203.0.113.50") == "127.0.0.1"

    monkeypatch.setattr(config.DevelopmentConfig, "TRUST_PROXY_COUNT", 1)
    trusted = create_app()
    assert trusted.config["TRUST_PROXY_COUNT"] == 1
    assert _logged_remote(trusted, "203.0.113.50") == "203.0.113.50"


def test_makefile_targets_are_cross_platform():
    text = (Path(__file__).resolve().parents[1] / "Makefile").read_text(encoding="utf-8")
    assert "activate" not in text
    assert "$env:" not in text
    assert "Windows_NT" in text
    assert "venv/bin/python" in text
    assert "venv/Scripts/python.exe" in text
    for target in ("install", "dev", "test", "lint", "run", "prod"):
        assert f"{target}:" in text


def test_browser_form_post_redirects_back_with_success_message():
    app = create_app()
    client = app.test_client()
    token = _csrf_token(client)
    res = client.post(
        "/submit",
        data={"name": "Ada", "csrf_token": token},
        headers={"Accept": BROWSER_ACCEPT},
    )
    assert res.status_code == 302
    assert res.headers["Location"].endswith("/submit")
    assert res.get_json() is None
    page = client.get(res.headers["Location"])
    assert page.status_code == 200
    assert page.content_type.startswith("text/html")
    assert b"Thanks, Ada." in page.data
    assert b"Sample Form" in page.data
    assert b'name="csrf_token"' in page.data


def test_json_and_fetch_submit_still_return_json():
    app = create_app()
    client = app.test_client()
    cases = [
        {"Accept": "application/json"},
        {"Accept": "*/*"},
        {},
    ]
    for headers in cases:
        token = _csrf_token(client)
        res = client.post(
            "/submit",
            data={"name": "Ada", "csrf_token": token},
            headers=headers,
        )
        assert res.status_code == 200, headers
        assert res.get_json() == {"message": "Thanks, Ada."}
