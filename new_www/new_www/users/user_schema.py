from datetime import datetime
from typing import Generic, Optional, TypeVar, Union
from pydantic import UUID4, BaseModel, Field
from pydantic.generics import GenericModel


class UserSchema(BaseModel):
    id: Optional[UUID4] = None
    login: str
    name: str
    email: str
    password: str


class UserDisplay(BaseModel):
    name: str
