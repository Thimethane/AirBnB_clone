#!/usr/bin/python3
"""Module for testing multiple classes' documentation and style"""
import inspect
import pep8


class TestClassDocumentationAndStyle:
    """Class to test documentation and style of multiple classes"""

    def __init__(self, tests, _classes):
        """Constructor"""
        self.tests = tests
        self.classes = _classes

    def test_documentation(self):
        """Test documentation of classes, methods, and modules"""
        for _class in self.classes:
            with self.tests.subTest(msg=f"Testing {_class.__name__}"):
                self.check_class_documentation(_class)

    def test_pep8(self, files):
        """Test PEP8 style conformity of specified files"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(files)
        self.tests.assertEqual(
            result.total_errors, 0, "Found code style errors and warnings."
        )

    def check_class_documentation(self, _class):
        """Check documentation of the module, class, and methods"""
        class_functions = inspect.getmembers(_class, inspect.isfunction)

        with self.tests.subTest(msg="Testing class documentation"):
            class_doc = _class.__doc__
            self.tests.assertGreaterEqual(len(class_doc), 1)

        for function_name, function in class_functions:
            with self.tests.subTest(
                msg=f"Testing {function_name} method documentation"
            ):
                function_doc = function.__doc__
                self.tests.assertGreaterEqual(len(function_doc), 1)


if __name__ == "__main__":
    unittest.main()
