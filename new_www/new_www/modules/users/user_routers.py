import logging
from typing import Union
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.exc import IntegrityError
from core.log_conf import set_logger
from database.database import SessionLocal, get_db
from modules.users.user_repository import (
    create_user,
    delate_user,
    get_user,
    get_users,
    update_user,
)
from modules.users.user_schema import UserDisplay, UserSchema


set_logger()

log = logging.getLogger("__name__")

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserDisplay])
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
    try:
        user = create_user(db, user)
    except IntegrityError as e:
        log.error("User exist, {%s}", e)
        raise HTTPException(status_code=409, detail="User exist") from e

    response.status_code = status.HTTP_201_CREATED
    return user


@router.get("/{user_id}", response_model=UserDisplay)
async def get_one_user(user_id: UUID, db: SessionLocal = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        log.info("User with this id: {%s} not found", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    log.info("Get user {%s}", user.name)
    return user


@router.patch("/{user_id}", response_model=UserDisplay)
async def update_one_user(
    user_id: UUID, user: UserSchema, db: SessionLocal = Depends(get_db)
):
    user = update_user(db, user_id, user)
    log.info("User {%s} updated", user.name)
    return user


@router.delete("/{user_id}", response_model=UserDisplay)
async def del_user(user_id: UUID, db: SessionLocal = Depends(get_db)):
    user = delate_user(db, user_id)
    log.info("User {%s} updated", user.name)
    return user
