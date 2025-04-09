from abc import ABC
from typing import AsyncIterator, List

from .base_repository_abs import BaseRepositoryABS
from ...entities.abstractions.recommendation_entity_abs import RecommendationEntityABS


class RecommendationsRepositoryABS(BaseRepositoryABS, ABC):
    async def get_one(self, id: str):
        pass

    async def get_any(self, ids: List[str]) -> List[RecommendationEntityABS] | None:
        pass

    async def get_batch(self, batch_size: int = 2 ** 16, offset: int = 0) -> List[RecommendationEntityABS] | None:
        pass

    async def insert_one(self, data: RecommendationEntityABS) -> None:
        pass

    async def insert_many(self, data: List[RecommendationEntityABS]) -> None:
        pass

    async def get_all(self, chunk_size: int = 2 ** 16) -> AsyncIterator[RecommendationEntityABS]:
        pass
