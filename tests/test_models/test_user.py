#!/usr/bin/python3
"""Model test for User"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test User class"""

    def setUp(self):
        """setUp the User class"""
        self.user = User()

    def test_init(self):
        """Tests that the User class is initialized correctly."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_assigning(self):
        """Tests that attribute get assigned correctly."""
        first_name_val = "rash"
        last_name_value = "0x11"
        email_value = "rash@gmail.com"
        password_value = "xf33434fg"

        self.user.first_name = first_name_val
        self.user.last_name = last_name_value
        self.user.email = email_value
        self.user.password = password_value

        self.assertEqual(self.user.email, email_value)
        self.assertEqual(self.user.password, password_value)
        self.assertEqual(self.user.first_name, first_name_val)
        self.assertEqual(self.user.last_name, last_name_value)


if __name__ == "__main__":
    unittest.main()
