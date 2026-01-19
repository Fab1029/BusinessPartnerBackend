from pydantic import BaseModel, Field
from uuid import UUID
from Model.ContactInfo import ContactInfo
from Model.Coordinates import Coordinates
from Model.PlaceCategory import PlaceCategory

class PartnerProfile(BaseModel):
    id: UUID = Field(
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )
    name: str = Field(
        min_length=5,
        max_length=50,
        example="Hotel Mock"
    )
    category: PlaceCategory
    contact_info: ContactInfo
    location: Coordinates
    description: str = Field(
        min_length=5,
        max_length=200,
        example="Hotel ubicado en el centro histórico"
    )
