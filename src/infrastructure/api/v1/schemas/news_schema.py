from pydantic import BaseModel
from datetime import datetime


class NewsBase(BaseModel):
    anons: str
    title: str
    body: str


class NewsCreate(NewsBase):
    pass


class NewsResponse(NewsBase):
    id: str
    date_creation: datetime

    class Config:
        from_attributes = True
