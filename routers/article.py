from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article

router = APIRouter(
    prefix="/article",
    tags=["article"]
)


# --[CRUD]--
# CREATE ARTICLE
@router.post("/", response_model=ArticleDisplay)
def post_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


# READ ARTICLE
@router.get("/{article_id}", response_model=ArticleDisplay)
def get_article(article_id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, article_id)

# UPDATE ARTICLE

# DELETE ARTICLE
