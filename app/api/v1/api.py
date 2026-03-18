from fastapi import APIRouter
from app.api.v1.routers import events, tickets

api_router = APIRouter()
api_router.include_router(events.router, prefix="/events", tags=["events"])
api_router.include_router(tickets.router, prefix="/tickets", tags=["tickets"])
