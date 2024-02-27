#!/usr/bin/python3
"""Unit tests for the Review model"""

import os
import unittest
import pycodestyle
from models import storage
from models.review import Review
from models.base_model import BaseModel, Base


class TestReviewModel(unittest.TestCase):
    """Tests for the Review model, which is a subclass of BaseModel"""

    @classmethod
    def setUp(cls):
        """Set up method to prepare for each test"""
        cls.review_1 = Review(
            place_id="unique_place_id_1",
            user_id="unique_user_id_1",
            text="This is a review text."
        )
        cls.review_2 = Review(
            place_id="unique_place_id_2",
            user_id="unique_user_id_2",
            text="Another review text."
        )
        cls.review_3 = Review(**cls.review_1.to_dict())
        storage.save()

    @classmethod
    def tearDown(cls):
        """Clean up method to be executed after each test"""
        del cls.review_1
        del cls.review_2
        del cls.review_3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_module_docstring_exists(self):
        """Test if module docstring exists"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_pycodestyle_compliance(self):
        """Test code style compliance using pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/review.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_attribute_initialization(self):
        """Test if attributes are initialized correctly"""
        self.assertEqual(type(self.review_1.place_id), str)
        self.assertEqual(type(self.review_1.user_id), str)
        self.assertEqual(type(self.review_1.text), str)
        self.assertEqual(type(self.review_2.place_id), str)
        self.assertEqual(type(self.review_2.user_id), str)
        self.assertEqual(type(self.review_2.text), str)
        self.assertEqual(type(self.review_3.place_id), str)
        self.assertEqual(type(self.review_3.user_id), str)
        self.assertEqual(type(self.review_3.text), str)
        self.assertEqual(self.review_1.place_id, "unique_place_id_1")
        self.assertEqual(self.review_1.user_id, "unique_user_id_1")
        self.assertEqual(self.review_1.text, "This is a review text.")
        self.assertEqual(self.review_2.place_id, "unique_place_id_2")
        self.assertEqual(self.review_2.user_id, "unique_user_id_2")
        self.assertEqual(self.review_2.text, "Another review text.")
        self.assertEqual(self.review_3.place_id, "unique_place_id_1")
        self.assertEqual(self.review_3.user_id, "unique_user_id_1")
        self.assertEqual(self.review_3.text, "This is a review text.")

    def test_type_and_subclass_hierarchy(self):
        """Test correct type and subclass hierarchy"""
        self.assertEqual(type(self.review_1), Review)
        self.assertTrue(isinstance(self.review_1, Review))
        self.assertTrue(issubclass(self.review_1.__class__, BaseModel))
        self.assertTrue(issubclass(self.review_1.__class__, Base))


if __name__ == "__main__":
    unittest.main()
