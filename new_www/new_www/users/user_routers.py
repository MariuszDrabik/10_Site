import logging
from typing import List

from fastapi import APIRouter, Depends
from core.log_conf import set_logger
from database.database import SessionLocal, get_db
from users.user_repository import create_user, get_users
from users.user_schema import UserDisplay, UserSchema


set_logger()

log = logging.getLogger("__name__")

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_many(db: SessionLocal = Depends(get_db)):
    log.info("Log informacjom")
    log.debug("A to debug")
    users = get_users(db)
    return users


@router.post("/", response_model=UserDisplay)
async def made_user(
    user: UserSchema, db: SessionLocal = Depends(get_db)
) -> UserDisplay:
    log.info(f"Post user {user} {UserSchema}")
    log.debug("A to debug")
    user = create_user(db, user)
    return user
