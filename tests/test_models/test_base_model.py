#!/usr/bin/python3
"""Contains test cases for the BaseModel class used
for all other classes in this project"""
from contextlib import redirect_stdout
from datetime import datetime
from models.base_model import BaseModel
import io
import unittest


class TestBaseModelClassInstantiation(unittest.TestCase):
    """Tests the Instantiation of objects; attribute assignment"""

    def setUp(self):
        """sets up the resources required to run the tests"""

        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """deletes the resources used after tests are run"""

        del self.model1
        del self.model2

    def test_id_attribute(self):
        """Tests that objects of this class are properly instantiated
        with a universally unique identifier"""

        self.assertTrue(hasattr(self.model1, "id"))
        self.assertIs(type(self.model1.id), str)
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_created_at_attribute(self):
        """Tests that the current datetime is assigned when
        objects of this class are instantiated"""

        t = datetime.now()
        created = self.model1.created_at.isoformat(timespec='seconds')
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertIs(type(self.model1.created_at), datetime)
        self.assertGreaterEqual(t.isoformat(timespec='seconds'), created)

    def test_updated_at_attribute(self):
        """Tests that the current datetime is assigned when
        objects of this class are updated"""

        self.assertTrue(hasattr(self.model1, "updated_at"))
        self.assertIs(type(self.model1.updated_at), datetime)
        self.model1.save()
        t = datetime.now()
        update = self.model1.updated_at.isoformat(timespec='seconds')
        self.assertEqual(t.isoformat(timespec='seconds'), update)

    def test_intantiation_with_kwargs(self):
        """Tests that objects can properly be created with the
        kwargs argument"""

        attributes = ['id', 'created_at', 'updated_at']

        my_model = BaseModel(**{})
        self.assertNotIn('__class__', my_model.__dict__)
        for att in attributes:
            self.assertTrue(hasattr(my_model, att))

        model1_json = self.model1.to_dict()
        new_model1 = BaseModel(**model1_json)
        self.assertNotIn('__class__', new_model1.__dict__)
        self.assertEqual(len(new_model1.__dict__), len(self.model1.__dict__))
        for att in attributes:
            self.assertTrue(hasattr(new_model1, att))
            self.assertEqual(new_model1.__dict__[att],
                             self.model1.__dict__[att])

        self.model2.name = "My_Second_model"
        self.model2.number = 100
        model2_json = self.model2.to_dict()
        new_model2 = BaseModel(**model2_json)
        self.assertNotIn('__class__', new_model1.__dict__)
        self.assertEqual(len(self.model2.__dict__), len(new_model2.__dict__))
        attributes.extend(['name', 'number'])
        for att in attributes:
            self.assertTrue(hasattr(new_model2, att))
            self.assertEqual(new_model2.__dict__[att],
                             self.model2.__dict__[att])


class TestBaseModelClassMethods(unittest.TestCase):
    """defines functions that test the methods defined in the Base class"""

    def setUp(self):
        """Sets up the resources needed to run the tests"""

        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        del self.model1
        del self.model2

    def test_save_method(self):
        """Tests that this methods correctly updates the public instance
        attribute updated_at with the current datetime when called"""

        old = self.model1.updated_at
        self.model1.save()
        new = self.model1.updated_at
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

        self.assertEqual(TestBaseModelClassMethods.captured_output(
            self.model1), f"[BaseModel]\
 ({self.model1.id}) {self.model1.__dict__}\n")

    def test_to_dict_method(self):
        """Tests that the to_dict methd returns the expected dictionary
        representation of the instance attributes"""

        my_dict = self.model1.to_dict()

        self.assertTrue(type(my_dict) == dict)

        keys = ["id", "created_at", "updated_at", "__class__"]
        self.assertEqual(len(keys), len(my_dict.keys()))
        for key in keys:
            self.assertIn(key, my_dict.keys())

        self.assertEqual(my_dict["id"], self.model1.id)
        self.assertTrue(type(my_dict["id"]) == str)

        self.assertTrue(type(my_dict["__class__"]) == str)
        self.assertTrue(my_dict["__class__"] ==
                        self.model1.__class__.__name__)

        self.assertTrue(type(my_dict["created_at"]) == str)
        created_at_date = datetime.fromisoformat(my_dict["created_at"])
        self.assertEqual(created_at_date, self.model1.created_at)

        self.assertTrue(type(my_dict["updated_at"]) == str)
        updated_at_date = datetime.fromisoformat(my_dict["updated_at"])
        self.assertEqual(updated_at_date, self.model1.updated_at)


if __name__ == '__main__':
    unittest.main()
