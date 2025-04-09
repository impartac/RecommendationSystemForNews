from typing import Optional

from .factory import Factory
from core.factories.abstractions.recommendation_factory_abs import RecommendationFactoryABS
from core.entities.implementation.domain_recommendation import DomainRecommendation
from ...models.recommendation_orm import RecommendationORM


class RecommendationFactory(Factory, RecommendationFactoryABS):
    def to_entity(self, instance: Optional[RecommendationORM]) -> Optional[DomainRecommendation]:
        return DomainRecommendation(
            id=instance.id,
            recommendations=instance.recommendations.copy()
        ) if instance else None

    def to_orm(self, instance: Optional[DomainRecommendation]) -> Optional[RecommendationORM]:
        return RecommendationORM(
            id=instance.id,
            recommendations=instance.recommendations.copy()
        ) if instance else None
