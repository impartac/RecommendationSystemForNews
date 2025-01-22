from fastapi import APIRouter, HTTPException
from fastapi.requests import Request

from src.app.services.managers import news_manager, recommendations_manager
from src.app.v1.common import templates
from src.config.logger_config import logger

router = APIRouter(prefix="/v1")


@router.get("/")
async def index(
        request: Request,
):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@router.get("/news/")
async def index(
        request: Request,
        id: str
):
    try:
        article = news_manager.get_one(id)
        if article is None:
            raise HTTPException(404)
        recommendation_ids = recommendations_manager.get_recommendations(id)
        if len(recommendation_ids) == 0:
            recommendation_ids = []
        recommendations = news_manager.get_any(recommendation_ids)
        context = {
            "request": request,
            "title": article.title,
            "body": article.body,
            "recommendations": [{"id": i.id, "title": i.title, "anons": i.anons} for i in recommendations]}
        return templates.TemplateResponse(
            "news_page.html",
            context
        )
    except Exception as e:
        logger.error(e)
        return templates.TemplateResponse(
            request=request,
            name="404.html",
        )



# [
# {
#     "id": 0,
#     "title": recommendations[0].title,
#     "anons": recommendations[0].anons
# },
# {
#     "id": 1,
#     "title": recommendations[1].title,
#     "anons": recommendations[1].anons
# },
# {
#     "id": 2,
#     "title": recommendations[2].title,
#     "anons": recommendations[2].anons
# },
# {
#     "id": 3,
#     "title": recommendations[3].title,
#     "anons": recommendations[3].anons
# },
# {
#     "id": 4,
#     "title": recommendations[4].title,
#     "anons": recommendations[4].anons
# }
# ]

# ░░░░░░░░░░░░░░░░░░░░
# ░░░░░ЗАПУСКАЕМ░░░░░░░
# ░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░
# ▄███▀░◐░░░▌░░░░░░░░░
# ░░░░▌░░░░░▐░░░░░░░░░
# ░░░░▐░░░░░▐░░░░░░░░░
# ░░░░▌░░░░░▐▄▄░░░░░░░
# ░░░░▌░░░░▄▀▒▒▀▀▀▀▄
# ░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
# ░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
# ░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
# ░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
# ░░░░░░░░░░░▌▌░▌▌░░░░░
# ░░░░░░░░░░░▌▌░▌▌░░░░░
# ░░░░░░░░░▄▄▌▌▄▌▌░░░░░
