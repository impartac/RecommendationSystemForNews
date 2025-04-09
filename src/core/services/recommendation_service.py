from typing import Iterator

from ..repositories.abstractions.recommendations_repository_abs import RecommendationsRepositoryABS
from ..entities.abstractions.recommender_model_abs import RecommendationModelAbstraction
from core.entities.abstractions.recommendation_entity_abs import RecommendationEntityABS
from core.entities.abstractions.vector_entity_abs import VectorEntityABS


class RecommendationService:
    def __init__(self, recommendation_repository: RecommendationsRepositoryABS,
                 recommender_model_abs: RecommendationModelAbstraction
                 ):
        self.recommendation_repository = recommendation_repository
        self.recommender_model = recommender_model_abs

    async def train_model(self, data: Iterator[VectorEntityABS], name: str = "knn"):
        await self.recommender_model.build(data)
        self.recommender_model.save(name)

    async def insert_one(self, data: RecommendationEntityABS):
        await self.recommendation_repository.insert_one(data)
