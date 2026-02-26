import json
import logging
import os
import time
import uuid

from flask import Flask, jsonify, g, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf import CSRFProtect

from app.ratelimit import rate_limit_storage_uri


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = getattr(g, "request_id", "-")
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


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "development").lower()
    config_obj = "config.ProductionConfig" if env == "production" else "config.DevelopmentConfig"
    app.config.from_object(config_obj)

    handler = logging.StreamHandler()
    handler.setFormatter(JsonLogFormatter())
    handler.addFilter(RequestIdFilter())
    app.logger.handlers.clear()
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    CSRFProtect(app)

    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=app.config.get("RATELIMIT_DEFAULT"),
        storage_uri=rate_limit_storage_uri(),
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

    @app.get("/submit")
    def submit_form():
        return render_template("form.html")

    @app.post("/submit")
    def handle_submit():
        name = request.form.get("name", "anonymous").strip() or "anonymous"
        return jsonify(message=f"Thanks, {name}.")

    @app.get("/health")
    @limiter.exempt
    def health():
        return jsonify(status="ok")

    @app.after_request
    def set_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "no-referrer")
        response.headers.setdefault("Content-Security-Policy", "default-src 'self'")
        return response

    return app
