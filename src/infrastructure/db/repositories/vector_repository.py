from typing import List, Iterable, Iterator

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories.abstractions.vector_repository_abs import VectorRepositoryABS
from core.entities.implementation.domain_vector import DomainVector
from ..factories.implementation.vector_factory import VectorFactory
from ..models.vector_orm import VectorORM
from src.config.logger_config import logger
from sqlalchemy.dialects.postgresql import insert as pg_insert


class VectorRepository(VectorRepositoryABS):

    def __init__(self, session: AsyncSession):
        self._session = session
        self.factory = VectorFactory()

    async def get_one(self, id: str):
        """
        Get one element from database by id
        :param id:
        :return: Element or None if not found
        """
        try:
            res = await self._session.get(VectorORM, id)
            return self.factory.to_entity(res)
        except Exception as e:
            logger.error(f"Error during get_one: {e}")
            return None

    async def insert_one(self, vector: DomainVector) -> None:
        """
        Insert one element into database
        :param vector:
        :return:
        """
        try:
            orm_vector = self.factory.to_orm(vector)
            self._session.add(orm_vector)
            await self._session.commit()
        except Exception as e:
            logger.error(f"Error during get_one: {e}")
            return None

    async def insert_many(self, vectors: Iterable[DomainVector]) -> None:
        try:
            orm_vectors = list(map(self.factory.to_orm, vectors))
            self._session.add_all(orm_vectors)
            await self._session.commit()
            logger.info(f"Inserted {len(orm_vectors)} vectors")
        except Exception as e:
            logger.error(f"Error during insert_many: {e}")

    async def get_all(self, chunk_size: int = 2 ** 30) -> Iterator[List[DomainVector]]:
        offset = 0
        factory = VectorFactory()
        while True:
            logger.info(f"Offset: {offset}")
            query = select(VectorORM).limit(chunk_size).offset(offset).order_by(VectorORM.id)
            result = await self._session.execute(query)
            news = result.scalars().all()
            if not news:
                break
            offset += chunk_size
            news = list(map(factory.to_entity, news))
            yield news

    async def get_all_slow(self) -> List[DomainVector]:
        query = select(VectorORM).order_by(VectorORM.id)
        logger.info(f"Getting all vectors from database")
        result = await self._session.execute(query)
        logger.info(f"Vectors have been loaded")
        news = result.scalars().all()
        factory = VectorFactory()
        return list(map(factory.to_entity, news))

    async def get_any(self, ids: Iterable[id]) -> List[DomainVector]:
        query = select(VectorORM).where(VectorORM.id.in_(ids))
        logger.info(f"Getting {len(ids)} vectors from database")
        result = await self._session.execute(query)
        news = result.scalars().all()
        factory = VectorFactory()
        return list(map(factory.to_entity, news))
