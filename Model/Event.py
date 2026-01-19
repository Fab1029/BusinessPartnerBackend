from uuid import UUID
from datetime import date as Date
from pydantic import BaseModel, Field

class Event(BaseModel):
    id: UUID = Field(
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )
    price: float = Field(
        ge=0.0,
        example=34.67
    )
    date: Date = Field(
        example="2026-01-12"
    )
    description: str = Field(
        min_length=10,
        max_length=200,
        example="Evento cultural realizado en el centro histórico de la ciudad"
    )
