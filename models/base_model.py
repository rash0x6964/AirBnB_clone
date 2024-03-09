#!/usr/bin/python3
"""A model that represents a base class for all the other classes"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class holdes all the common
        attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value,
                        "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return (
            f"[{self.__class__.__name__}] "
            f"({self.id}) {self.__dict__}"
        )

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """a dictionary containing all keys/values of __dict__"""
        tmpDict = {}
        for key, value in self.__dict__.items():
            if (key in ["updated_at", "created_at"]):
                tmpDict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                tmpDict[key] = value
        tmpDict["__class__"] = self.__class__.__name__
        return tmpDict
