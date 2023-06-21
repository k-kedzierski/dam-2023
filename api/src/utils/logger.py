import logging
from logging.config import dictConfig

from src.config import settings

dictConfig(settings.LOGGER_CONFIG)

def get_logger() -> logging.Logger:
    return logging.getLogger("default")
