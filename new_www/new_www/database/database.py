from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


POSTGRES_URL = (
    f"""postgresql+psycopg2://{settings.POSTGRES_USER}:"""
    f"""{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:"""
    f"""{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"""
)
# POSTGRES_URL = "postgresql://www:www@127.0.0.1:5432/www_db"


engine = create_engine(POSTGRES_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        # rollback or other operation.
        raise e
    finally:
        db.close()
