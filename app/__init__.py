import json
import logging
import os
import time
import uuid
from logging.handlers import RotatingFileHandler

from flask import Flask, g, has_request_context, jsonify, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf import CSRFProtect
from werkzeug.middleware.proxy_fix import ProxyFix

from app.ratelimit import rate_limit_storage_uri


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        if has_request_context():
            record.request_id = getattr(g, "request_id", "-")
        else:
            record.request_id = "-"
        return True


class JsonLogFormatter(logging.Formatter):
    def format(self, record):
        payload = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "request_id": getattr(record, "request_id", "-"),
        }
        for key in ("method", "path", "status", "duration_ms", "remote"):
            if hasattr(record, key):
                payload[key] = getattr(record, key)
        return json.dumps(payload, separators=(",", ":"))


def _normalize_limits(value):
    if value is None:
        return ["200 per day", "50 per hour"]
    if isinstance(value, (list, tuple)):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        s = value.strip()
        if not s:
            return ["200 per day", "50 per hour"]
        if s.isdigit():
            return [f"{s} per day"]
        return [part.strip() for part in s.replace(",", ";").split(";") if part.strip()]
    return ["200 per day", "50 per hour"]


def _validate_production_secret_key(app, env):
    if env != "production":
        return
    secret_key = str(app.config.get("SECRET_KEY", "")).strip()
    if secret_key in {"", "dev-not-secret"}:
        raise RuntimeError(
            "Production requires a strong SECRET_KEY. Set SECRET_KEY in the environment."
        )


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "development").lower()
    config_obj = "config.ProductionConfig" if env == "production" else "config.DevelopmentConfig"
    app.config.from_object(config_obj)
    _validate_production_secret_key(app, env)
    trust_proxy_count = int(app.config.get("TRUST_PROXY_COUNT", 0) or 0)
    if trust_proxy_count > 0:
        app.wsgi_app = ProxyFix(
            app.wsgi_app,
            x_for=trust_proxy_count,
            x_proto=trust_proxy_count,
            x_host=trust_proxy_count,
        )

    log_file = os.environ.get("LOG_FILE")
    if log_file:
        max_bytes = int(os.environ.get("LOG_MAX_BYTES", "10485760"))
        backup_count = int(os.environ.get("LOG_BACKUP_COUNT", "5"))
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    else:
        handler = logging.StreamHandler()
    handler.setFormatter(JsonLogFormatter())
    handler.addFilter(RequestIdFilter())
    app.logger.handlers.clear()
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    csrf = CSRFProtect(app)

    app.config["RATELIMIT_DEFAULT"] = _normalize_limits(app.config.get("RATELIMIT_DEFAULT"))
    limits = app.config.get("RATELIMIT_DEFAULT")

    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=limits,
        storage_uri=rate_limit_storage_uri(app.config, app.logger),
    )

    @app.before_request
    def attach_request_id():
        g.request_id = request.headers.get("X-Request-Id", str(uuid.uuid4()))
        g.start_time = time.time()

    @app.after_request
    def add_request_id_header(response):
        response.headers.setdefault("X-Request-Id", g.request_id)
        duration_ms = int((time.time() - g.start_time) * 1000)
        app.logger.info(
            "request",
            extra={
                "method": request.method,
                "path": request.path,
                "status": response.status_code,
                "duration_ms": duration_ms,
                "remote": request.headers.get("X-Forwarded-For", request.remote_addr),
            },
        )
        return response

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/learn")
    def learn():
        return render_template("learn.html")

    @app.get("/submit")
    def submit_form():
        return render_template("form.html")

    @app.post("/submit")
    def handle_submit():
        name = request.form.get("name", "anonymous").strip() or "anonymous"
        return jsonify(message=f"Thanks, {name}.")

    @app.post("/api/echo")
    @limiter.limit("30 per minute")
    @csrf.exempt
    def api_echo():
        payload = request.get_json(silent=True) or {}
        return jsonify(received=payload)

    @app.get("/health")
    @limiter.exempt
    def health():
        return jsonify(status="ok")

    @app.after_request
    def set_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "no-referrer")
        response.headers.setdefault(
            "Content-Security-Policy",
            app.config.get("CONTENT_SECURITY_POLICY", "default-src 'self'"),
        )
        return response

    return app
