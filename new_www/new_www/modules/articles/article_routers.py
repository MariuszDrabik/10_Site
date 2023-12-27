import logging
from typing import Union
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.exc import IntegrityError
from core.log_conf import set_logger
from database.database import SessionLocal, get_db
from modules.articles.article_repository import get_articles, post_article
from modules.articles.article_schema import ArticleLists, ArticleSchema


set_logger()

log = logging.getLogger("__name__")

router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/", response_model=list[ArticleLists])
async def get_many(db: SessionLocal = Depends(get_db)):
    log.info("Log inform")
    log.debug("A to debug")
    articles = get_articles(db)
    return articles


@router.post("/", response_model=ArticleSchema)
async def made_article(
    article: ArticleSchema,
    response: Response,
    db: SessionLocal = Depends(get_db),
) -> ArticleSchema:
    log.info("Post article")

    user = post_article(db, article)

    response.status_code = status.HTTP_201_CREATED
    return user
