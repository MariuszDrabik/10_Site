import logging
from uuid import UUID
from database.database import SessionLocal
from modules.articles.article_model import Article
from modules.articles.article_schema import ArticlePatch, ArticleSchema
from fastapi import HTTPException
from core.log_conf import set_logger

set_logger()
log = logging.getLogger("__name__")


def post_article(db: SessionLocal, article: ArticleSchema):
    article = Article(**article.model_dump())
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_articles(db: SessionLocal):
    articles = db.query(Article).all()
    return articles


def get_article(db: SessionLocal, article_slug: str):
    article = db.query(Article).filter(Article.slug == article_slug).first()
    if not article:
        log.warning("Article with this id: {%s} not found", article_slug)
        raise HTTPException(status_code=404, detail="Article not found")
    return article


def update_article(
    db: SessionLocal, article_id: UUID, article: ArticlePatch
) -> Article:
    article_update = db.query(Article).filter_by(id=article_id)
    if not article_update.first():
        log.info("Article with this id: {%s} not found", article_id)
        raise HTTPException(status_code=404, detail="Article not found")

    article_update.update(article.model_dump(exclude_unset=True))
    db.commit()
    return article_update.first()


def delate_article(db: SessionLocal, article_id: UUID) -> Article:
    article = db.query(Article).filter_by(id=article_id).first()
    if not article:
        log.info("Article with this id: {%s} not found", article_id)
        raise HTTPException(status_code=404, detail="Article not found")
    db.delete(article)
    db.commit()
    return article
