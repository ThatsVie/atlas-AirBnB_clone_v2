#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


# Check the value of the HBNB_TYPE_STORAGE environment variable
if getenv("HBNB_TYPE_STORAGE") == "db":
    # If it's "db", import and instantiate DBStorage
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()  # Load data from the database storage
else:
    # If it's not "db", import and instantiate FileStorage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()  # Load data from the file storage
