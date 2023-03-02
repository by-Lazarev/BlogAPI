from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class User(BaseModel):
    user_id: int
    username: str

    class Config:
        orm_mode = True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        orm_mode = True


class UserDisplay(BaseModel):
    username: str
    email: str
    articles: list[Article] = []

    class Config:
        orm_mode = True
