#!/usr/bin/python3
"""Unit tests for the City module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from datetime import datetime

ct1 = City()
ct2 = City(**ct1.to_dict())
ct3 = City("hello", "wait", "in")


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""
        km = f"{type(ct1).__name__}.{ct1.id}"
        self.assertIsInstance(ct1.name, str)
        self.assertEqual(ct3.name, "")
        ct1.name = "Cairo"
        self.assertEqual(ct1.name, "Cairo")

    def test_init(self):
        """Test method for public instances"""
        self.assertIsInstance(ct1.id, str)
        self.assertIsInstance(ct1.created_at, datetime)
        self.assertIsInstance(ct1.updated_at, datetime)
        self.assertEqual(ct1.updated_at, ct2.updated_at)

    def test_save(self):
        """Test method for save"""
        old_update = ct1.updated_at
        ct1.save()
        self.assertNotEqual(ct1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        a_dict = ct2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict["__class__"], type(ct2).__name__)
        self.assertIn("created_at", a_dict.keys())
        self.assertIn("updated_at", a_dict.keys())
        self.assertNotEqual(ct1, ct2)


if __name__ == "__main__":
    unittest.main()
