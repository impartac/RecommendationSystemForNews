from abc import ABC, abstractmethod
from core.entities.abstractions.vector_entity_abs import VectorEntityABS
from .custom_model_abs import CustomModelAbs
from typing import Iterable, List
from uuid import UUID


class RecommendationModelAbstraction(ABC):
    # model: CustomModelAbs
    # device: str

    @abstractmethod
    async def build(self, data: Iterable[VectorEntityABS]) -> None:
        pass

    @abstractmethod
    def train(self, additional_data: Iterable[VectorEntityABS]) -> None:
        pass

    @abstractmethod
    def predict(self, additional_data: VectorEntityABS) -> Iterable[str]:
        pass

    @abstractmethod
    def predict_batch(self, additional_data: Iterable[VectorEntityABS]) -> List[List[str]]:
        pass

    @abstractmethod
    def save(self, name: str):
        pass
