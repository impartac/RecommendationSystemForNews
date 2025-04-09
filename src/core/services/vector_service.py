from typing import Iterable, List

from ..entities.abstractions.vector_entity_abs import VectorEntityABS
from ..repositories.abstractions.vector_repository_abs import VectorRepositoryABS
from ..entities.abstractions.vectorizer_model_abs import VectorizerModelABS
from ..entities.abstractions.news_entity_abs import NewsEntityABS


class VectorService:
    def __init__(self, vector_repository: VectorRepositoryABS,
                 vectorizer_model: VectorizerModelABS):
        self._vector_repository = vector_repository
        self._vectorizer_model = vectorizer_model

    async def vectorize(self, news: NewsEntityABS) -> None:
        vector = await self._vectorizer_model.vectorize(news)
        await self._vector_repository.insert_one(vector)

    async def vectorize_batch(self, news: Iterable[NewsEntityABS]) -> None:
        vectors = await self._vectorizer_model.vectorize_batch(news)
        await self._vector_repository.insert_many(list(vectors))

    async def get_one(self, id: str) -> VectorEntityABS:
        return await self._vector_repository.get_one(id)

    async def get_any(self, ids: List[str]) -> List[VectorEntityABS]:
        return await self._vector_repository.get_any(ids)
