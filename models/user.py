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

    user_email = ""
    user_password = ""
    user_first_name = ""
    user_last_name = ""
