#!/usr/bin/python3
"""Tests for City model"""

import os
import unittest
import pycodestyle
from models import storage
from models.city import City
from models.base_model import BaseModel, Base


class TestCityModel(unittest.TestCase):
    """Tests for the City model, which is a subclass of BaseModel"""

    @classmethod
    def setUpClass(cls):
        """Set up method"""
        cls.city_1 = City(name="NYC", state_id="PugUUID4")
        cls.city_2 = City(name="LA", state_id="WugUUID4")
        cls.city_3 = City(**cls.city_1.to_dict())
        storage.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up method """
        del cls.city_1
        del cls.city_2
        del cls.city_3
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_module_docstring(self):
        """Test if module docstring is present"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_pycodestyle_compliance(self):
        """Test code style compliance using pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/city.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_attribute_initialization(self):
        """Test if attributes are initialized correctly"""
        self.assertEqual(type(self.city_1.state_id), str)
        self.assertEqual(type(self.city_1.name), str)
        self.assertEqual(type(self.city_2.state_id), str)
        self.assertEqual(type(self.city_2.name), str)
        self.assertEqual(type(self.city_3.state_id), str)
        self.assertEqual(type(self.city_3.name), str)
        self.assertEqual(self.city_1.state_id, "PugUUID4")
        self.assertEqual(self.city_1.name, "NYC")
        self.assertEqual(self.city_2.state_id, "WugUUID4")
        self.assertEqual(self.city_2.name, "LA")
        self.assertEqual(self.city_3.state_id, "PugUUID4")
        self.assertEqual(self.city_3.name, "NYC")

    def test_type_subclass(self):
        """Test correct type and subclass"""
        self.assertEqual(type(self.city_1), City)
        self.assertTrue(isinstance(self.city_1, City))
        self.assertTrue(issubclass(self.city_1.__class__, BaseModel))
        self.assertTrue(issubclass(self.city_1.__class__, Base))


if __name__ == "__main__":
    unittest.main()
