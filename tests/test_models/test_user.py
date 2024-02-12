#!/usr/bin/python3
"""Unit tests for the User module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for the `User` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        us1 = User()
        km = f"{type(us1).__name__}.{us1.id}"
        self.assertIn(km, storage.all())
        self.assertIsInstance(us1.email, str)
        self.assertIsInstance(us1.password, str)
        self.assertIsInstance(us1.first_name, str)
        self.assertIsInstance(us1.last_name, str)

    def test_init(self):
        """Test method for public instances"""
        us1 = User()
        us2 = User(**us1.to_dict())
        self.assertIsInstance(us1.id, str)
        self.assertIsInstance(us1.created_at, datetime)
        self.assertIsInstance(us1.updated_at, datetime)
        self.assertEqual(us1.updated_at, us2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        us1 = User()
        string = f"[{type(us1).__name__}] ({us1.id}) {us1.__dict__}"
        self.assertEqual(us1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        us1 = User()
        old_update = us1.updated_at
        us1.save()
        self.assertNotEqual(us1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        us1 = User()
        us2 = User(**us1.to_dict())
        a_dict = us2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict["__class__"], type(us2).__name__)
        self.assertIn("created_at", a_dict.keys())
        self.assertIn("updated_at", a_dict.keys())
        self.assertNotEqual(us1, us2)


if __name__ == "__main__":
    unittest.main()
