#!/usr/bin/python3
"""A model that contain a Filestorage class to save
    and load data from JSON file
"""

import json
import os
from ..base_model import BaseModel


class FileStorage:
    """FileStorage class that serializes instances
        to a JSON file and deserializes JSON file
        to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__}.{obj.id}"] = obj

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
                tmp_dict = json.loads(f.read())
                for obj in tmp_dict.values():
                    name = obj["__class__"]
                    self.new(globals()[name](**obj))
