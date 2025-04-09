from typing import List

from pydantic import BaseModel

from infrastructure.api.v1.schemas.news_schema import NewsResponse


class RecommendationResponse(BaseModel):
    news: NewsResponse
    recommendations: List[NewsResponse]

    class Config:
        from_attributes = True
