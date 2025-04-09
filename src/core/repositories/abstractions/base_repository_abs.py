from abc import ABC, abstractmethod
from typing import List, Iterator
from ...entities.abstractions.base_entity_abs import BaseEntity


class BaseRepositoryABS(ABC):
    @abstractmethod
    async def get_one(self, id: str):
        pass

    @abstractmethod
    async def get_any(self, ids: List[str]) -> List[BaseEntity] | None:
        pass

    @abstractmethod
    async def get_batch(self, batch_size: int = 2 ** 16, offset: int = 0) -> List[BaseEntity] | None:
        pass

    @abstractmethod
    async def insert_one(self, data: BaseEntity) -> None:
        pass

    @abstractmethod
    async def insert_many(self, data: List[BaseEntity]) -> None:
        pass

    @abstractmethod
    async def get_all(self, chunk_size: int = 2 ** 16) -> Iterator[BaseEntity]:
        pass

