from pydantic import BaseModel, ConfigDict
from datetime import datetime
from uuid import UUID
from typing import Optional

class EventBase(BaseModel):
    name: str
    date_time: datetime
    location: str
    description: Optional[str] = None

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)
