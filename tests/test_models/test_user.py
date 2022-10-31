#!/usr/bin/python3
"""Contains tests for the Class User"""
from contextlib import redirect_stdout
from datetime import datetime
from models.base_model import BaseModel
import io
import os
from models.user import User
import unittest


class TestUserClassAttributes(unittest.TestCase):
    """Tests instantiation of User objects and all the attributes
    defined in the class"""

    def setUp(self):
        """sets up the resources needed to run the tests"""

        self.user1 = User()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        del self.user1

    def test_issubclass(self):
        """Tests if User is a subclass of BaseModel"""

        self.assertIsInstance(self.user1, BaseModel)
        self.assertTrue(hasattr(self.user1, "id"))
        self.assertTrue(hasattr(self.user1, "created_at"))
        self.assertTrue(hasattr(self.user1, "updated_at"))

    def test_email_attribute(self):
        """Tests that objects of User class have the attribute email"""

        self.assertTrue(hasattr(self.user1, "email"))
        self.assertEqual(self.user1.email, "")
        self.user1.email = "beldinemoturi@gmail.com"
        self.assertEqual(self.user1.email, "beldinemoturi@gmail.com")

    def test_password_attribute(self):
        """Tests that objects of the class User have the password attribute"""

        self.assertTrue(hasattr(self.user1, "password"))
        self.assertEqual(self.user1.password, "")
        self.user1.password = "password1"
        self.assertEqual(self.user1.password, "password1")

    def test_name_attributes(self):
        """Tests that objects of the class User have the first_name and
        last_name attributes"""

        self.assertTrue(hasattr(self.user1, "first_name"))
        self.assertTrue(hasattr(self.user1, "last_name"))
        self.assertEqual(self.user1.first_name, "")
        self.assertEqual(self.user1.last_name, "")

        self.user1.first_name = "Bella"
        self.user1.last_name = "Moturi"
        self.assertEqual(self.user1.first_name, "Bella")
        self.assertEqual(self.user1.last_name, "Moturi")


class TestUserClassMethods(unittest.TestCase):
    """Tests that methods defined in User's parent class work on instances
    of class User"""

    def setUp(self):
        """Sets up the resources needed to run the tests"""

        self.user2 = User()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        if (os.path.isfile("filestorage.json")):
            os.remove("filestorage.json")
        del self.user2

    def test_save_method(self):
        """Tests that this methods correctly updates the public instance
        attribute updated_at with the current datetime when called"""

        old = self.user2.updated_at
        self.user2.save()
        new = self.user2.updated_at
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

        self.assertEqual(TestUserClassMethods.captured_output(
            self.user2), f"[User]\
 ({self.user2.id}) {self.user2.__dict__}\n")

    def test_to_dcit_method(self):
        """Tests the to_dict method on User objects"""

        user_dict = self.user2.to_dict()

        for att in ["id", "created_at", "updated_at","__class__"]:
            self.assertIn(att, user_dict.keys())
            self.assertTrue(type(user_dict[att]) == str)
        self.assertEqual(user_dict["__class__"], "User")

        created_date = datetime.fromisoformat(user_dict["created_at"])
        self.assertEqual(created_date, self.user2.created_at)

        updated_at_date = datetime.fromisoformat(user_dict["updated_at"])
        self.assertEqual(updated_at_date, self.user2.updated_at)


if __name__ == "__main__":
    unittest.main()
