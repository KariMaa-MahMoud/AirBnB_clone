#!/usr/bin/python3
"""defines one class, Review() which sub-classes the BaseModel() class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A review of a place/house.

    It represents a review posted by the users
    of the application about a place/house.

    Attributes:
        text(str)
        user_id(str)
        place_id(str)
    """

    text = ""
    user_id = ""
    place_id = ""
