#!/usr/bin/python3
"""Test module for the console"""

import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test class for the console"""

    def create_console_instance(self):
        """Create an instance of the console"""
        return HBNBCommand()

    def test_quit_command(self):
        """Test the 'quit' command"""
        console_instance = self.create_console_instance()
        self.assertTrue(console_instance.onecmd("quit"))

    def test_eof_command(self):
        """Test the 'EOF' command"""
        console_instance = self.create_console_instance()
        self.assertTrue(console_instance.onecmd("EOF"))
