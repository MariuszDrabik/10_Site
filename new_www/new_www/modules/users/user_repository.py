import logging
from uuid import UUID
from fastapi import HTTPException
from core.log_conf import set_logger
from database.database import SessionLocal
from modules.users.user_model import User
from modules.users.user_schema import UserSchema
from utils.hashing import Hash
from sqlalchemy import or_


set_logger()
log = logging.getLogger("__name__")


def get_users(db: SessionLocal):
    users = db.query(User).all()

    return users


def get_user(db: SessionLocal, user_id: UUID):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        log.warning("User with this id: {%s} not found", user_id)
        raise HTTPException(status_code=404, detail="User not found")

    return user


def has_user(db: SessionLocal, login):
    user = db.query(User).filter(User.login == login).first()
    return user


def create_user(db: SessionLocal, user: UserSchema):
    user = User(
        name=user.name,
        email=user.email,
        login=user.login,
        password=Hash.hash_password(user.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: SessionLocal, user_id: UUID, user: UserSchema) -> User:
    user_update = db.query(User).filter_by(id=user_id)
    if not user_update.first():
        log.info("User with this id: {%s} not found", user_id)
        raise HTTPException(status_code=404, detail="User not found")

    if not Hash.check_password(
        user_update.first().password,
        user.password,
    ):
        raise HTTPException(status_code=401, detail="Old password is wrong")

    user_update.update(
        {
            User.name: user.name,
            User.email: user.email,
            User.login: user.login,
            User.password: Hash.hash_password(user.password),
        }
    )
    db.commit()
    return user_update.first()


def delate_user(db: SessionLocal, user_id: UUID) -> User:
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        log.info("User with this id: {%s} not found", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user
