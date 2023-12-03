from database.database import SessionLocal
from users.user_model import User
from users.user_schema import UserSchema
from utils.hashing import Hash


def get_users(db: SessionLocal):
    users = db.query(User).all()

    return users


def create_user(db: SessionLocal, user: UserSchema):
    print(user)
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
