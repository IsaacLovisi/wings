import uuid
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(255), nullable=False, index=True)
    date_time = Column(DateTime(timezone=True), nullable=False)
    location = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
