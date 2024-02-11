#!/usr/bin/python3

"""defines one class, Place() which sub-classes the BaseModel() class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A place/house in the application.

    Attributes:
        name(str)
        user_id(str)
        city_id(str)
        description(str)
        number_bathrooms(int)
        price_by_night(int)
        number_rooms(int)
        longitude
        latitude
        max_guest(int)
        amenity_ids(list)
    """

    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    max_guest = 0
    amenity_ids = []
    longitude = 0.0
    latitude = 0.0
