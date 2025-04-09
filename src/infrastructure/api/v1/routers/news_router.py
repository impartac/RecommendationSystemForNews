import http

from fastapi import APIRouter, Depends
from fastapi.params import Query

from infrastructure.db.factories.implementation.news_factory import NewsFactory
from ..schemas.news_schema import NewsResponse, NewsCreate
from ..schemas.recommendation_schema import RecommendationResponse
from core.use_cases.news_use_case import NewsUseCase
from ...dependencies import get_news_use_case
from src.config.logger_config import logger

router = APIRouter(prefix='/api/v1')


@router.post("/news")
async def create_news(
        news_data: NewsCreate,
        use_case: NewsUseCase = Depends(get_news_use_case),
) -> NewsResponse:
    news_factory = NewsFactory()
    entity = await use_case.create_news(news_data.anons, news_data.title, news_data.body)
    await use_case.vectorize(entity)
    orm = news_factory.to_orm(entity)
    news_response = NewsResponse.from_orm(orm)
    return news_response


@router.post("/init_vectors")
async def init_vectors(
        use_case: NewsUseCase = Depends(get_news_use_case)
):
    await use_case.vectorize_all()
    return http.HTTPStatus(200)


@router.post("/init_model")
async def init_model(
        use_case: NewsUseCase = Depends(get_news_use_case)
):
    data = use_case._vector_service._vector_repository.get_all()
    async for i in data:
        use_case._recommendation_service.recommender_model.train(i)
    use_case._recommendation_service.recommender_model.save("knn2")
    return http.HTTPStatus(200)


@router.post("/init_recs")
async def init_recs(
        use_case: NewsUseCase = Depends(get_news_use_case)
):
    data = use_case._news_repository.get_all(2**14)
    offset = 0
    async for news in data:
        logger.info(f"Init recs offset: {offset}")
        offset += 2**14
        recs = await use_case.get_recommendations(news)
        # logger.info(f"Get recs for id={news.id}: {recs.recommendations}")
        await use_case.insert_recommendations(recs)
    return http.HTTPStatus(200)


@router.get("/news", response_model=RecommendationResponse)
async def get_news(
        id: str = Query(),
        use_case: NewsUseCase = Depends(get_news_use_case)
) -> NewsResponse:
    news = await use_case.get_news(id)
    recs = await use_case.get_recommendation(news)
    return RecommendationResponse.from_orm({
        "news": news,
        "recommendations": [
            await use_case.get_news(i) for i in recs.recommendations
        ]
    })


@router.get("/")
async def health_check():
    return {"status": "ok", "code": 200}
