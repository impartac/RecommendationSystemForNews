import os
from typing import Generator

import joblib
import pandas as pd
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.services.vector_service import VectorService
from core.use_cases.news_use_case import NewsUseCase
from ..db.models.news_orm import NewsORM
from ..db.repositories.news_repository import NewsRepository
from ..db.repositories.vector_repository import VectorRepository
from ..db.repositories.recommendations_repository import RecommendationsRepository
from ..ml.Vectorizer import VectorizerModel
from ..db.session import get_async_db_session
from core.services.recommendation_service import RecommendationService
from ..ml.KNNmodel import KNN
from config.logger_config import logger


async def get_news_use_case(
        news_session: AsyncSession = Depends(get_async_db_session),
        recommendation_session: AsyncSession = Depends(get_async_db_session),
        vector_session: AsyncSession = Depends(get_async_db_session),
) -> NewsUseCase:
    news_repo = NewsRepository(news_session)
    recommendations_repo = RecommendationsRepository(recommendation_session)
    vector_repo = VectorRepository(vector_session)

    vector_service = VectorService(vector_repo, VectorizerModel())
    knn = KNN()
    if not knn.has_built:
        logger.info("KNN loading")
        knn.model = joblib.load(
            f"C:\\Users\\32233\\OneDrive\\Documents\\HSE\\Курсач\\RecommendationSystemforNews\\src\\knn")
        logger.info("KNN model loaded")
        logger.info(f"news_ids loading")
        query = select(NewsORM.id).order_by(NewsORM.id)
        logger.info(f"Getting news ids")
        knn.news_ids = await news_repo._session.execute(query)
        knn.news_ids = knn.news_ids.scalars().all()
        print(len(knn.news_ids))
        logger.info(f"Ids has been got")
        knn.has_built = True
    recommendation_service = RecommendationService(recommendations_repo, knn)

    return NewsUseCase(vector_service, recommendation_service, news_repo)


# def get_knn_model() -> Generator[RecommendationModelAbstraction, None, None]:
#     """Зависимость для получения KNN модели"""
#     model = None
#     try:
#         if os.path.exists("knn.joblib"):
#             model = joblib.load("knn.joblib")
#             logger.info("Model loaded")
#         else:
#             # Инициализируем новую модель
#             from infrastructure.ml.KNNmodel import KNN
#             model = KNN()
#             logger.info("New model activated")
#         yield model
#
#     except Exception as e:
#         logger.error(e)
#         raise


async def get_vector_service(
        vector_session: AsyncSession = Depends(get_async_db_session),
        vector_model: VectorizerModel = VectorizerModel(),
) -> VectorService:
    vector_repo = VectorRepository(vector_session)
    return VectorService(vector_repo, vector_model)
