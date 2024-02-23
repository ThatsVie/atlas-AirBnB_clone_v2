#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}
class FileStorage:
    """This class manages storage of models in JSON format"""

    # Define class attributes
    __file_path = 'file.json'  # File path to store JSON data
    __objects = {}  # Dictionary to store model objects

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage,
        can also filter by class type

        Args:
        cls (class or str): The class type or class name to filter objects.
        If None, returns all objects
        """
        # If cls is not None, filter objects by class type
        if cls is not None:
            # If cls is a string, convert it to a class object using getattr
            cls = getattr(models, cls, None)
            # If cls is not None after conversion, filter objects by cls type
            if cls is not None:
                return {
                    obj_id: obj
                    for obj_id, obj in self.__objects.items()
                    if isinstance(obj, cls)
                }
            else:
                # If cls is None after conversion, return an empty dictionary
                return {}

        # If cls is None, return all objects without filtering
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it's inside.

        Args:
        obj: object to be deleted from storage. If None, no action is taken.

        Returns: None
        """
        # Ensure obj is not None
        if obj is not None:
            # Create the key to locate the object in the storage dictionary
            key = f"{type(obj).__name__}.{obj.id}"
            # Check if the key exists in the storage dictionary
            if key in self.__objects:
                # If the key exists, delete object from the storage dictionary
                del self.__objects[key]
