#!/usr/bin/python3
"""
The City module
Inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Subclass of BaseModel"""

    state_id = ""   # State.id
    name = ""
