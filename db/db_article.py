from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle
from fastapi import HTTPException, status


def create_article(db: Session, request: ArticleBase):
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, article_id: int):
    article = db.query(DbArticle).filter(DbArticle.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"article with id {article_id} not found")
    return article
