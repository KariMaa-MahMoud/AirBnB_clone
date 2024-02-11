#!/usr/bin/python3

""" defines one class, Amenity(),
which sub-class to the BaseModel() parent class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house.

    Attributes:
        name(str)
    """

    name = ""
