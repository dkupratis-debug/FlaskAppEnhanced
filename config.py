import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-not-secret")
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
