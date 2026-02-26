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


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "development").lower()
    config_obj = "config.ProductionConfig" if env == "production" else "config.DevelopmentConfig"
    app.config.from_object(config_obj)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s request_id=%(request_id)s %(message)s"
    )
    handler.setFormatter(formatter)
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
            "method=%s path=%s status=%s duration_ms=%s remote=%s",
            request.method,
            request.path,
            response.status_code,
            duration_ms,
            request.headers.get("X-Forwarded-For", request.remote_addr),
        )
        return response

    @app.get("/")
    def home():
        return render_template("index.html")

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
