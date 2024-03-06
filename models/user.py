#!/usr/bin/python3
"""A module define a user class"""

from .base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
