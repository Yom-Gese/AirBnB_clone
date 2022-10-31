#!/usr/bin/python3
"""
The Review module
Inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Subclass of BaseModel"""

    place_id = ""   # Place.id
    user_id = ""    # User.id
    text = ""
