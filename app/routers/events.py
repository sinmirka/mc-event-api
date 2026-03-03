from fastapi import APIRouter
from app.schemas.event import EventRequest

router = APIRouter(
    prefix="/api/v1",
    tags=["events"]
)

@router.post("/event")
async def receive_event(payload: EventRequest):
    return {
        "status": "received",
        "username": payload.username
    }