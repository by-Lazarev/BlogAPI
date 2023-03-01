from fastapi import APIRouter, Path

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


@router.get("/all")
def get_all_blogs():
    return {"status": 200,
            "content": "All blogs"}


@router.get("/{blog_id}")
def get_blog(blog_id: int = Path(None, gt=0)):
    return {"status": 200,
            "content": "Blog given",
            "blog_id": blog_id}
