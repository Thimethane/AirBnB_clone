#!/usr/bin/python3
"""A class inheriting from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class representing reviews"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a Review object"""
        super().__init__(*args, **kwargs)
