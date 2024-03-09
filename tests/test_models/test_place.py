#!/usr/bin/python3
"""Model test for Place"""

from models.place import Place
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """Test Place class"""

    def setUp(self):
        """SetUp the Place class"""
        self.place = Place()
        self.user = User()
        self.city = City()
        self.amenity = Amenity()

    def test_init(self):
        """Tests that the Place class is initialized correctly."""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_assigning(self):
        """Tests that attribute get assigned correctly."""
        city_id_value = self.city.id
        user_id_value = self.user.id
        name_value = "name_value"
        description_value = "<@@##$$"
        number_rooms_value = 201
        number_bathrooms_value = 45
        max_guest_value = 4656
        price_by_night_value = 234
        latitude_value = 23.605
        longitude_value = 34.857
        amenity_ids_value = [self.amenity.id]

        self.place.city_id = city_id_value
        self.place.user_id = user_id_value
        self.place.name = name_value
        self.place.description = description_value
        self.place.number_rooms = number_rooms_value
        self.place.number_bathrooms = number_bathrooms_value
        self.place.max_guest = max_guest_value
        self.place.price_by_night = price_by_night_value
        self.place.latitude = latitude_value
        self.place.longitude = longitude_value
        self.place.amenity_ids = amenity_ids_value

        self.assertEqual(self.place.city_id, city_id_value)
        self.assertEqual(self.place.user_id, user_id_value)
        self.assertEqual(self.place.name, name_value)
        self.assertEqual(self.place.description, description_value)
        self.assertEqual(self.place.number_rooms, number_rooms_value)
        self.assertEqual(self.place.max_guest, max_guest_value)
        self.assertEqual(self.place.price_by_night, price_by_night_value)
        self.assertEqual(self.place.latitude, latitude_value)
        self.assertEqual(self.place.longitude, longitude_value)
        self.assertEqual(self.place.amenity_ids, amenity_ids_value)


if __name__ == '__main__':
    unittest.main()
