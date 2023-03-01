from fastapi import FastAPI
from routers import blog_get
from routers import blog_post
from db import models
from db.database import engine

blogAPI = FastAPI()
blogAPI.include_router(blog_get.router)
blogAPI.include_router(blog_post.router)


@blogAPI.get("/hello")
async def root():
    return {"message": "Hello World"}


models.Base.metadata.create_all(engine)
