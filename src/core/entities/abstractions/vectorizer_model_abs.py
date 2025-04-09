from abc import ABC, abstractmethod
from typing import Iterable

from .news_entity_abs import NewsEntityABS
from .vector_entity_abs import VectorEntityABS


class VectorizerModelABS(ABC):
    @abstractmethod
    async def vectorize(self, news: NewsEntityABS) -> VectorEntityABS:
        pass

    @abstractmethod
    async def vectorize_batch(self, news: Iterable[NewsEntityABS]) -> Iterable[VectorEntityABS]:
        pass
