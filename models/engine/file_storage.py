#!/usr/bin/python3
"""A model that contain a Filestorage class to save
    and load data from JSON file
"""

import os
import json
from ..user import User
from ..city import City
from ..place import Place
from ..state import State
from ..review import Review
from ..amenity import Amenity
from ..base_model import BaseModel


class FileStorage:
    """FileStorage class that serializes instances
        to a JSON file and deserializes JSON file
        to instances.
    """

    __file_path = "file.json"
    __objects = {}
    supportedClss = {
        "BaseModel": BaseModel, "User": User, "Place": Place,
        "State": State, "City": City, "Amenity": Amenity,
        "Review": Review
    }

    def __init__(self):
        pass

    def all(self):
        """return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        tmp_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(tmp_dict))

    def reload(self):
        """deserializes the JSON file to __objects"""
        fileName = FileStorage.__file_path
        if os.path.exists(fileName):
            with open(fileName, mode="r", encoding="utf-8") as f:
                res = f.read()
                res = "{}" if len(res) == 0 else res
                tmp_dict = json.loads(res)
                for obj in tmp_dict.values():
                    cls = obj["__class__"]
                    self.new(FileStorage.supportedClss[cls](**obj))
