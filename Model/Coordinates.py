from pydantic import BaseModel, Field

class Coordinates(BaseModel):
    latitude: float = Field(
        ge=-90,
        le=90,
        example=-0.180653
    )
    longitude: float = Field(
        ge=-180,
        le=180,
        example=-78.467834
    )
