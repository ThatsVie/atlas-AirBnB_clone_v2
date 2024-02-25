#!/usr/bin/python3
"""Tests for the State model"""

import os
import unittest
import pycodestyle
from models import storage
from models.state import State
from models.base_model import BaseModel, Base


class TestStateModel(unittest.TestCase):
    """Tests for the State model subclass of BaseModel"""

    @classmethod
    def setUpClass(cls):
        """Set up method to be executed before each test"""
        cls.state_1 = State(name="California")
        cls.state_2 = State(name="Nevada")
        cls.state_3 = State(**cls.state_1.to_dict())
        storage.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up method to be executed following all tests"""
        del cls.state_1
        del cls.state_2
        del cls.state_3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_module_docstring_exists(self):
        """Test if module docstring is present"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_pycodestyle_compliance(self):
        """Test code style compliance using pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/state.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_attribute_initialization(self):
        """Test attributes initialized with correct value & type"""
        self.assertEqual(type(self.state_1.name), str)
        self.assertEqual(type(self.state_2.name), str)
        self.assertEqual(type(self.state_3.name), str)
        self.assertEqual(self.state_1.name, "California")
        self.assertEqual(self.state_2.name, "Nevada")
        self.assertEqual(self.state_3.name, "California")

    def test_type_and_subclass_hierarchy(self):
        """Test correct type and subclass hierarchy"""
        self.assertEqual(type(self.state_1), State)
        self.assertTrue(isinstance(self.state_1, State))
        self.assertTrue(issubclass(self.state_1.__class__, BaseModel))
        self.assertTrue(issubclass(self.state_1.__class__, Base))


if __name__ == "__main__":
    unittest.main()

