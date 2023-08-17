#!/usr/bin/python3
"""A class inheriting from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class representing cities"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a City object"""
        super().__init__(*args, **kwargs)
