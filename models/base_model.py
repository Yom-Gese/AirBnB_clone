#!/usr/bin/python3
"""
The Base Model module
Defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    The "BaseModel" class
    Defines all common attributes/methods for other model classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel object"""

        if len(kwargs) > 0:     # kwargs is not empty
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of BaseModel object"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """'save' method
        Updates the public instance attribute 'updated_at'\
             with current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values\
             of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                new_dict[k] = v
        return new_dict
