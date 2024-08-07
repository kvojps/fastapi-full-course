import logging
from settings.env_settings import settings


class LoggingFormatter(logging.Formatter):
    green = "\033[0;32m"
    yellow = "\x1b[33;20m"
    red = "\033[0;31m"
    reset = "\x1b[0m"
    format = (
        "%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: green + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)

        return formatter.format(record)


def init_logging():
    logger = logging.getLogger()

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(LoggingFormatter())
    logger.setLevel(settings.LOG_LEVEL)
    logger.addHandler(stream_handler)

    return logger


logger = init_logging()
