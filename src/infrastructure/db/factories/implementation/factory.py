from typing import Optional

from core.entities.abstractions.base_entity_abs import BaseEntity
from core.factories.abstractions.base_factory_abs import BaseFactoryABS
from ...models.base_orm import BaseORM


class Factory(BaseFactoryABS):

    def to_entity(self, instance: Optional[BaseORM]) -> Optional[BaseEntity]:
        pass

    def to_orm(self, instance: Optional[BaseEntity]) -> Optional[BaseORM]:
        pass
