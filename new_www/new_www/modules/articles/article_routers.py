import logging
from uuid import UUID
from oauth.oauth2 import get_current_user
from fastapi import APIRouter, Depends, Request, Response, status
from core.log_conf import set_logger
from database.database import SessionLocal, get_db
from modules.users.user_schema import UserDisplay
from modules.articles.article_repository import (
    delate_article,
    get_article,
    get_articles,
    post_article,
    update_article,
)
from modules.articles.article_schema import (
    ArticleDisplay,
    ArticleLists,
    ArticlePatch,
    ArticleSchema,
)


set_logger()

log = logging.getLogger("__name__")

router = APIRouter(
    prefix="/articles", tags=["articles"]
)  # dependencies=[Depends(set_logger)]


@router.get("/", response_model=list[ArticleLists])
async def get_many_articles(db: SessionLocal = Depends(get_db)):
    log.info("Log inform")
    articles = get_articles(db)
    return articles


@router.get(
    "/{article_slug}",
    response_model=ArticleSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_one_article(
    article_slug: str,
    db: SessionLocal = Depends(get_db),
):
    article = get_article(db, article_slug)
    log.info("Get article {%s}", article.title)
    return article


@router.post("/", response_model=ArticleDisplay)
async def made_article(
    article: ArticleSchema,
    response: Response,
    db: SessionLocal = Depends(get_db),
    current_user: UserDisplay = Depends(get_current_user),
) -> ArticleDisplay:
    log.info("Post article")

    article = post_article(db, article)

    response.status_code = status.HTTP_201_CREATED
    return article


@router.patch("/{article_id}", response_model=ArticleSchema)
async def update_one_user(
    article_id: UUID,
    article: ArticlePatch,
    db: SessionLocal = Depends(get_db),
):
    article = update_article(db, article_id, article)
    log.info("User {%s} updated", article.title)
    return article


@router.delete(
    "/{article_id}",
    response_model=ArticleSchema,
    dependencies=[Depends(get_current_user)],
)
async def del_article(article_id: UUID, db: SessionLocal = Depends(get_db)):
    article = delate_article(db, article_id)
    log.info("User {%s} updated", article.title)
    return article
