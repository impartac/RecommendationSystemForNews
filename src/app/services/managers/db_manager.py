from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.config.logger_config import logger, log_method_call
from typing import List, Any, Type, AsyncIterator
from abc import ABC


class BaseDBManager(ABC):
    def __init__(self, database_url: str, echo=False, pool_size=5, max_overflow=10):
        self.engine = create_async_engine(
            url=database_url,
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow
        )
        self.async_session = async_sessionmaker(bind=self.engine)
        self.model_type = None

    '''
    self.__orig_class__.__args__[0] - getting correct type T for sqlalchemy funcs.
    '''

    @log_method_call
    async def create_tables_if_not_exists(self, metadata):
        async with self.engine.begin() as conn:
            for table in metadata.tables.values():
                try:
                    await conn.run_sync(metadata.create_all, tables=[table])
                    logger.info(f"Таблица '{table.name}' создана.")
                except Exception as e:
                    logger.info(e)

    @log_method_call
    async def get_one(self, id: str) -> Type | None:
        try:
            async with self.async_session() as session:
                res = await session.get(self.model_type, id)
                return res
        except Exception as e:
            logger.error(f"Error during get_one: {e}")
            return None

    @log_method_call
    async def get_any(self, ids: List[str]) -> List[Any] | None:
        try:
            async with self.async_session() as session:
                query = select(self.model_type).where(
                    getattr(self.model_type, "id").in_(ids))
                result = await session.execute(query)
                return list(result.scalars().all())
        except Exception as e:
            logger.error(f"Error during get_any: {e}")
            return None

    @log_method_call
    async def get_batch(self, batch_size: int = 2 ** 16, offset: int = 0) -> List[Any]:
        try:
            async with self.async_session() as session:
                query = select(self.model_type).limit(batch_size).offset(offset)
                result = await session.execute(query)
                logger.info(f"Method get_batch select data from {offset} to {offset + batch_size}")
                return list(result.scalars().all())
        except Exception as e:
            logger.error(f"Error during get_batch: {e}")
            return []

    @log_method_call
    async def insert_one(self, data: Any) -> None:
        try:
            async with self.async_session() as session:
                session.add(data)
                await session.commit()
        except Exception as e:
            logger.error(f"Error during insert_one: {e}")
            return None

    @log_method_call
    async def insert_many(self, data: List[Any]) -> None:
        try:
            async with self.async_session() as session:
                session.add_all(data)
                await session.commit()
        except Exception as e:
            logger.error(f"Error during insert_many: {e}")
            return None

    async def get_all(self, chunk_size: int = 2**16) -> AsyncIterator[Any]:
        """Fetch vectors from db in chunks"""
        offset = 0
        async with self.async_session() as session:
            while True:
                query = select(self.model_type).limit(chunk_size).offset(offset)
                result = await session.execute(query)
                vectors = result.scalars().all()
                if not vectors:
                    break
                offset += chunk_size
                yield vectors

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
