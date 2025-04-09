from sqlalchemy import Column, UUID, ARRAY, ForeignKey, TIMESTAMP, Text
from config.config import Settings
from .base_orm import BaseORM


class RecommendationORM(BaseORM):
    __tablename__ = 'news_recommendation'

    id = Column(
        Text,
        ForeignKey(f'news.id', ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    )

    recommendations = Column(
        ARRAY(Text),
        nullable=False
    )

    updated_at = Column(
        TIMESTAMP(timezone=False),
        nullable=False
    )

    def __repr__(self):
        return f"<NewsRecommendations(id='{self.id}', updated_at='{self.updated_at}, recommendations='{self.recommendations}')>"
