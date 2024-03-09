#!/usr/bin/python3
"""Model test for BaseModel"""

import unittest
import uuid
from datetime import datetime, timedelta
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def test_init(self):
        """Tests initialization of attributes."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertTrue(uuid.UUID(model.id))
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_valid_datetime_kwargs(self):
        """Tests initialization with valid datetime keyword arguments."""
        now = datetime.now()
        past_time = now - timedelta(days=1)
        future_time = now + timedelta(days=1)
        kwargs = {
            "created_at": past_time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "updated_at": future_time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.created_at, past_time)
        self.assertEqual(model.updated_at, future_time)

    def test_init_with_invalid_datetime_format(self):
        """Tests initialization with invalid datetime format in kwargs."""
        invalid_kwargs = {"created_at": "invalid_date_format"}
        with self.assertRaises(ValueError):
            BaseModel(**invalid_kwargs)

    def test_str(self):
        """Tests string representation."""
        model = BaseModel()
        expected_str = (
            f"[{model.__class__.__name__}]"
            f"({model.id}) {model.__dict__}"
        )
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """Tests updating updated_at timestamp."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Tests conversion to dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], model.__class__.__name__)
        self.assertEqual(model_dict['id'], model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertTrue(all(
            field in model_dict for field in ['id', 'created_at', 'updated_at']
        ))


if __name__ == '__main__':
    unittest.main()
