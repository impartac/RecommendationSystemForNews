import asyncio

from src.config.config import settings
from src.app.services.models.vector_orm import VectorORM
from src.app.services.helpers.vectorizer import Vectorizer
from src.app.services.managers.news_manager import NewsManager
from src.app.services.models.news_orm import NewsORM
from src.app.services.managers.vector_manager import VectorManager
from src.app.services.helpers.utils import Utils


async def vectorize_data():
    news_manager = NewsManager(settings.DATABASE_URL_psycopg, NewsORM)
    vectorizer = Vectorizer()
    vector_manager = VectorManager(settings.DATABASE_URL_psycopg, VectorORM, vectorizer)
    await Utils.transform_all_news(news_manager, vector_manager)


if __name__ == '__main__':
    asyncio.run(vectorize_data())

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
