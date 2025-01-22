import logging
import os
from src.config.config import settings


def log_method_call(func):
    async def wrapper(*args, **kwargs):
        logger.debug(f"Calling {func.__name__} ")  # with args: {args}, kwargs: {kwargs}")
        try:
            result = await func(*args, **kwargs)
            # logger.debug(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise

    return wrapper


root_dir = os.path.dirname(os.path.realpath(__file__))
log_dir = os.path.join(root_dir, 'app', 'logs')

os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, '.log')

logger = logging.getLogger()
logger.setLevel(settings.LOGGER_LEVEL)

file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(settings.LOGGER_LEVEL)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(settings.LOGGER_LEVEL)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

fastapi_logger = logging.getLogger("fastapi")
fastapi_logger.setLevel(settings.LOGGER_LEVEL)

fastapi_logger.addHandler(file_handler)
fastapi_logger.addHandler(console_handler)

logger.info("Logger has been initialized and is ready to write logs.")

# ░░░░░░░░░░░░░░░░░░░░
# ░░░░░ЗАПУСКАЕМ░░░░░░░
# ░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░
# ▄███▀░◐░░░▌░░░░░░░░░
# ░░░░▌░░░░░▐░░░░░░░░░
# ░░░░▐░░░░░▐░░░░░░░░░
# ░░░░▌░░░░░▐▄▄░░░░░░░
# ░░░░▌░░░░▄▀▒▒▀▀▀▀▄
# ░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
# ░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
# ░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
# ░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
# ░░░░░░░░░░░▌▌░▌▌░░░░░
# ░░░░░░░░░░░▌▌░▌▌░░░░░
# ░░░░░░░░░▄▄▌▌▄▌▌░░░░░
