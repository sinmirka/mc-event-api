from pydantic import BaseModel
from pydantic import Field

class EventRequest(BaseModel):
    username: str = Field(min_length=1)
    mod_id: str = Field(min_length=1)
    timestamp: int
    signature: str = Field(min_length=1)