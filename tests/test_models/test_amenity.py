#!/usr/bin/python3
"""Test module for Amenity class"""
import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the implementation of the Amenity class"""

    def test_module_docstring(self):
        """Check if the module has documentation"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_pep8_conformance_amenity(self):
        """Test if models/amenity.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/amenity.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_amenity(self):
        """Test if tests/test_models/test_amenity.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_amenity.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_constructor_docstring(self):
        """Check if the constructor has documentation"""
        self.assertTrue(len(Amenity.__init__.__doc__) > 0)

    def test_inheritance(self):
        """Check if Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Check the types of Amenity's attributes"""
        self.assertIsInstance(Amenity.name, str)


if __name__ == "__main__":
    unittest.main()
