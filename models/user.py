#!/usr/bin/python3
"""Class Amenity"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that inherits from BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
