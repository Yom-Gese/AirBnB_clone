#!/usr/bin/python3

"""
    Defines a class TestUser.
"""


from models.user import User
import unittest
import models
import os


class TestUser(unittest.TestCase):
    """Represent a User."""

    def setUp(self):
        """SetUp method"""

        self.user = User()

    def TearDown(self):
        """TearDown method."""

        del self.user

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.user.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(User.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Test File user.py permissions"""

        test_file = os.access("models/user.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/user.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/user.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test type object of User"""

        self.assertEqual(
            str(type(self.user)),
            "<class 'models.user.User'>")
        self.assertIsInstance(self.user, User)
