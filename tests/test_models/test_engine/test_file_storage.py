#!/usr/bin/python3
"""Contains unitests for the file storage of the console"""
from models.engine.file_storage import FileStorage
import json
from models import storage
from models.base_model import BaseModel
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """Tests all the methods and attributes defined in class FileStorage"""

    @classmethod
    def tearDownClass(cls):
        """Deletes the resources created after all the tests have run"""

        os.remove("filestorage.json")

    def  test_filestorage_json(self):
        """Tets that the file "filestorage.json" does not exists
        the first time the program is run"""

        self.assertFalse(os.path.isfile("filestorage.json"))

    def test_all_method(self):
        """Tests that the FileStorage all method returns
        an empty dictionary the first time the program is run"""

        all_objs = storage.all()
        self.assertEqual(all_objs, {})

    def test_new_and_save_method(self):
        """Tests that the new method adds a new object created to the class
        attribute FileStorage.__objects, and that the save method
        saves this new object to a json file"""

        new_model = BaseModel()
        all_objs = storage.all()
        self.assertTrue(len(all_objs) == 1)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == BaseModel)

        new_model.save()
        self.assertTrue(os.path.isfile("filestorage.json"))
        with open("filestorage.json", 'r') as f:
            from_json = json.load(f)
            self.assertTrue(type(from_json) == dict)
            self.assertTrue(len(from_json) == 1)

    def test_reload_method(self):
        """Tests that the reload method properly reloads all objects
        previously created"""

        new_model2 = BaseModel()
        new_model2.save()
        storage.reload()
        all_objs = storage.all()
        self.assertTrue(len(all_objs) == 2)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == BaseModel)
