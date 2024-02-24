#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

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
            if isinstance(cls, str):
                cls = getattr(models, cls, None)

            # If cls is not None after conversion, filter objects by cls type
            if cls is not None:
                return {
                    obj for obj in self.__objects.items()
                    if isinstance(obj, cls)
                }
            else:
                # If cls is None after conversion, return an empty dictionary
                return {}

        # If cls is None, return list
        return list(self.__objects.values())

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
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
