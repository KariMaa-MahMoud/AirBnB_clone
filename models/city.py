#!/usr/bin/python3

"""defines one class, City(),
which sub-classes the BaseModel() parent class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A city in the application.

    Attributes:
        name(str)
        state_id(str)
    """

    name = ""
    state_id = ""
