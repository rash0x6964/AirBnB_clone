#!/usr/bin/python3
"""Model test for Review"""

from models.review import Review
from models.place import Place
from models.user import User
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    """Test Review class"""

    def setUp(self):
        """SetUp the Review class"""
        self.review = Review()
        self.user = User()
        self.place = Place()

    def test_init(self):
        """Tests that the Review class is initialized correctly."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_assigning(self):
        """Tests that attribute get assigned correctly."""
        place_id_value = self.place.id
        user_id_value = self.user.id
        text_value = "<3 <3 ^^"

        self.review.place_id = place_id_value
        self.review.user_id = user_id_value
        self.review.text = text_value

        self.assertEqual(self.review.place_id, place_id_value)
        self.assertEqual(self.review.user_id, user_id_value)
        self.assertEqual(self.review.text, text_value)


if __name__ == '__main__':
    unittest.main()
