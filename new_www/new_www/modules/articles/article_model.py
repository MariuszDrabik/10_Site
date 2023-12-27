import datetime
import uuid
from sqlalchemy import (
    JSON,
    UUID,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    String,
)
from sqlalchemy.orm import relationship
from database.database import Base

now = datetime.datetime.utcnow


class Article(Base):
    __tablename__ = "articles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255))
    slug = Column(String(255), unique=True)
    thumbnail = Column(String(255))
    abstract = Column(String(255))
    body = Column(JSON)
    author_id = Column(ForeignKey("users.id"))
    author = relationship("User", back_populates="articles")
    published = Column(Boolean, default=False)
    date_created = Column(DateTime, default=now)
    date_modified = Column(DateTime, default=now, onupdate=now)

    def show(self):
        print("User:", self.title, self.date_created)
