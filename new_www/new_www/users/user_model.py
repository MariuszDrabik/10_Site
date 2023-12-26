import uuid
from sqlalchemy import (
    UUID,
    Column,
    String,
)
from database.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    login = Column(String, unique=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def show(self):
        print("User:", self.name)
