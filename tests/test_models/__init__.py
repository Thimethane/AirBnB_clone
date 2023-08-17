#!/usr/bin/python3
"""Create a unique instance of FileStorage for the application"""
from models.engine.file_storage import FileStorage

"""Instantiate the 'storage' variable as a FileStorage instance"""
storage = FileStorage()
storage.reload()
