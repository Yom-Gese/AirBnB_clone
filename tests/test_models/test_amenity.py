#!/usr/bin/python3

"""
    Defines a class Amenity.
"""


from models.amenity import Amenity
import unittest
import models
import os


class TestAmenity(unittest.TestCase):
    """Represent a Amenity."""

    def setUp(self):
        """SetUp method"""

        self.amenity = Amenity()

    def TearDown(self):
        """TearDown method."""

        del self.amenity

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.amenity.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Amenity.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Test File amenity.py permissions"""

        test_file = os.access("models/amenity.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/amenity.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/amenity.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test type object of Amenity"""

        self.assertEqual(
            str(type(self.amenity)),
            "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(self.amenity, Amenity)
