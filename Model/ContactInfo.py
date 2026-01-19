from pydantic import BaseModel, Field

class ContactInfo(BaseModel):
    phone: str = Field(
        min_length=5,
        max_length=15,
        example="+593987654321"
    )
    email: str = Field(
        example= "example@gmail.com"
    )
    website: str = Field(
        example="https://www.business.com"
    )
