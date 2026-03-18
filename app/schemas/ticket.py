from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional
from app.models.ticket import TicketStatus

class TicketBase(BaseModel):
    event_id: UUID
    owner_name: str
    owner_document: Optional[str] = None

class TicketCreate(TicketBase):
    pass

class TicketResponse(TicketBase):
    id: UUID
    status: TicketStatus
    qr_code_token: str
    
    model_config = ConfigDict(from_attributes=True)
