import time
from typing import List, Iterator
from collections.abc import AsyncIterator

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.entities.abstractions.news_entity_abs import NewsEntityABS
from core.repositories.abstractions.news_repository_abs import NewsRepositoryABS
from ..factories.implementation.news_factory import     NewsFactory, NewsORM, DomainNews
from src.config.logger_config import logger


class NewsRepository(NewsRepositoryABS):

    def __init__(self, session: AsyncSession):
        self._session = session
        self.factory = NewsFactory()

    async def get_one(self, id: str, **kwargs) -> DomainNews | None:
        """
        Get one element from database by id
        :param id:
        :return: Element or None if not found
        """
        try:
            res = await self._session.get(NewsORM, id)
            return self.factory.to_entity(res)
        except Exception as e:
            logger.error(f"Error during get_one: {e}")
            return None

    async def insert_one(self, news: DomainNews, **kwargs) -> None:
        try:
            orm = self.factory.to_orm(news)
            self._session.add(orm)
            await self._session.commit()
            logger.info(f"News domain {news} has been inserted")
        except Exception as e:
            logger.error(f"Error during insert_one: {e}")

    async def get_all(self, chunk_size: int = 2 ** 15) -> Iterator[List[DomainNews]]:
        offset = 0
        factory = NewsFactory()
        while True:
            logger.info(f"Offset: {offset}")
            query = select(NewsORM).limit(chunk_size).offset(offset).order_by(NewsORM.id)
            result = await self._session.execute(query)
            news = result.scalars().all()
            if not news:
                break
            offset += chunk_size
            news = list(map(factory.to_entity, news))
            time.sleep(1)
            yield news

    async def get_all_slow(self) -> List[DomainNews]:
        query = select(NewsORM).order_by(NewsORM.id)
        result = await self._session.execute(query)
        news = result.scalars().all()
        factory = NewsFactory()
        return list(map(factory.to_entity, news))
