import time
import hmac
import hashlib
from fastapi import HTTPException

from app.core.config import SECRET_KEY

MAX_TIME_DIFF = 60

def verify_timestamp(timestamp: int):
    current_time = int(time.time())
    time_difference = abs(current_time - timestamp)
    if time_difference > MAX_TIME_DIFF:
        raise HTTPException(
            status_code=400,
            detail="Request expired"
        )
    
def verify_signature(username: str, mod_id: str, timestamp: int, signature: str):
    # checking HMAC
    message = f"{username}{mod_id}{timestamp}"

    calculated_signature = hmac.new(
        SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(calculated_signature, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")