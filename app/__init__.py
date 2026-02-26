import os

from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "development").lower()
    config_obj = "config.ProductionConfig" if env == "production" else "config.DevelopmentConfig"
    app.config.from_object(config_obj)

    @app.get("/")
    def home():
        return "FlaskAppEnhanced is running"

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    return app
