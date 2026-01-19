from enum import Enum

class PlaceCategory(str, Enum):
    CITY = "CITY"
    HOTEL = "HOTEL"
    ATTRACTION = "ATTRACTION"
    RESTAURANT = "RESTAURANT"
    ACTIVITY = "ACTIVITY"
