#!/usr/bin/python3
"""Create a new instance of a class FileStorage"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
