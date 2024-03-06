#!/usr/bin/python3
"""A module define a City class"""

from .base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel"""

    state_id = ""
    name = ""
