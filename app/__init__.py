import os

from flask import Flask, jsonify, render_template


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "development").lower()
    config_obj = "config.ProductionConfig" if env == "production" else "config.DevelopmentConfig"
    app.config.from_object(config_obj)

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/health")
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
