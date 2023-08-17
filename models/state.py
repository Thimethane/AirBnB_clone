#!/usr/bin/python3
"""A class inheriting from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """A class representing states"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a State object"""
        super().__init__(*args, **kwargs)
