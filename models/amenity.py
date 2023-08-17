#!/usr/bin/python3
"""A class inheriting from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class representing amenities"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the Amenity object"""
        super().__init__(*args, **kwargs)
