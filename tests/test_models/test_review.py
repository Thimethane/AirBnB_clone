#!/usr/bin/python3
"""Test module for Review class"""
import unittest
import pep8

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test the implementation of the Review class"""

    def test_module_docstring(self):
        """Check if the module has documentation"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_pep8_conformance_review(self):
        """Test if models/review.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_review(self):
        """Test if tests/test_models/test_review.py conforms to PEP8 style."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_review.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_constructor_docstring(self):
        """Check if the constructor has documentation"""
        self.assertTrue(len(Review.__init__.__doc__) > 0)

    def test_inheritance(self):
        """Check if Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Check the types of Review's attributes"""
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)


if __name__ == "__main__":
    unittest.main()
