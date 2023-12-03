from typing import Optional
from pydantic import UUID4, BaseModel, EmailStr, constr


class UserSchema(BaseModel):
    id: Optional[UUID4] = None
    login: str
    name: str
    email: EmailStr
    password: constr(min_length=8, max_length=21)


class UserDisplay(BaseModel):
    name: str
