from typing import Optional
from pydantic import UUID4, BaseModel, EmailStr, constr
from modules.articles.article_schema import ArticleUserLists


class UserSchema(BaseModel):
    id: Optional[UUID4] = None
    login: str
    name: str
    email: EmailStr
    bio: Optional[str] = None
    password: constr(min_length=8, max_length=21)


class UserDisplay(BaseModel):
    id: UUID4
    login: str
    name: str
    email: str
    bio: str | None
    articles: list[ArticleUserLists] | None
