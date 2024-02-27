#!/usr/bin/python3
"""Tests for Place"""

import os
import unittest
import pycodestyle
from models import storage
from models.place import Place
from models.base_model import BaseModel, Base


class Test_Place(unittest.TestCase):
    """Tests for Place subclass of BaseModel"""

    @classmethod
    def setUpClass(cls):
        """Set up method to be executed before all tests"""
        cls.place_1 = Place(
            user_id="user_1",
            name="Cozy Cabin",
            description="A cozy cabin in the woods",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=150,
            latitude=40.7128,
            longitude=-74.0060,
            amenity_ids=["wifi", "kitchen"]
        )
        cls.place_2 = Place(
            user_id="user_2",
            name="Sunny Villa",
            description="A sunny villa by the beach",
            number_rooms=3,
            number_bathrooms=2,
            max_guest=6,
            price_by_night=250,
            latitude=34.0522,
            longitude=-118.2437,
            amenity_ids=["wifi", "pool"]
        )
        cls.place_3 = Place(**cls.place_1.to_dict())
        storage.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up method to be executed after all tests"""
        del cls.place_1
        del cls.place_2
        del cls.place_3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        """Test if module docstring is present"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_pycodestyle(self):
        """Test code style compliance using pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/place.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_attribute_initialization(self):
        """Test if attributes are initialized correctly"""
        self.assertEqual(type(self.place_1.user_id), str)
        self.assertEqual(type(self.place_1.name), str)
        self.assertEqual(type(self.place_1.description), str)
        self.assertEqual(type(self.place_1.number_rooms), int)
        self.assertEqual(type(self.place_1.number_bathrooms), int)
        self.assertEqual(type(self.place_1.max_guest), int)
        self.assertEqual(type(self.place_1.price_by_night), int)
        self.assertEqual(type(self.place_1.latitude), float)
        self.assertEqual(type(self.place_1.longitude), float)
        self.assertEqual(type(self.place_1.amenity_ids), list)

        self.assertEqual(type(self.place_2.user_id), str)
        self.assertEqual(type(self.place_2.name), str)
        self.assertEqual(type(self.place_2.description), str)
        self.assertEqual(type(self.place_2.number_rooms), int)
        self.assertEqual(type(self.place_2.number_bathrooms), int)
        self.assertEqual(type(self.place_2.max_guest), int)
        self.assertEqual(type(self.place_2.price_by_night), int)
        self.assertEqual(type(self.place_2.latitude), float)
        self.assertEqual(type(self.place_2.longitude), float)
        self.assertEqual(type(self.place_2.amenity_ids), list)

        self.assertEqual(type(self.place_3.user_id), str)
        self.assertEqual(type(self.place_3.name), str)
        self.assertEqual(type(self.place_3.description), str)
        self.assertEqual(type(self.place_3.number_rooms), int)
        self.assertEqual(type(self.place_3.number_bathrooms), int)
        self.assertEqual(type(self.place_3.max_guest), int)
        self.assertEqual(type(self.place_3.price_by_night), int)
        self.assertEqual(type(self.place_3.latitude), float)
        self.assertEqual(type(self.place_3.longitude), float)
        self.assertEqual(type(self.place_3.amenity_ids), list)

    def test_type_subclass(self):
        """Test correct type and subclass"""
        self.assertEqual(type(self.place_1), Place)
        self.assertTrue(isinstance(self.place_1, Place))
        self.assertTrue(issubclass(self.place_1.__class__, BaseModel))
        self.assertTrue(issubclass(self.place_1.__class__, Base))


if __name__ == "__main__":
    unittest.main()

