#!/usr/bin/python3
"""Test case for the FileStorage module"""
import unittest
import os
import json
import pep8
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def test_pep8_conformance(self):
        """Test if models/engine/file_storage.py conforms to PEP8 style."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def setUp(self):
        """Set up the test environment"""
        self.b1 = BaseModel()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.r1 = Review()
        self.s1 = State()
        self.u1 = User()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")

    def tearDown(self):
        """Tear down the test environment"""
        del self.b1
        del self.a1
        del self.c1
        del self.p1
        del self.r1
        del self.s1
        del self.u1
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_method(self):
        """Test the all() method of FileStorage"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_storage_empty(self):
        """Check if storage is not empty"""
        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """Check the type of the storage"""
        self.assertEqual(dict, type(self.storage.all()))

    def test_new_method(self):
        """Test the new() method of FileStorage"""
        obj = self.storage.all()
        self.u1.id = 1234
        self.u1.name = "Julien"
        self.storage.new(self.u1)
        key = "{}.{}".format(self.u1.__class__.__name__, self.u1.id)
        self.assertIsNotNone(obj[key])

    def test_json_loading(self):
        """Test if the JSON file loads correctly"""
        with open("file.json") as f:
            dic = json.load(f)
            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """Test if the file.json file exists"""
        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_docstrings(self):
        """Test if all methods have docstrings"""
        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(FileStorage.reload.__doc__)


if __name__ == "__main__":
    unittest.main()
