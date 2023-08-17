#!/usr/bin/python3
"""Create a unique FileStorage instance for the application"""
from models.engine.file_storage import FileStorage

# Create a single instance of FileStorage
storage = FileStorage()

# Reload objects from storage
storage.reload()
