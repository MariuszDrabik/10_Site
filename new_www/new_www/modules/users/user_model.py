import uuid
from sqlalchemy import (
    UUID,
    Column,
    String,
)
from sqlalchemy.orm import relationship
from database.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    login = Column(String(16), unique=True)
    name = Column(String(32))
    email = Column(String, unique=True)
    bio = Column(String(1000))
    password = Column(String(32))
    articles = relationship("Article", back_populates="author")

    def show(self):
        print("User:", self.name)
