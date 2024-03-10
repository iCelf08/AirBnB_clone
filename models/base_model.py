#!/usr/bin/python3
"""
Module for storage
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    Base class for all models
    """
    def __init__(self, *args, **kwargs):
        """
        constructor
        """
        
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def save(self):
        """
        save updates to the storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary representation of the object
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
        

    def __str__(self):
        """
        string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__) 
