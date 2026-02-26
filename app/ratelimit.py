from flask import current_app


def rate_limit_storage_uri():
    uri = current_app.config.get("RATELIMIT_STORAGE_URI", "memory://")
    env = current_app.config.get("ENV", "development")
    if env == "production" and uri.startswith("memory"):
        current_app.logger.warning(
            "RATELIMIT_STORAGE_URI is memory:// in production; use Redis for accuracy."
        )
    return uri
