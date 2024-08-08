import logging
from settings.env_settings import settings


class LoggingFormatter(logging.Formatter):
    GREEN = "\033[0;32m"
    YELLOW = "\x1b[33;20m"
    RED = "\033[0;31m"
    RESET = "\x1b[0m"
    FORMAT = "%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    FORMATS = {
        logging.DEBUG: GREEN + FORMAT + RESET,
        logging.INFO: GREEN + FORMAT + RESET,
        logging.WARNING: YELLOW + FORMAT + RESET,
        logging.ERROR: RED + FORMAT + RESET,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)

        return formatter.format(record)


def init_logging():
    logger = logging.getLogger()

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(LoggingFormatter())
    logger.addHandler(stream_handler)
    logger.setLevel(settings.LOG_LEVEL)

    return logger


logger = init_logging()
