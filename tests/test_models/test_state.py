#!/usr/bin/python3
"""Test module for State class"""
import unittest
import pep8

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test the implementation of the State class"""

    def test_module_docstring(self):
        """Check if the module has documentation"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_pep8_conformance_state(self):
        """Test if models/state.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_state(self):
        """Test if tests/test_models/test_state.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_state.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_constructor_docstring(self):
        """Check if the constructor has documentation"""
        self.assertTrue(len(State.__init__.__doc__) > 0)

    def test_inheritance(self):
        """Check if State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Check the types of State's attributes"""
        self.assertIsInstance(State.name, str)


if __name__ == "__main__":
    unittest.main()
