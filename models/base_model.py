#!/usr/bin/python3
"""
BaseModel class for the entire project (parent)

"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel for all the classes in the AirBnb console project

    Arttributes:
        unique_id: handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, unique_id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """

    def __init__(self, *args, **kwargs):
        """initialization artribute
        after creation the class

        Args:
            *args(args): arguments
            **kwargs(dict): more than one attribute values

        """
        Date_Time_Format = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.unique_id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value, Date_Time_Format)
                elif key[0] == "unique_id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Returns string representation of the class
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.unique_id, self.__dict__
        )

    def save(self):
        """
        Updates the attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Method returns a dictionary containing all
        keys/values of __dict__ instance
        """
        object_mapped = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                object_mapped[key] = value.isoformat()
            else:
                object_mapped[key] = value
        object_mapped["__class__"] = self.__class__.__name__
        return object_mapped
