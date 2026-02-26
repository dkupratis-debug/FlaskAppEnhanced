from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    @app.get("/")
    def home():
        return "FlaskAppEnhanced is running"

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    return app
