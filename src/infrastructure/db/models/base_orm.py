from sqlalchemy import Column, Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.types import UUID as SQLAlchemyUUID
from sqlalchemy import MetaData
metadata = MetaData()


class BaseORM(DeclarativeBase):
    metadata = MetaData()
    __table_args__ = {'info': {'is_async': True}}

    id = Column(
        Text,
        primary_key=True,
        default=SQLAlchemyUUID(),
        nullable=False
    )
