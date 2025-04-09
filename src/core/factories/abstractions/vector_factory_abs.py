from typing import Optional, Any

from core.entities.abstractions.vector_entity_abs import VectorEntityABS
from .base_factory_abs import BaseFactoryABS


class VectorFactoryABS(BaseFactoryABS):
    def to_entity(self, instance: Optional[Any]) -> Optional[VectorEntityABS]:
        pass

    def to_orm(self, instance: Optional[VectorEntityABS]) -> Optional[Any]:
        pass
