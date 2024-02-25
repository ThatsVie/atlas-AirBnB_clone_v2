#!/usr/bin/python3
"""Tests for Amenity"""
import os
import unittest
import pycodestyle
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base


class Test_Amenity(unittest.TestCase):
    """ Tests for Amenity subclass of BaseModel"""
    @classmethod
    def setUpClass(cls):
        """ Preparation method before all tests """
        cls.amenity1 = Amenity(name='chew_toy')
        cls.amenity2 = Amenity(name='pug_bed')
        cls.amenity3 = Amenity(**cls.amenity1.to_dict())
        storage.save()

    @classmethod
    def tearDownClass(cls):
        """ Cleanup method after all tests """
        del cls.amenity1
        del cls.amenity2
        del cls.amenity3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_amenity_docstring(self):
        """ Tests module docstring for amenities """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_pycodestyle(self):
        """ Tests PEP 8 compliance for amenity module """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/amenity.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_amenity_attribute_initialization(self):
        """ Test attributes initialized """
        self.assertEqual(type(self.amenity1.name), str)
        self.assertEqual(type(self.amenity2.name), str)
        self.assertEqual(type(self.amenity3.name), str)
        self.assertEqual(self.amenity1.name, "chew_toy")
        self.assertEqual(self.amenity2.name, "pug_bed")
        self.assertEqual(self.amenity3.name, "chew_toy")

    def test_amenity_type_subclass(self):
        """ Tests correct type and subclass """
        self.assertEqual(type(self.amenity1), Amenity)
        self.assertTrue(isinstance(self.amenity1, Amenity))
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel))
        self.assertTrue(issubclass(self.amenity1.__class__, Base))


if __name__ == "__main__":
    unittest.main()
