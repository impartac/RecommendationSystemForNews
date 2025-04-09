from typing import List, Optional
from abc import ABC
from .base_entity_abs import BaseEntity


class VectorEntityABS(BaseEntity, ABC):
    data: List[float]

    def __init__(self, data: List[float], id: Optional[str]):
        super().__init__(id)
        self.data = data
