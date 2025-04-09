import os

import dotenv

from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

config_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(config_dir)
root = os.path.dirname(src_dir)
dev = os.path.join(root, 'dev', '.env')
dotenv.load_dotenv(dotenv_path=dev)


class Settings(BaseSettings):
    LOGGER_LEVEL: str = os.getenv('LOGGER_LEVEL')

    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: str = os.getenv('DB_PORT')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_USER: str = os.getenv('DB_USER')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')

    SCHEMA: str = os.getenv('SCHEMA', 'public')

    @property
    def DATABASE_URL_psycopg(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()

async_engine = create_async_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,          # Логирование SQL-запросов
    pool_size=5,        # Размер пула подключений
    max_overflow=10     # Максимальное количество подключений
)

session_async = async_sessionmaker(
    bind=async_engine,
)

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
