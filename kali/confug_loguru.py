from loguru import logger


def config_loguru():
    logger.add("logs/{time:YYYY-MM-DD}/{time}.log", rotation="6h", level="INFO")
