
import json
import os
from models.base_model import BaseModel

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
        type(self).__objects[key] = obj

   
    def save(self):
        """serializes __objects to the JSON file"""
        serialized = []
        for obj in type(self).__objects.values():
            serialized.append(obj.to_dict())
        with open(type(self).__file_path, mode='w', encoding="UTF-8") as j_f:
            json.dump(serialized, j_f)

                
      
    def reload(self):
        """deserializes the JSON file to __objects(Only if the JSON file
            (__file_path)exists; otherwise, does nothing. if the file doesn't exist
            no exception is raised)"""
        if os.path.exists(type(self).__file_path) is True:
            try:
                with open(type(self).__file_path, mode='r', encoding="UTF-8") as f:
                    data = json.load(f)
                for key, value in data.items():
                    obj = self.class_dict[value['__class__']](**value)
                    type(self).__objects[key] = obj
            except FileNotFoundError:
                pass