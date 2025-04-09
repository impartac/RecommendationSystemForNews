from abc import ABC, abstractmethod
from typing import Optional, Any

from core.entities.abstractions.news_entity_abs import NewsEntityABS
from .base_factory_abs import BaseFactoryABS


class NewsFactoryABS(BaseFactoryABS, ABC):
    @abstractmethod
    def to_entity(self, instance: Optional[Any]) -> Optional[NewsEntityABS]:
        pass

    @abstractmethod
    def to_orm(self, instance: Optional[NewsEntityABS]) -> Optional[Any]:
        pass
