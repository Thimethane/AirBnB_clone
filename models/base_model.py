#!/usr/bin/python3
"""This module defines the base class BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """The fundamental class that serves as the foundation for other models"""

    def __init__(self, *args, **kwargs):
        """Constructor for the BaseModel class"""

        if kwargs:
            # Convert datetime strings to datetime objects
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )

            # Set instance attributes from keyword arguments
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            # Generate a unique ID and timestamps for a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of a BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' instance with the current datetime and save changes"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of an instance"""
        new_dict = dict(self.__dict__)
        new_dict["created_at"] = self.__dict__["created_at"].isoformat()
        new_dict["updated_at"] = self.__dict__["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
