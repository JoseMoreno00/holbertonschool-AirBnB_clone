#!/usr/bin/python3
"""

"""
import json
import sys


class FileStorage:
    __file_path = "data.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        json_dictionary = {}
        for k, v in self.__objects.items():
            json_dictionary[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dictionary, file, indent=4)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        classes = {
            "BaseModel":  BaseModel,
            "User": User,
            "Place": Place,
            "Review": Review,
            "State": State,
            "City": City,
            "Amenity": Amenity
        }
        try:
            with open(self.__file_path, "r") as f:
                objdict = json.load(f)
                for k, v in objdict.items():
                    self.new(classes[v["__class__"]](**v))

        except FileNotFoundError:
            pass
