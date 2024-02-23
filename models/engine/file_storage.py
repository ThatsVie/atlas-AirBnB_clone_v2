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
    Returns a dictionary of models currently in storage.
    
    Args:
        cls (class or str): The class type or class name to filter objects. If None, returns all objects.
   
    """
    # Check if the cls argument is provided (i.e., not None).
    if cls is not None:
        # Check if the type of cls is a string.
        if type(cls) is str:
            # If cls is a string, attempts to retrieve the corresponding class object from the classes dictionary.
            cls = classes.get(cls)
        # Initializes an empty dictionary to store the filtered objects.
        obj_dict = {}
        # Iterates over the key-value pairs in the __objects dictionary.
        for key, value in self.__objects.items():
            # Checks if the type of the value matches the specified class type (cls).
            if type(value) is cls:
                # If the value's type matches the specified class type, adds the key-value pair to the obj_dict dictionary.
                obj_dict[key] = value
        # Returns the dictionary containing the filtered objects.
        return obj_dict
    else:
        # If cls is None, indicating no filtering is requested, returns the entire dictionary of objects
        # stored in the __objects attribute of the FileStorage class.
        return FileStorage.__objects

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
