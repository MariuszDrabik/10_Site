import logging
from fastapi import APIRouter, Depends
from core.log_conf import set_logger
from database.database import SessionLocal, get_db
from modules.users.user_model import User
from modules.users.user_repository import create_admin

router = APIRouter(tags=["user_admin"])

set_logger()
log = logging.getLogger("__name__")


@router.get("/admin")
def admin_created(
    db: SessionLocal = Depends(get_db),
):
    user = db.query(User).first()
    if not user:
        admin = create_admin(db=db)
        log.info("Admin crated %s", admin.login)
        return {
            "admin": "created",
        }

    log.info("Admin already created")

    return {
        "admin": "created",
    }
