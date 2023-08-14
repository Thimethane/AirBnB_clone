#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """Serializes and deserializes objects to/from JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """public instance method that deserializes a JSON file to objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for key, value in data.items():
                cls_name = value['__class__']
                if cls_name == 'BaseModel':
                    obj = BaseModel(**value)
                elif cls_name == 'User':
                    obj = User(**value)
                elif cls_name == 'Place':
                    obj = Place(**value)
                elif cls_name == 'State':
                    obj = State(**value)
                elif cls_name == 'City':
                    obj = City(**value)
                elif cls_name == 'Amenity':
                    obj = Amenity(**value)
                elif cls_name == 'Review':
                    obj = Review(**value)
                else:
                    continue
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
