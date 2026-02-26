import os
import time
import uuid

from flask import Flask, jsonify, g, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf import CSRFProtect


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "development").lower()
    config_obj = "config.ProductionConfig" if env == "production" else "config.DevelopmentConfig"
    app.config.from_object(config_obj)

    CSRFProtect(app)

    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=app.config.get("RATELIMIT_DEFAULT"),
    )

    @app.before_request
    def attach_request_id():
        g.request_id = request.headers.get("X-Request-Id", str(uuid.uuid4()))
        g.start_time = time.time()

    @app.after_request
    def add_request_id_header(response):
        response.headers.setdefault("X-Request-Id", g.request_id)
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
