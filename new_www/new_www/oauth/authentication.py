from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database.database import SessionLocal, get_db
from modules.users.user_model import User
from utils.hashing import Hash
from oauth import oauth2

router = APIRouter(tags=["authentication"])


@router.post("/token")
def authentication(
    request: OAuth2PasswordRequestForm = Depends(),
    db: SessionLocal = Depends(get_db),
):
    user = db.query(User).filter(User.login == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not Hash.check_password(user.password, request.password):
        raise HTTPException(status_code=401, detail="Password is wrong")

    access_token = oauth2.create_access_token(data={"sub": user.login})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.login,
    }
