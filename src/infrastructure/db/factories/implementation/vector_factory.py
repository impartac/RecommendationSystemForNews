from typing import Optional

from core.entities.implementation.domain_vector import DomainVector
from .factory import Factory
from core.factories.abstractions.vector_factory_abs import VectorFactoryABS
from ...models.vector_orm import VectorORM


class VectorFactory(VectorFactoryABS, Factory):
    def to_entity(self, instance: Optional[VectorORM]) -> Optional[DomainVector]:
        return DomainVector(
            id=instance.id,
            data=instance.data.copy()
        ) if instance else None

    def to_orm(self, instance: Optional[DomainVector]) -> Optional[VectorORM]:
        return VectorORM(
            id=instance.id,
            data=instance.data.copy()
        ) if instance else None
