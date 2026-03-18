import uuid
from sqlalchemy import Column, String, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum
from app.models.base import Base

class TicketStatus(str, enum.Enum):
    PENDING = "pending"
    EMITTED = "emitted"
    VALIDATED = "validated"
    CANCELLED = "cancelled"

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"), nullable=False)
    owner_name = Column(String(255), nullable=False)
    owner_document = Column(String(50), nullable=True)
    status = Column(Enum(TicketStatus), default=TicketStatus.EMITTED, nullable=False)
    qr_code_token = Column(String(255), unique=True, index=True, default=lambda: str(uuid.uuid4()))

    event = relationship("Event", backref="tickets")
