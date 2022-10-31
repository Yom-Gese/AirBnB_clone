#!/usr/bin/python3
"""Contains tests for the Class User"""
from contextlib import redirect_stdout
from datetime import datetime
from models.base_model import BaseModel
import io
import os
from models.amenity import Amenity
import unittest


class TestAmenityClassAttributes(unittest.TestCase):
    """Tests instantiation of Amenity objects and all the attributes
    defined in the class"""

    def setUp(self):
        """sets up the resources needed to run the tests"""

        self.amenity1 = Amenity()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        del self.amenity1

    def test_issubclass(self):
        """Tests if Amenity is a subclass of BaseModel"""

        self.assertIsInstance(self.amenity1, BaseModel)
        self.assertTrue(hasattr(self.amenity1, "id"))
        self.assertTrue(hasattr(self.amenity1, "created_at"))
        self.assertTrue(hasattr(self.amenity1, "updated_at"))

    def test_name_attribute(self):
        """Tests that objects of the class Amenity have the name attribute"""

        self.assertTrue(hasattr(self.amenity1, "name"))
        self.assertEqual(self.amenity1.name, "")
        self.amenity1.name = "WiFi"
        self.assertEqual(self.amenity1.name, "WiFi")


class TestAmenityClassMethods(unittest.TestCase):
    """Tests that methods defined in Amenity's parent class work on instances
    of class"""

    def setUp(self):
        """Sets up the resources needed to run the tests"""

        self.amenity2 = Amenity()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        if (os.path.isfile("filestorage.json")):
            os.remove("filestorage.json")
        del self.amenity2

    def test_save_method(self):
        """Tests that this methods correctly updates the public instance
        attribute updated_at with the current datetime when called"""

        old = self.amenity2.updated_at
        self.amenity2.save()
        new = self.amenity2.updated_at
        self.assertNotEqual(old, new)

    @staticmethod
    def captured_output(obj):
        """Captures what is printed to the standard output
        when the print method is called on obj"""

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            print(obj)
            return (captured_output.getvalue())

    def test_str_method(self):
        """Tests that the __str__ method correctly returns
        a string representation of objects of this class"""

        self.assertEqual(TestAmenityClassMethods.captured_output(
            self.amenity2), f"[Amenity]\
 ({self.amenity2.id}) {self.amenity2.__dict__}\n")

    def test_to_dcit_method(self):
        """Tests the to_dict method on Amenity objects"""

        amenity_dict = self.amenity2.to_dict()

        for att in ["id", "created_at", "updated_at","__class__"]:
            self.assertIn(att, amenity_dict.keys())
            self.assertTrue(type(amenity_dict[att]) == str)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

        created_date = datetime.fromisoformat(amenity_dict["created_at"])
        self.assertEqual(created_date, self.amenity2.created_at)

        updated_at_date = datetime.fromisoformat(amenity_dict["updated_at"])
        self.assertEqual(updated_at_date, self.amenity2.updated_at)


if __name__ == "__main__":
    unittest.main()
