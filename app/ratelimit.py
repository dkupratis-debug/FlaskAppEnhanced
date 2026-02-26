def rate_limit_storage_uri(config, logger):
    uri = config.get("RATELIMIT_STORAGE_URI", "memory://")
    env = config.get("ENV", "development")
    if env == "production" and uri.startswith("memory"):
        logger.warning("RATELIMIT_STORAGE_URI is memory:// in production; use Redis for accuracy.")
    return uri
