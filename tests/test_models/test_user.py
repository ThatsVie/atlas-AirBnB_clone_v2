#!/usr/bin/python3
"""Tests for User model"""

import os
import unittest
import pycodestyle
from models import storage
from models.user import User
from models.base_model import BaseModel, Base


class TestUserModel(unittest.TestCase):
    """Tests for the User model subclass of BaseModel"""

    @classmethod
    def setUpClass(cls):
        """Set up method to be executed before each test"""
        cls.user_1 = User(
            email="pugs@puggies.com",
            password="wordpass",
            first_name="Puggy",
            last_name="Wuggy"
        )
        cls.user_2 = User(
            email="puggies@wuggies.com",
            password="backrolls",
            first_name="Pookie",
            last_name="MyLove"
        )
        cls.user_3 = User(**cls.user_1.to_dict())
        storage.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up method to be executed following all tests"""
        del cls.user_1
        del cls.user_2
        del cls.user_3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_module_docstring_exists(self):
        """Test if module docstring is present"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_pycodestyle_compliance(self):
        """Test code style compliance using pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/user.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_attribute_initialization(self):
        """Test attributes initialized with correct value & type"""
        self.assertEqual(type(self.user_1.email), str)
        self.assertEqual(type(self.user_1.password), str)
        self.assertEqual(type(self.user_1.first_name), str)
        self.assertEqual(type(self.user_1.last_name), str)
        self.assertEqual(type(self.user_2.email), str)
        self.assertEqual(type(self.user_2.password), str)
        self.assertEqual(type(self.user_2.first_name), str)
        self.assertEqual(type(self.user_2.last_name), str)
        self.assertEqual(type(self.user_3.email), str)
        self.assertEqual(type(self.user_3.password), str)
        self.assertEqual(type(self.user_3.first_name), str)
        self.assertEqual(type(self.user_3.last_name), str)
        self.assertEqual(self.user_1.email, "pugs@puggies.com")
        self.assertEqual(self.user_1.password, "wordpass")
        self.assertEqual(self.user_1.first_name, "Puggy")
        self.assertEqual(self.user_1.last_name, "Wuggy")
        self.assertEqual(self.user_2.email, "puggies@wuggies.com")
        self.assertEqual(self.user_2.password, "backrolls")
        self.assertEqual(self.user_2.first_name, "Pookie")
        self.assertEqual(self.user_2.last_name, "MyLove")
        self.assertEqual(self.user_3.email, "pugs@puggies.com")
        self.assertEqual(self.user_3.password, "wordpass")
        self.assertEqual(self.user_3.first_name, "Puggy")
        self.assertEqual(self.user_3.last_name, "Wuggy")

    def test_type_and_subclass_hierarchy(self):
        """Test correct type and subclass hierarchy"""
        self.assertEqual(type(self.user_1), User)
        self.assertTrue(isinstance(self.user_1, User))
        self.assertTrue(issubclass(self.user_1.__class__, BaseModel))
        self.assertTrue(issubclass(self.user_1.__class__, Base))


if __name__ == "__main__":
    unittest.main()
