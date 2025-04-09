import datetime
import uuid
from abc import ABC
from typing import Optional
from uuid import UUID

from .base_entity_abs import BaseEntity


class NewsEntityABS(BaseEntity, ABC):
    id: str
    title: str
    body: str
    anons: str
    date_creation: datetime.datetime

    def __init__(self, id: str, title: str, body: str, anons: str, date_creation: datetime.datetime):
        super().__init__()
        self.id = str(id)
        self.title = title
        self.body = body
        self.anons = anons
        self.date_creation = date_creation
