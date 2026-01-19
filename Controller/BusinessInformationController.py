from uuid import UUID
from typing import List
from fastapi import APIRouter

from Model.Event import Event
from Model.EventsRequest import EventsRequest
from Model.PartnerProfile import PartnerProfile
from Service.BusinessInformationService import BusinessInformationService

router = APIRouter(
    prefix="/v1/business",
    tags=["Business Information Provider"]
)

service = BusinessInformationService()

@router.get(
    "/information/{partner_id}",
    name="Get Partner Information",
    description="Obtiene la información del socio de negocio",
    response_model=PartnerProfile,
    status_code=200
)
async def get_partner_information(partner_id: UUID):
    return service.get_partner_information(partner_id)


@router.get(
    "/events",
    name="Get Partner Events",
    description="Obtiene los eventos asociados a un socio de negocio",
    response_model=List[Event],
    status_code= 200
)
async def get_partner_events(events_request: EventsRequest):
    return service.get_partner_events(events_request)
