from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.websockets import WebSocket

from routers import blog_get, blog_post, article, user, file
from auth import authentication
from client import html

from db import models
from db.database import engine

blogAPI = FastAPI()
blogAPI.include_router(authentication.router)
blogAPI.include_router(blog_get.router)
blogAPI.include_router(blog_post.router)
blogAPI.include_router(user.router)
blogAPI.include_router(article.router)
blogAPI.include_router(file.router)

models.Base.metadata.create_all(engine)
clients = []


@blogAPI.get("/hello")
async def root():
    return {"message": "Hello World"}


@blogAPI.get("/")
async def get():
    return HTMLResponse(html)


@blogAPI.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)


@blogAPI.middleware("http")
async def add_middleware(request: Request, call_next):
    response = await call_next(request)
    return response


origins = [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:3000'
]

blogAPI.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

blogAPI.mount("/files", StaticFiles(directory="files"), name="files")
