from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """Test State class"""

    def setUp(self):
        """SetUp the State class"""
        self.state = State()

    def test_init(self):
        """Tests that the Test class is initialized correctly."""
        self.assertEqual(self.state.name, "")
        self.assertTrue(issubclass(State, BaseModel))

    def test_assigning(self):
        """Tests that attribute get assigned correctly."""
        name_value = "someWhere"
        self.state.name = name_value
        self.assertEqual(self.state.name, name_value)


if __name__ == '__main__':
    unittest.main()
