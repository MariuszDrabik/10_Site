import logging
from typing import List, Union

from fastapi import APIRouter, Depends, Response, status
from core.log_conf import set_logger
from database.database import SessionLocal, get_db
from users.user_repository import create_user, get_users, has_user
from users.user_schema import UserDisplay, UserSchema


set_logger()

log = logging.getLogger("__name__")

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserDisplay])
async def get_many(db: SessionLocal = Depends(get_db)):
    log.info("Log inform")
    log.debug("A to debug")
    users = get_users(db)
    return users


@router.post("/", response_model=Union[UserDisplay, dict[str, str]])
async def made_user(
    user: UserSchema,
    response: Response,
    db: SessionLocal = Depends(get_db),
) -> UserDisplay:
    log.info("Post user %s, %s", user, UserSchema)
    log.debug("A to debug")
    if has_user(db, user.login, user.email):
        response.status_code = status.HTTP_409_CONFLICT
        return {
            "msg": (
                f"User with mail: {user.email}, and login: {user.login} exist"
            )
        }

    user = create_user(db, user)
    response.status_code = status.HTTP_201_CREATED
    return user
