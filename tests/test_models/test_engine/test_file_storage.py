#!/usr/bin/python3
"""Model test for FileStorage"""

import unittest
import os
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class"""

    def setUp(self):
        self.sstorage = FileStorage()

    def test_init(self):
        """Tests that storage is an instance of FileStorage and file exists."""
        self.assertIsInstance(self.sstorage, FileStorage)
        self.assertTrue(os.path.exists("file.json"))

    @patch('models.engine.file_storage.FileStorage.save')
    def test_new_adds_object_and_saves(self, mock_save):
        """Tests that new() adds objects to __objects and calls save()."""
        user = User()
        user.name="John Doe"
        user.email="johndoe@example.com"
        self.sstorage.new(user)
        self.sstorage.save()
        expected_key = f"{user.__class__.__name__}.{user.id}"
        self.assertEqual(self.sstorage.all()[expected_key], user)
        mock_save.assert_called_once()


if __name__ == "__main__":
    unittest.main()
