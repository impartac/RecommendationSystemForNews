from abc import ABC
from typing import AsyncIterator, List, Iterator

from .base_repository_abs import BaseRepositoryABS
from ...entities.abstractions.vector_entity_abs import VectorEntityABS


class VectorRepositoryABS(BaseRepositoryABS, ABC):

    async def get_any(self, ids: List[str]) -> List[VectorEntityABS] | None:
        pass

    async def get_batch(self, batch_size: int = 2 ** 16, offset: int = 0) -> List[VectorEntityABS] | None:
        pass

    async def insert_one(self, data: VectorEntityABS) -> None:
        pass

    async def insert_many(self, data: List[VectorEntityABS]) -> None:
        pass

    async def get_all(self, chunk_size: int = 2 ** 16) -> Iterator[List[VectorEntityABS]]:
        pass

    async def get_all_slow(self) -> Iterator[VectorEntityABS]:
        pass
