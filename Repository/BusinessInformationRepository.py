import json
from pathlib import Path
from uuid import UUID
from typing import List
from Model.Event import Event
from datetime import date
from Model.PartnerProfile import PartnerProfile
from Model.EventsRequest import EventsRequest
from Utils.time import get_date_from_string

class BusinessInformationRepository:

    def __init__(self):
        self.db_partners = "database/partner_information.json"
        self.db_events = "database/partner_events.json"

    def get_partner_information(self, partner_id: UUID):
        with open(self.db_partners, "r", encoding="utf-8") as file:
            partners = json.load(file)

        for partner in partners:
            if partner["id"] == str(partner_id):
                return PartnerProfile(**partner)

        return None

    def get_partner_events(self, events_request: EventsRequest):
        with open(self.db_events, "r", encoding="utf-8") as file:
            data = json.load(file)

        for entry in data:
            if entry["partnerId"] == str(events_request.partner_id):
                return [
                    Event(**event)
                    for event in entry["events"]
                    if events_request.date_start <= get_date_from_string(event["date"]) <= events_request.date_end
                ]

        return []
