#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User



class FileStorage:
    __file_path = "json_file"
    __objects = {}
    def all(self):
        """
        Returns a list of all objects in the storage.

        Returns:
        list: A list of all objects in the storage.
        """
        return type(self).__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
        obj (object): The object to add.

        Returns:
        None

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        """
        return FileStorage.__objects
        
    def save(self):
        """serializes __objects to the JSON file"""
        all_obj = FileStorage.__objects
        serialized = {}
        for obj in all_obj.keys():
            serialized[obj] = all_obj[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized, f)

                
        
      
    def reload(self):
        """deserializes the JSON file to __objects(Only if the JSON file
            (__file_path)exists; otherwise, does nothing. if the file doesn't exist
            no exception is raised)"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r', encoding="UTF-8") as f:
                try:
                    data = json.load(f)
                    for key, value in data.items():
                        class_name, obj_id = key.split(".")
                        cls = eval(class_name)
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                except FileNotFoundError:
                    pass
