#!/usr/bin/python3
"""A module define a Review class"""

from .base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
