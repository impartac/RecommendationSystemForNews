from abc import ABC, abstractmethod
from typing import Optional, Any

from core.entities.abstractions.base_entity_abs import BaseEntity


class BaseFactoryABS(ABC):
    @abstractmethod
    def to_entity(self, instance: Optional[Any]) -> Optional[BaseEntity]:
        pass

    @abstractmethod
    def to_orm(self, instance: Optional[BaseEntity]) -> Optional[Any]:
        pass
