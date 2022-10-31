#!/usr/bin/python3
"""
The User module
Inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Subclass of BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
