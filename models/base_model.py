#!/usr/bin/python3
"""
    Define a class

    [BaseModel]: class that define all attributes and methods for other class
        Public Instances:
            Id: This instance save a unique id when the an instance is created
            Created_at: assign with the current datetime when an instance
                        is created.
            Update_at: assign with the current datetime when an instance is
            created and it will be updated every time you change your object

"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class: define all attributes and methods"""
    def __init__(self, *args, **kwargs):
        typefrmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        v = datetime.strptime(v, typefrmt)
                    setattr(self, k, v)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Method __str__ that print a string"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance:"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
