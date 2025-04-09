from abc import ABC
from typing import AsyncIterator, List, Iterator

from .base_repository_abs import BaseRepositoryABS
from ...entities.abstractions.news_entity_abs import NewsEntityABS


class NewsRepositoryABS(BaseRepositoryABS, ABC):
    async def get_one(self, id: str):
        pass

    async def get_any(self, ids: List[str]) -> List[NewsEntityABS] | None:
        pass

    async def get_batch(self, batch_size: int = 2 ** 16, offset: int = 0) -> List[NewsEntityABS] | None:
        pass

    async def insert_one(self, data: NewsEntityABS) -> None:
        pass

    async def insert_many(self, data: List[NewsEntityABS]) -> None:
        pass

    async def get_all(self, chunk_size: int = 2 ** 16) -> Iterator[List[NewsEntityABS]]:
        pass

    async def get_all_slow(self) -> Iterator[NewsEntityABS]:
        pass