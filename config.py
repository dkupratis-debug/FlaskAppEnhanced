import os
from datetime import timedelta


def _env_int(name, default):
    try:
        return int(os.environ.get(name, str(default)))
    except (TypeError, ValueError):
        return default


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-not-secret")
    JSON_SORT_KEYS = False
    MAX_CONTENT_LENGTH = _env_int("MAX_CONTENT_LENGTH", 1_048_576)  # 1 MiB
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = _env_int("WTF_CSRF_TIME_LIMIT", 3600)
    RATELIMIT_HEADERS_ENABLED = True
    RATELIMIT_DEFAULT = os.environ.get("RATELIMIT_DEFAULT", "200 per day;50 per hour")
    RATELIMIT_STORAGE_URI = os.environ.get("RATELIMIT_STORAGE_URI", "memory://")
    TRUST_PROXY_COUNT = _env_int("TRUST_PROXY_COUNT", 0)
    CONTENT_SECURITY_POLICY = os.environ.get("CONTENT_SECURITY_POLICY", "default-src 'self'")
    ENV = os.environ.get("FLASK_ENV", "development").lower()
    PERMANENT_SESSION_LIFETIME = timedelta(hours=12)


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = "https"
