#!/usr/bin/python3
"""Contains tests for the Class User"""
from contextlib import redirect_stdout
from datetime import datetime
from models.base_model import BaseModel
import io
import os
from models.city import City
import unittest


class TestCityClassAttributes(unittest.TestCase):
    """Tests instantiation of City objects and all the attributes
    defined in the class"""

    def setUp(self):
        """sets up the resources needed to run the tests"""

        self.city1 = City()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        del self.city1

    def test_issubclass(self):
        """Tests if City is a subclass of BaseModel"""

        self.assertIsInstance(self.city1, BaseModel)
        self.assertTrue(hasattr(self.city1, "id"))
        self.assertTrue(hasattr(self.city1, "created_at"))
        self.assertTrue(hasattr(self.city1, "updated_at"))

    def test_state_id_attribute(self):
        """Tests that objects of City class have the attribute state_id"""

        self.assertTrue(hasattr(self.city1, "state_id"))
        self.assertEqual(self.city1.state_id, "")

    def test_nameattribute(self):
        """Tests that objects of the class City have the name attribute"""

        self.assertTrue(hasattr(self.city1, "name"))
        self.assertEqual(self.city1.name, "")
        self.city1.name = "Nakuru"
        self.assertEqual(self.city1.name, "Nakuru")


class TestCityClassMethods(unittest.TestCase):
    """Tests that methods defined in City's parent class work on instances
    of class City"""

    def setUp(self):
        """Sets up the resources needed to run the tests"""

        self.city2 = City()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        if (os.path.isfile("filestorage.json")):
            os.remove("filestorage.json")
        del self.city2

    def test_save_method(self):
        """Tests that this methods correctly updates the public instance
        attribute updated_at with the current datetime when called"""

        old = self.city2.updated_at
        self.city2.save()
        new = self.city2.updated_at
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

        self.assertEqual(TestCityClassMethods.captured_output(
            self.city2), f"[City]\
 ({self.city2.id}) {self.city2.__dict__}\n")

    def test_to_dcit_method(self):
        """Tests the to_dict method on City objects"""

        city_dict = self.city2.to_dict()

        for att in ["id", "created_at", "updated_at","__class__"]:
            self.assertIn(att, city_dict.keys())
            self.assertTrue(type(city_dict[att]) == str)
        self.assertEqual(city_dict["__class__"], "City")

        created_date = datetime.fromisoformat(city_dict["created_at"])
        self.assertEqual(created_date, self.city2.created_at)

        updated_at_date = datetime.fromisoformat(city_dict["updated_at"])
        self.assertEqual(updated_at_date, self.city2.updated_at)


if __name__ == "__main__":
    unittest.main()
