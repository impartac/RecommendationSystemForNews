import asyncio

from src.app.services.recommendations_builder import RecommendationBuilder
from src.config.config import settings
from src.app.services.models.vector_orm import VectorORM
from src.app.services.helpers.vectorizer import Vectorizer
from src.app.services.managers.news_manager import NewsManager
from src.app.services.models.news_orm import NewsORM
from src.app.services.managers.vector_manager import VectorManager


async def main():
    news_manager = NewsManager(settings.DATABASE_URL_psycopg, NewsORM)
    vectorizer = Vectorizer()
    vector_manager = VectorManager(settings.DATABASE_URL_psycopg, VectorORM, vectorizer)
    recommendations_builder = RecommendationBuilder(news_manager, vector_manager)
    recommendations_builder.load_model()
    recommendations_builder.knn()

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
