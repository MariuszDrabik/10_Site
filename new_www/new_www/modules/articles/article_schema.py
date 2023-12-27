import datetime
from typing import Optional
from pydantic import UUID4, BaseModel, field_serializer


class ShowUser(BaseModel):
    id: UUID4
    name: str


class ArticleSchema(BaseModel):
    id: Optional[UUID4] = None
    title: str
    slug: str
    thumbnail: str
    abstract: str
    body: dict
    author_id: UUID4 | None
    published: bool


class ArticleLists(BaseModel):
    id: Optional[UUID4] = None
    title: str
    slug: str
    author: ShowUser


class ArticleUserLists(BaseModel):
    id: Optional[UUID4] = None
    title: str
    slug: str
    date_created: datetime.datetime

    @field_serializer("date_created")
    def serialize_dt(self, date_created: datetime, _info):
        return date_created.strftime("%d-%m-%Y")
