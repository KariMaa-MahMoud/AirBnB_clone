#!/usr/bin/python3
"""
The User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User

    Attributes:
        email (str),password (str),first_name (str),last_name (str)

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
