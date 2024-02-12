#!/usr/bin/python3
"""Unit tests for the Amenity module.
"""
import os
import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Test cases for the `Amenity` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        am1 = Amenity()
        am2 = Amenity(**am1.to_dict())
        am3 = Amenity("hello", "wait", "in")

        km = f"{type(am1).__name__}.{am1.id}"
        self.assertIsInstance(am1.name, str)
        self.assertIn(km, storage.all())
        self.assertEqual(am3.name, "")

    def test_init(self):
        """Test method for public instances"""
        am1 = Amenity()
        am2 = Amenity(**am1.to_dict())
        self.assertIsInstance(am1.id, str)
        self.assertIsInstance(am1.created_at, datetime)
        self.assertIsInstance(am1.updated_at, datetime)
        self.assertEqual(am1.updated_at, am2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        am1 = Amenity()
        string = f"[{type(am1).__name__}] ({am1.id}) {am1.__dict__}"
        self.assertEqual(am1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        am1 = Amenity()
        old_update = am1.updated_at
        am1.save()
        self.assertNotEqual(am1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        am1 = Amenity()
        am2 = Amenity(**am1.to_dict())
        am_dict = am2.to_dict()
        self.assertIsInstance(am_dict, dict)
        self.assertEqual(am_dict["__class__"], type(am2).__name__)
        self.assertIn("created_at", am_dict.keys())
        self.assertIn("updated_at", am_dict.keys())
        self.assertNotEqual(am1, am2)


if __name__ == "__main__":
    unittest.main()
