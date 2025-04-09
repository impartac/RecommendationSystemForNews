from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.params import Query

from ..schemas.news_schema import NewsResponse, NewsCreate
from core.use_cases.news_use_case import NewsUseCase
from ...dependencies import get_news_use_case
from ..common import templates

router = APIRouter()


@router.get("/news", response_class=HTMLResponse)
async def get_news(
        request: Request,
        id: str = Query(),
        use_case: NewsUseCase = Depends(get_news_use_case)
) -> NewsResponse:
    news = await use_case.get_news(id)
    recommendations = await use_case.get_recommendations(id)
    return templates.TemplateResponse(
        "news_page.html",
        {"news": news,
         "request": request,
         "recommendations": recommendations},
    )
