#!/usr/bin/python3
""" Tests for file storage """
import os
import unittest
from models import storage
from genericpath import exists
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


@unittest.skipIf(os.getenv("HBNB_ENV") != "file", 'FileStorage inactive')
class TestFileStorageInitialization(unittest.TestCase):
    """ Tests for FileStorage class initialization """

    def test_documentation(self):
        """ Ensures all necessary docstrings are present """
        self.assertTrue(len(FileStorage.__doc__) > 0)
        self.assertTrue(len(FileStorage.all.__doc__) > 0)
        self.assertTrue(len(FileStorage.new.__doc__) > 0)
        self.assertTrue(len(FileStorage.save.__doc__) > 0)
        self.assertTrue(len(FileStorage.reload.__doc__) > 0)
        self.assertTrue(len(FileStorage.delete.__doc__) > 0)

    def test_code_style(self):
        """ Checks code style compliance with PEP 8 """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/engine/file_storage.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_invalid_argument(self):
        """ Verifies TypeError is raised when an argument is supplied """
        with self.assertRaises(TypeError):
            FileStorage(1)

    def test_private_attributes(self):
        """ Tests types and privacy of class attributes """
        self.assertTrue(type(storage._FileStorage__file_path) is str)
        self.assertTrue(type(storage._FileStorage__objects) is dict)
        with self.assertRaises(AttributeError):
            print(storage.__objects)
            print(storage.__file_path)


@unittest.skipIf(os.getenv("HBNB_ENV") != "file", 'FileStorage inactive')
class TestFileStorageAllMethod(unittest.TestCase):
    """ Tests for FileStorage all method """

    @classmethod
    def setUpClass(cls):
        """ Sets up objects for testing """
        cls.obj = BaseModel()
        cls.obj.save()

    @classmethod
    def tearDownClass(cls):
        """ Cleans up after testing """
        del cls.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_all(self):
        """ Checks correct operation of all method """
        self.assertTrue(self.obj, exists)
        self.assertIn(
            f'{self.obj.__class__.__name__}.{self.obj.id}',
            storage.all()
        )
        self.assertTrue(type(storage.all()) is dict)
        self.assertTrue(len(storage.all()) > 0)


@unittest.skipIf(os.getenv("HBNB_ENV") != "file", 'FileStorage inactive')
class TestFileStorageNewMethod(unittest.TestCase):
    """ Tests for FileStorage new method """

    @classmethod
    def setUpClass(cls):
        """ Sets up objects for testing """
        cls.obj = BaseModel()
        cls.obj.save()

    @classmethod
    def tearDownClass(cls):
        """ Cleans up after testing """
        del cls.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_new(self):
        """ Checks correct operation of new method """
        storage.new(self.obj)
        self.assertIn(
            f'{self.obj.__class__.__name__}.{self.obj.id}',
            storage._FileStorage__objects
        )
        self.assertIn(self.obj, storage.all().values())

    def test_invalid_arguments(self):
        """ Verifies exceptions are raised with invalid arguments """
        with self.assertRaises(TypeError):
            storage.new(self.obj, 6)
        with self.assertRaises(AttributeError):
            storage.new(8)
            storage.new({2, 4, 8})


@unittest.skipIf(os.getenv("HBNB_ENV") != "file", 'FileStorage inactive')
class TestFileStorageSaveMethod(unittest.TestCase):
    """ Tests for FileStorage save method """

    @classmethod
    def setUpClass(cls):
        """ Sets up objects for testing """
        cls.obj = BaseModel()
        cls.obj.save()

    @classmethod
    def tearDownClass(cls):
        """ Cleans up after testing """
        del cls.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save(self):
        """ Checks correct operation of save method """
        self.obj.save()
        self.assertTrue(os.path.exists('file.json'))
        with open("file.json") as file:
            content = file.read()
            self.assertIn(
                f"{self.obj.__class__.__name__}.{self.obj.id}",
                content
            )
            self.assertTrue(len(content) > 0)

    def test_invalid_arguments(self):
        """ Verifies exceptions are raised with invalid arguments """
        with self.assertRaises(TypeError):
            storage.save(1)
            self.obj.save(1)


@unittest.skipIf(os.getenv("HBNB_ENV") != "file", 'FileStorage inactive')
class TestFileStorageReloadMethod(unittest.TestCase):
    """ Tests for FileStorage reload method """

    def test_reload(self):
        """ Checks correct operation of reload method """
        obj = BaseModel()
        obj.save()
        storage.reload()
        self.assertIn(
            f'{obj.__class__.__name__}.{obj.id}',
            storage._FileStorage__objects
        )
        self.assertTrue(len(storage.all()) > 0)
        del obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_invalid_arguments(self):
        """ Verifies exceptions are raised with invalid arguments """
        with self.assertRaises(TypeError):
            storage.reload(1)


@unittest.skipIf(os.getenv("HBNB_ENV") != "file", 'FileStorage inactive')
class TestFileStorageDeleteMethod(unittest.TestCase):
    """ Tests for FileStorage delete method """

    @classmethod
    def setUpClass(cls):
        """ Sets up objects for testing """
        cls.obj = BaseModel()
        cls.obj.save()
        cls.obj_to_delete = BaseModel()
        cls.obj_to_delete.save()

    @classmethod
    def tearDownClass(cls):
        """ Cleans up after testing """
        del cls.obj
        del cls.obj_to_delete
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_delete(self):
        """ Checks correct operation of delete method """
        initial_state = storage.all().copy()
        obj_id = f'{self.obj_to_delete.__class__.__name__}.{self.obj_to_delete.id}'
        self.assertEqual(initial_state, storage.all())
        self.assertIn(obj_id, storage.all())
        storage.delete(self.obj_to_delete)
        self.assertNotEqual(initial_state, storage.all())
        self.assertNotIn(obj_id, storage.all())


if __name__ == "__main__":
    unittest.main()
