from uuid import UUID
from datetime import date
from pydantic import BaseModel, Field

class EventsRequest(BaseModel):
    partner_id: UUID = Field(
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )
    date_start: date = Field(
        example="2026-01-15"
    )
    date_end: date = Field(
        example="2026-01-20"
    )
