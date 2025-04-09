from typing import Optional, Any

from core.entities.abstractions.recommendation_entity_abs import RecommendationEntityABS
from .base_factory_abs import BaseFactoryABS


class RecommendationFactoryABS(BaseFactoryABS):
    def to_entity(self, instance: Optional[Any]) -> Optional[RecommendationEntityABS]:
        pass

    def to_orm(self, instance: Optional[RecommendationEntityABS]) -> Optional[Any]:
        pass
