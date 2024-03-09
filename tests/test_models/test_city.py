from models.city import City
from models.state import State
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """Test city class"""

    def setUp(self):
        """method that setUp the city"""
        self.state = State()
        self.city = City()

    def test_init(self):
        """Tests that the City class is initialized correctly."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_assigning(self):
        """Tests that attribute get assigned correctly."""
        self.city.state_id = self.state.id
        self.city.name = "someWhere"
        
        self.assertEqual(self.city.state_id, self.state.id)
        self.assertEqual(self.city.name , "someWhere")


if __name__ == '__main__':
    unittest.main()
