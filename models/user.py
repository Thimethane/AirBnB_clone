#!/usr/bin/python3
"""A class User inheriting from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class representing users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
