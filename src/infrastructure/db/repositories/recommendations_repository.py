from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories.abstractions.recommendations_repository_abs import RecommendationsRepositoryABS
from ..factories.implementation.recommendation_factory import RecommendationFactory
from src.config.logger_config import logger
from core.entities.implementation.domain_recommendation import DomainRecommendation
from ..models.recommendation_orm import RecommendationORM


class RecommendationsRepository(RecommendationsRepositoryABS):

    async def commit(self) -> None:
        await self._session.commit()

    def __init__(self, session: AsyncSession):
        self._session = session
        self.factory = RecommendationFactory()

    async def get_one(self, id: str, **kwargs) -> DomainRecommendation | None:
        """
        Get one element from database by id
        :param id:
        :return: Element or None if not found
        """
        try:
            res = await self._session.get(RecommendationORM, id)
            return self.factory.to_entity(res)
        except Exception as e:
            logger.error(f"Error during get_one: {e}")
            return None

    async def insert_one(self, recs: DomainRecommendation) -> None:
        try:
            orm = self.factory.to_orm(recs)
            self._session.add(orm)
            await self._session.commit()
            logger.info(f"Recs domain {recs} has been inserted")
        except Exception as e:
            logger.error(f"Error during insert_one: {e}")

    async def insert_many(self, data: List[DomainRecommendation]) -> None:
        try:
            orm = list(map(self.factory.to_orm, data))
            self._session.add_all(orm)
            await self._session.commit()
            logger.info(f"Recs domain {len(data)} has been inserted")
        except Exception as e:
            logger.error(f"Error during insert_many: {e}")

