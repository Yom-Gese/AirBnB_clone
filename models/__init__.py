#!/usr/bin/python3
"""File engines init file"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
