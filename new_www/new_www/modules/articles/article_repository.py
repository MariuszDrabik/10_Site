import logging
from uuid import UUID
from database.database import SessionLocal
from modules.articles.article_model import Article
from modules.articles.article_schema import ArticleSchema
from fastapi import HTTPException
from core.log_conf import set_logger

set_logger()
log = logging.getLogger("__name__")


def post_article(db: SessionLocal, article: ArticleSchema):
    print(article)
    article = Article(**article.__dict__)
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_articles(db: SessionLocal):
    articles = db.query(Article).all()

    return articles


def get_article(db: SessionLocal, article_id: UUID):
    user = db.query(Article).filter(Article.id == article_id).first()
    if not user:
        log.warning("User with this id: {%s} not found", article_id)
        raise HTTPException(status_code=404, detail="User not found")

    return user
