from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import blog_get, blog_post, article, user
from auth import authentication

from db import models
from db.database import engine

blogAPI = FastAPI()
blogAPI.include_router(authentication.router)
blogAPI.include_router(blog_get.router)
blogAPI.include_router(blog_post.router)
blogAPI.include_router(user.router)
blogAPI.include_router(article.router)


@blogAPI.get("/hello")
async def root():
    return {"message": "Hello World"}


origins = [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:3000'
]
models.Base.metadata.create_all(engine)
blogAPI.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)