#!/usr/bin/python3
"""
Module file_storage.py containing the 
FileStorage class for managing object storage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """A class to handle storing and retrieving objects in JSON format"""
    
    _file_path = "file.json"
    _objects = {}
    
    def all(self):
        """Returns a dictionary containing all stored objects"""
        return FileStorage._objects
    
    def new(self, obj):
        """Associates a new object with its corresponding key and stores it"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage._objects[key] = obj
    
    def save(self):
        """Serializes and saves the objects to a JSON file"""
        new_dict = {}
        for key, value in FileStorage._objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage._file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)
    
    def reload(self):
        """Deserializes and reloads objects from a JSON file"""
        try:
            with open(FileStorage._file_path, mode='r') as my_file:
                new_dict = json.load(my_file)
            
            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(f"{class_name}(**value)")
                FileStorage._objects[key] = obj
        
        except FileNotFoundError:
            pass
