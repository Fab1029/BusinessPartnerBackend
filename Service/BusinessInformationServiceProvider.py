from uuid import UUID
from fastapi import HTTPException, status
from Model.EventsRequest import EventsRequest
from Repository.BusinessInformationRepositoryProvider import BusinessInformationRepositoryProvider


class BusinessInformationService:

    def __init__(self):
        self.repo = BusinessInformationRepository()

    def get_partner_information(self, partner_id: UUID):
        partner = self.repo.get_partner_information(partner_id)

        if not partner:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Business partner not found"
            )

        return partner

    def get_partner_events(self, events_request: EventsRequest):
      
        # Validación de rango de fechas
        if events_request.date_end < events_request.date_start:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Date range incorrect"
            )

        # Validar existencia del partner
        partner_exists = self.repo.get_partner_information(events_request.partner_id)

        events = self.repo.get_partner_events(events_request)

        if not events:
            raise HTTPException(
                status_code=status.HTTP_204_NO_CONTENT,
                detail="No events found for this partner"
            )

        return events
