from fastapi import APIRouter, Request
from datetime import datetime

from slowapi import Limiter
from slowapi.util import get_remote_address

from app.schemas.event import EventRequest
from app.core.security import verify_timestamp, verify_signature
from app.services.discord import send_discord_event
from app.services.storage import save_event

router = APIRouter(
    prefix="/api/v1",
    tags=["events"]
)

limiter = Limiter(key_func=get_remote_address)

def normalize_time(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    time =dt.strftime("%Y-%m-%d %H:%M:%S")
    return time

@router.post("/event")
@limiter.limit("10/minute")
async def receive_event(request: Request, payload: EventRequest):

    verify_timestamp(payload.timestamp)

    verify_signature(
        payload.username,
        payload.mod_id,
        payload.timestamp,
        payload.signature,
    )

    await send_discord_event(
        username=payload.username,
        mod_id=payload.mod_id,
        timestamp=normalize_time(payload.timestamp)
    )

    save_event(
        username=payload.username,
        mod_id=payload.mod_id,
        timestamp=normalize_time(payload.timestamp)
    )

    return {
        "status": "received"
    }