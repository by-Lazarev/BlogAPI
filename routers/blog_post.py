from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: bool | None
    image: Image | None = None


@router.post("/new/{blog_id}")
def post_new_blog(blog: BlogModel, blog_id: int):
    return {"status": 200,
            "message": "Got the new blog to post",
            "Blog_id": blog_id,
            "data": blog}
