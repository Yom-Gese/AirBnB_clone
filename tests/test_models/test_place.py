#!/usr/bin/python3
"""Contains tests for the Class Place"""
from contextlib import redirect_stdout
from datetime import datetime
from models.base_model import BaseModel
import io
import os
from models.place import Place
import unittest


class TestPLaceClassAttributes(unittest.TestCase):
    """Tests instantiation of Place objects and all the attributes
    defined in the class"""

    def setUp(self):
        """sets up the resources needed to run the tests"""

        self.place1 = Place()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        del self.place1

    def test_issubclass(self):
        """Tests if Place is a subclass of BaseModel"""

        self.assertIsInstance(self.place1, BaseModel)
        self.assertTrue(hasattr(self.place1, "id"))
        self.assertTrue(hasattr(self.place1, "created_at"))
        self.assertTrue(hasattr(self.place1, "updated_at"))

    def test_city_id_attribute(self):
        """Tests that objects of Place class have the attribute email"""

        self.assertTrue(hasattr(self.place1, "city_id"))
        self.assertEqual(self.place1.city_id, "")

    def test_user_id_attribute(self):
        """Tests the user_id attribute"""
        self.assertTrue(hasattr(self.place1, "user_id"))
        self.assertEqual(self.place1.user_id, "")

    def test_name_attribute(self):
        """Tests that objects of the class Place have the name attribute"""

        self.assertTrue(hasattr(self.place1, "name"))
        self.assertEqual(self.place1.name, "")
        self.place1.name = "Nakuru"
        self.assertEqual(self.place1.name, "Nakuru")

    def test_description_attributes(self):
        """Tests that objects of the class Place have the description
        attribute"""

        self.assertTrue(hasattr(self.place1, "description"))
        self.assertEqual(self.place1.description, "")

        self.place1.description = "good"
        self.assertEqual(self.place1.description, "good")

    def test_number_rooms_attribute(self):
        """Tests that objects of the class Place have the number_rooms
        attribute"""

        self.assertTrue(hasattr(self.place1, "number_rooms"))
        self.assertTrue(type(self.place1.number_rooms) == int)
        self.assertEqual(self.place1.number_rooms, 0)
        self.place1.number_rooms = 5
        self.assertEqual(self.place1.number_rooms, 5)

    def test_number_bathrooms_attribute(self):
        """Tests that objects of the class Place have the number_bathrooms
        attribute"""

        self.assertTrue(hasattr(self.place1, "number_bathrooms"))
        self.assertEqual(self.place1.number_bathrooms, 0)
        self.assertTrue(type(self.place1.number_bathrooms) == int)
        self.place1.number_bathrooms = 5
        self.assertEqual(self.place1.number_bathrooms, 5)


    def test_max_guest_attribute(self):
        """Tests that objects of the class Place have the max_guest
        attribute"""

        self.assertTrue(hasattr(self.place1, "max_guest"))
        self.assertTrue(type(self.place1.max_guest) == int)
        self.assertEqual(self.place1.max_guest, 0)
        self.place1.max_guest = 3
        self.assertEqual(self.place1.max_guest, 3)

    def test_price_by_night_attribute(self):
        """Tests that objects of the class Place have the price_by_night
        attribute"""

        self.assertTrue(hasattr(self.place1, "price_by_night"))
        self.assertTrue(type(self.place1.price_by_night) == int)
        self.assertEqual(self.place1.price_by_night, 0)
        self.place1.price_by_night = 100
        self.assertEqual(self.place1.price_by_night, 100)

    def test_latitude_attribute(self):
        """Test Place latitude attribute"""
        self.assertTrue(hasattr(self.place1, "latitude"))
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(self.place1.latitude, 0.0)
        self.place1.latitude = 10.5
        self.assertEqual(self.place1.latitude, 10.5)

    def test_longitude_attribute(self):
        """Test Class Place longitude attribute"""
        self.assertTrue(hasattr(self.place1, "latitude"))
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(self.place1.latitude, 0.0)
        self.place1.longitude = 17.8
        self.assertEqual(self.place1.longitude, 17.8)

    def test_amenity_ids_attribute(self):
        """Test Class Place amenity_ids attribute"""

        self.assertTrue(hasattr(self.place1, "amenity_ids"))
        self.assertEqual(type(self.place1.amenity_ids), list)
        self.assertEqual(len(self.place1.amenity_ids), 0)


class TestPlaceClassMethods(unittest.TestCase):
    """Tests that methods defined in Place's parent class work on instances
    of class User"""

    def setUp(self):
        """Sets up the resources needed to run the tests"""

        self.place2 = Place()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        if (os.path.isfile("filestorage.json")):
            os.remove("filestorage.json")
        del self.place2

    def test_save_method(self):
        """Tests that this methods correctly updates the public instance
        attribute updated_at with the current datetime when called"""

        old = self.place2.updated_at
        self.place2.save()
        new = self.place2.updated_at
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

        self.assertEqual(TestPlaceClassMethods.captured_output(
            self.place2), f"[Place]\
 ({self.place2.id}) {self.place2.__dict__}\n")

    def test_to_dcit_method(self):
        """Tests the to_dict method on User objects"""

        place_dict = self.place2.to_dict()

        for att in ["id", "created_at", "updated_at","__class__"]:
            self.assertIn(att, place_dict.keys())
            self.assertTrue(type(place_dict[att]) == str)
        self.assertEqual(place_dict["__class__"], "Place")

        created_date = datetime.fromisoformat(place_dict["created_at"])
        self.assertEqual(created_date, self.place2.created_at)

        updated_at_date = datetime.fromisoformat(place_dict["updated_at"])
        self.assertEqual(updated_at_date, self.place2.updated_at)


if __name__ == "__main__":
    unittest.main()
