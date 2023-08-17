#!/usr/bin/python3
"""Test module for City class"""
import unittest
import json
import pep8
import datetime

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test the implementation of the City class"""

    def test_module_docstring(self):
        """Check if the module has documentation"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_pep8_conformance_city(self):
        """Test if models/city.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/city.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_city(self):
        """Test if tests/test_models/test_city.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_city.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_constructor_docstring(self):
        """Check if the constructor has documentation"""
        self.assertTrue(len(City.__init__.__doc__) > 0)

    def test_inheritance(self):
        """Check if City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Check the types of City's attributes"""
        self.assertIsInstance(City.name, str)
        self.assertIsInstance(City.state_id, str)


if __name__ == "__main__":
    unittest.main()
