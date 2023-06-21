from pydantic import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str = "../models/best_model.pkl"
    ESTIMATED_STDEV: float = 50581.26

    LOGGER_CONFIG: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(levelprefix)s %(message)s",
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
        },
        "loggers": {
            "default": {"handlers": ["default"], "level": "DEBUG"},
        },
    }

settings = Settings()