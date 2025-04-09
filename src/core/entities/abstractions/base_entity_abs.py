import uuid
from uuid import UUID
from abc import ABC


class BaseEntity(ABC):
    id: str

    def __init__(self, id: str = str(uuid.uuid4())):
        self.id = id

    def __repr__(self):
        obj_dict = vars(self)
        return ''.join(obj_dict.items().__str__()) + '\n'
