from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.schemas.ticket import TicketCreate, TicketResponse
from app.services import ticket_service

router = APIRouter()

@router.post("/", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
def emit_ticket(ticket_in: TicketCreate, db: Session = Depends(get_db)):
    return ticket_service.create_ticket(db=db, ticket_in=ticket_in)

@router.post("/validate/{token}", response_model=TicketResponse)
def validate_ticket(token: str, db: Session = Depends(get_db)):
    try:
        ticket = ticket_service.validate_ticket(db=db, token=token)
        if not ticket:
            raise HTTPException(status_code=404, detail="Ingresso não encontrado")
        return ticket
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
