import uuid
from datetime import datetime
from typing import Optional, List
from core.entities.implementation.domain_news import DomainNews
from core.entities.implementation.domain_recommendation import DomainRecommendation
from core.repositories.abstractions.news_repository_abs import NewsRepositoryABS
from core.services.vector_service import VectorService
from core.services.recommendation_service import RecommendationService
from logging import getLogger

logger = getLogger(__name__)


class NewsUseCase:
    def __init__(self, vector_service: VectorService,
                 recommendation_service: RecommendationService,
                 news_repository: NewsRepositoryABS):
        self._vector_service = vector_service
        self._recommendation_service = recommendation_service
        self._news_repository = news_repository

    async def create_news(self, anons: str, title: str, body: str) -> DomainNews:
        logger.info(f'Creating news for anonymous: {anons}')
        entity = DomainNews(
            id=str(uuid.uuid4()),
            anons=anons,
            title=title,
            body=body,
            date_creation=datetime.now()
        )
        await self._news_repository.insert_one(entity)
        return entity

    async def get_news(self, id: str) -> Optional[DomainNews]:
        logger.info(f'Getting news for {id}')
        news = await self._news_repository.get_one(id)
        logger.info(f'New news found: {news}')
        return news

    # async def get_recommendations(self, id: str) -> List[Optional[DomainNews]]:
    #     logger.info(f'Getting recommendations for {id}')
    #     recs = await self._recommendation_service.recommendation_repository.get_one(id)
    #     logger.info(f'Recommendations found: {recs}')
    #     if recs:
    #         return [await self.get_news(i) for i in recs.recommendations]
    #     return [None] * 5

    async def vectorize(self, news: DomainNews) -> None:
        try:
            logger.info(f'Vectorizing news: {news}')
            await self._vector_service.vectorize(news)
            logger.info(f'Vectorized news: {news}')
        except Exception as e:
            logger.error(f'Failed to vectorize news : {e}')

    async def vectorize_all(self) -> None:
        logger.info(f'Vectorizing all news')
        logger.info(f'News has been vectorized')
        news = self._news_repository.get_all()
        async for i in news:
            logger.info(f'News batch size:{len(i)}')
            await self._vector_service.vectorize_batch(i)

    async def get_recommendation(self, news: DomainNews) -> DomainRecommendation:
        logger.info(f'Getting recommendations : {news.id}')
        _id = news.id
        vector = await self._vector_service.get_one(_id)
        ids = await self._recommendation_service.recommendation_repository.get_one(_id)
        if ids is None:
            logger.info(f'No recommendations for {_id}. Building recs')
            ids = self._recommendation_service.recommender_model.predict(vector)
            logger.info(f'Recommendations for {_id} has been built')
        else:
            ids = ids.recommendations
        return DomainRecommendation(
            id=_id,
            recommendations=ids
        )

    async def insert_recommendation(self, news: DomainRecommendation) -> None:
        logger.info(f'Inserting recommendations for {news.id}')
        await self._recommendation_service.insert_one(news)
        logger.info(f'Recommendations for {news.id} has been inserted')

    async def get_recommendations(self, news: List[DomainNews]) -> List[DomainRecommendation]:
        logger.info(f'Getting recommendations for {len(news)}')
        vector_ids = await self._vector_service.get_any([i.id for i in news])
        logger.info(f'Vectors have been got')
        recs_ids = self._recommendation_service.recommender_model.predict_batch(vector_ids)
        logger.info(f'Recommendations have been built')
        ans = [DomainRecommendation(vector_ids[i].id, recs_ids[i]) for i in range(len(news))]
        return ans

    async def insert_recommendations(self, recs: List[DomainRecommendation]) -> None:
        logger.info(f'Inserting recommendations for {len(recs)}')
        await self._recommendation_service.recommendation_repository.insert_many(recs)
        logger.info(f'Recommendations for {len(recs)} has been inserted')
