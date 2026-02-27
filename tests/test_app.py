import pytest

from app import create_app


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
    assert b"const tracks" in res.data
    assert b"localStorage" in res.data


def test_production_requires_non_default_secret_key(monkeypatch):
    monkeypatch.setenv("FLASK_ENV", "production")
    monkeypatch.delenv("SECRET_KEY", raising=False)
    with pytest.raises(RuntimeError, match="Production requires a strong SECRET_KEY"):
        create_app()
