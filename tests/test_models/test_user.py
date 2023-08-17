#!/usr/bin/python3
"""Test module for User class"""
import unittest
import pep8

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test the implementation of the User class"""

    def test_module_docstring(self):
        """Check if the module has documentation"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_pep8_conformance_user(self):
        """Test if models/user.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_user(self):
        """Test if tests/test_models/test_user.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(["tests/test_models/test_user.py"])
        self.assertEqual(res.total_errors, 0, "Found code style errors (and warnings).")

    def test_constructor_docstring(self):
        """Check if the constructor has documentation"""
        self.assertTrue(len(User.__init__.__doc__) > 0)

    def test_inheritance(self):
        """Check if User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Check the types of User's attributes"""
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)


if __name__ == "__main__":
    unittest.main()
