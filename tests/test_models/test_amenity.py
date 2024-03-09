import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def test_init(self):
        """Tests that the Amenity class is initialized correctly."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_assigning(self):
        """Tests that attribute get assigned correctly."""
        amenity = Amenity()
        amenity.name = "Wi-Fi"
        self.assertEqual(amenity.name, "Wi-Fi")


if __name__ == "__main__":
    unittest.main()
