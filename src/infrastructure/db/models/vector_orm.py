from sqlalchemy import Column, ARRAY, FLOAT, ForeignKey, Text

from .base_orm import BaseORM
from .news_orm import NewsORM


class VectorORM(BaseORM):
    __tablename__ = 'news_to_vector'
    # __schema__ = Settings.SCHEMA
    id = Column(
        Text,
        ForeignKey(NewsORM.id, ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    )
    data = Column(
        ARRAY(FLOAT),
        nullable=False
    )
    # news = relationship(
    #     "NewsORM",
    #     back_populates="vector"
    # )

    def __repr__(self):
        return f"<Vector(id='{self.id}', body='{self.body[:5]}...')>"
