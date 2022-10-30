#!/usr/bin/python3

"""
    Defines a class FileStorage.
"""

import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent a FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all the objects saved in the file"""

        return self.__objects

    def new(self, obj):
        """Add new objects in a dictionary"""
        objId = obj.__class__.__name__ + '.' + obj.id
        self.__objects[objId] = obj

    def save(self):
        """Save object representation of JSON to a file"""

        with open(self.__file_path, mode='w', encoding='UTF-8') as myfile:
            to_json = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(to_json, myfile)

    def reload(self):
        """Function that creates an Object from a JSON file"""

        from_json = {}
        try:
            with open(self.__file_path, mode='r', encoding="UTF-8") as myfile:
                from_json = json.load(myfile)
                for key, value in from_json.items():
                    attr_cls_name = value.pop("__class__")
                    self.new(eval(attr_cls_name)(**value))
        except:
            pass
