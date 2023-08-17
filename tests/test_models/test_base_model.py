#!/usr/bin/python3
"""Test module for BaseModel class"""
import unittest
import json
import pep8
import datetime
from time import sleep

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the implementation of the BaseModel class"""

    def test_module_docstring(self):
        """Check if the module has documentation"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_pep8_conformance_base_model(self):
        """Test if models/base_model.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_base_model(self):
        """Test if tests/test_models/test_base_model.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_base_model.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_constructor_docstring(self):
        """Check if the constructor has documentation"""
        self.assertTrue(len(BaseModel.__init__.__doc__) > 0)

    def test_first_task(self):
        """Test creation of an instance and its to_dict method"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str,
        }
        my_model_json = my_model.to_dict()
        for key, value in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_base_types(self):
        """Test types of attributes in the instance's __dict__"""
        second_model = BaseModel()
        self.assertIs(type(second_model), BaseModel)
        second_model.name = "Andres"
        second_model.my_number = 80
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime,
        }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, second_model.__dict__)
                self.assertIs(type(second_model.__dict__[key]), value)

    def test_uuid(self):
        """Test that different instances have different uuids"""
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_model(self):
        """Test datetime attributes in the BaseModel instance"""
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_3.updated_at)
        self.assertNotEqual(model_3.created_at, model_4.created_at)

    def test_string_representation(self):
        """Test the magic method __str__"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        id_model = my_model.id

        expected = "[BaseModel] ({}) {}".format(id_model, my_model.__dict__)
        self.assertEqual(str(my_model), expected)

    def test_constructor_kwargs(self):
        """Test constructor that takes kwargs as attribute values"""
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        json_attributes = obj.to_dict()

        obj2 = BaseModel(**json_attributes)

        self.assertIsInstance(obj2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(obj, obj2)

    def test_file_save(self):
        """Test that information is saved to a file"""
        b3 = BaseModel()
        b3.save()
        with open("file.json", "r") as f:
            self.assertIn(b3.id, f.read())


if __name__ == "__main__":
    unittest.main()
