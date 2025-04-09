from typing import List, Optional
from uuid import UUID

from .base_entity_abs import BaseEntity


class RecommendationEntityABS(BaseEntity):
    id: str
    recommendations: List[str]

    def __init__(self, id: str, recommendations: List[str]):
        super().__init__()
        self.id = str(id)
        self.recommendations = recommendations
