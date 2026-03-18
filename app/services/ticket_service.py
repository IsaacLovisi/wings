from sqlalchemy.orm import Session
from app.models.ticket import Ticket, TicketStatus
from app.schemas.ticket import TicketCreate
import uuid

def create_ticket(db: Session, ticket_in: TicketCreate) -> Ticket:
    db_ticket = Ticket(
        event_id=ticket_in.event_id,
        owner_name=ticket_in.owner_name,
        owner_document=ticket_in.owner_document,
        status=TicketStatus.EMITTED,
        qr_code_token=str(uuid.uuid4())
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def validate_ticket(db: Session, token: str) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.qr_code_token == token).first()
    if not ticket:
        return None
    
    if ticket.status == TicketStatus.VALIDATED:
        raise ValueError("Ingresso já validado")
    
    if ticket.status == TicketStatus.CANCELLED:
        raise ValueError("Ingresso cancelado")

    ticket.status = TicketStatus.VALIDATED
    db.commit()
    db.refresh(ticket)
    return ticket
