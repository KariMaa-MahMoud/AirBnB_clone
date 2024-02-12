#!/usr/bin/python3
"""
This file_storage is for serializes and deserializes JSON types
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    class for file storage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        initiation phaseof the class
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the object with the key
        <obj class name>.id

        Args:
            object(obj)

        """
        self.__objects[obj.__class__.__name__ + "." + str(obj)] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        with open(self.__file_path, "w+") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        try:
            with open(self.__file_path, "r") as f:
                data = json.loads(f.read())
                for value in data.values():
                    cls = value["__class__"]
                self.new(eval(cls)(**value))
        except Exception:
            pass
