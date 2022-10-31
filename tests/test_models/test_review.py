#!/usr/bin/python3
"""Contains tests for the Class User"""
from contextlib import redirect_stdout
from datetime import datetime
from models.base_model import BaseModel
import io
import os
from models.review import Review
import unittest


class TestReviewClassAttributes(unittest.TestCase):
    """Tests instantiation of Review objects and all the attributes
    defined in the class"""

    def setUp(self):
        """sets up the resources needed to run the tests"""

        self.review1 = Review()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        del self.review1

    def test_issubclass(self):
        """Tests if Review is a subclass of BaseModel"""

        self.assertIsInstance(self.review1, BaseModel)
        self.assertTrue(hasattr(self.review1, "id"))
        self.assertTrue(hasattr(self.review1, "created_at"))
        self.assertTrue(hasattr(self.review1, "updated_at"))

    def test_place_id_attribute(self):
        """Tests that objects of Review class have the attribute place_id"""

        self.assertTrue(hasattr(self.review1, "place_id"))
        self.assertEqual(self.review1.place_id, "")

    def test_user_id_attribute(self):
        """Tests that objects of the class Review have the user_id attribute"""

        self.assertTrue(hasattr(self.review1, "user_id"))
        self.assertEqual(self.review1.user_id, "")

    def test_text_attributes(self):
        """Tests that objects of the class Review have the text attribute"""

        self.assertTrue(hasattr(self.review1, "text"))
        self.assertEqual(self.review1.text, "")
        self.review1.text = "good"
        self.assertEqual(self.review1.text, "good")


class TestReviewClassMethods(unittest.TestCase):
    """Tests that methods defined in Review's parent class work on instances
    of class User"""

    def setUp(self):
        """Sets up the resources needed to run the tests"""

        self.review2 = Review()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        if (os.path.isfile("filestorage.json")):
            os.remove("filestorage.json")
        del self.review2

    def test_save_method(self):
        """Tests that this methods correctly updates the public instance
        attribute updated_at with the current datetime when called"""

        old = self.review2.updated_at
        self.review2.save()
        new = self.review2.updated_at
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

        self.assertEqual(TestReviewClassMethods.captured_output(
            self.review2), f"[Review]\
 ({self.review2.id}) {self.review2.__dict__}\n")

    def test_to_dcit_method(self):
        """Tests the to_dict method on Review objects"""

        review_dict = self.review2.to_dict()

        for att in ["id", "created_at", "updated_at","__class__"]:
            self.assertIn(att, review_dict.keys())
            self.assertTrue(type(review_dict[att]) == str)
        self.assertEqual(review_dict["__class__"], "Review")

        created_date = datetime.fromisoformat(review_dict["created_at"])
        self.assertEqual(created_date, self.review2.created_at)

        updated_at_date = datetime.fromisoformat(review_dict["updated_at"])
        self.assertEqual(updated_at_date, self.review2.updated_at)


if __name__ == "__main__":
    unittest.main()
