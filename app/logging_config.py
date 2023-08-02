LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s | %(levelname)s | %(name)s.%(funcName)s | %(message)s",
            "datefmt": "%F %T",
        }
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "level": "DEBUG", "formatter": "verbose"}
    },
    "root": {"level": "DEBUG", "handlers": ["console"]},
    "disable_existing_loggers": False,
}
