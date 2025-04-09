from sqlalchemy.orm import relationship

from sqlalchemy import Column, String, Text, TIMESTAMP
from config.config import Settings
from .base_orm import BaseORM
from sqlalchemy import UUID as SQLAlchemyUUID

class NewsORM(BaseORM):
    __tablename__ = 'news'
    #
    # id = Column(
    #     Text,
    #     primary_key=True,
    #     default=SQLAlchemyUUID(),
    #     nullable=False
    # )
    title = Column(Text, nullable=False)
    anons = Column(Text, nullable=False)
    body = Column(Text, nullable=False)
    date_creation = Column(TIMESTAMP(timezone=False), nullable=False)

    # vector = relationship(
    #     "VectorORM",
    #     back_populates="news",
    #     uselist=False,
    #     cascade="all, delete-orphan"
    # )


    def __repr__(self):
        return f"<News(id='{self.id}', title='{self.title}')>"