#!/usr/bin/python3
"""Contains tests for the Class User"""
from contextlib import redirect_stdout
from datetime import datetime
from models.base_model import BaseModel
import io
import os
from models.state import State
import unittest


class TestStateClassAttributes(unittest.TestCase):
    """Tests instantiation of State objects and all the attributes
    defined in the class"""

    def setUp(self):
        """sets up the resources needed to run the tests"""

        self.state1 = State()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        del self.state1

    def test_issubclass(self):
        """Tests if State is a subclass of BaseModel"""

        self.assertIsInstance(self.state1, BaseModel)
        self.assertTrue(hasattr(self.state1, "id"))
        self.assertTrue(hasattr(self.state1, "created_at"))
        self.assertTrue(hasattr(self.state1, "updated_at"))

    def test_name_attribute(self):
        """Tests that objects of the class State have the name attribute"""

        self.assertTrue(hasattr(self.state1, "name"))
        self.assertEqual(self.state1.name, "")
        self.state1.name = "Kasarani"
        self.assertEqual(self.state1.name, "Kasarani")


class TestStateClassMethods(unittest.TestCase):
    """Tests that methods defined in State's parent class work on instances
    of class"""

    def setUp(self):
        """Sets up the resources needed to run the tests"""

        self.state2 = State()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        if (os.path.isfile("filestorage.json")):
            os.remove("filestorage.json")
        del self.state2

    def test_save_method(self):
        """Tests that this methods correctly updates the public instance
        attribute updated_at with the current datetime when called"""

        old = self.state2.updated_at
        self.state2.save()
        new = self.state2.updated_at
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

        self.assertEqual(TestStateClassMethods.captured_output(
            self.state2), f"[State]\
 ({self.state2.id}) {self.state2.__dict__}\n")

    def test_to_dcit_method(self):
        """Tests the to_dict method on State objects"""

        state_dict = self.state2.to_dict()

        for att in ["id", "created_at", "updated_at","__class__"]:
            self.assertIn(att, state_dict.keys())
            self.assertTrue(type(state_dict[att]) == str)
        self.assertEqual(state_dict["__class__"], "State")

        created_date = datetime.fromisoformat(state_dict["created_at"])
        self.assertEqual(created_date, self.state2.created_at)

        updated_at_date = datetime.fromisoformat(state_dict["updated_at"])
        self.assertEqual(updated_at_date, self.state2.updated_at)


if __name__ == "__main__":
    unittest.main()
