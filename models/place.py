#!/usr/bin/python3
"""A class inheriting from Base Model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A class representing places"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize a Place object"""
        super().__init__(*args, **kwargs)
