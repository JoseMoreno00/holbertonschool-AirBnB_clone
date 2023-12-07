#!/usr/bin/python3
"""Class Amenity"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class that inherits from BaseModel class"""
    place_id = ""
    user_id = ""
    text = ""
