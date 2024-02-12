#!/usr/bin/python3
"""Unit tests for the Review module.
"""
import os
import unittest
from models.review import Review
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test cases for the `Review` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        rv1 = Review()
        rv3 = Review("hello", "wait", "in")
        km = f"{type(rv1).__name__}.{rv1.id}"
        self.assertIsInstance(rv1.text, str)
        self.assertIsInstance(rv1.id, str)
        self.assertIsInstance(rv1.place_id, str)
        self.assertEqual(rv3.text, "")

    def test_init(self):
        """Test method for public instances"""
        rv1 = Review()
        rv2 = Review(**rv1.to_dict())
        self.assertIsInstance(rv1.id, str)
        self.assertIsInstance(rv1.created_at, datetime)
        self.assertIsInstance(rv1.updated_at, datetime)
        self.assertEqual(rv1.updated_at, rv2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        rv1 = Review()
        string = f"[{type(rv1).__name__}] ({rv1.id}) {rv1.__dict__}"
        self.assertEqual(rv1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        rv1 = Review()
        old_update = rv1.updated_at
        rv1.save()
        self.assertNotEqual(rv1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        rv1 = Review()
        rv2 = Review(**rv1.to_dict())
        a_dict = rv2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict["__class__"], type(rv2).__name__)
        self.assertIn("created_at", a_dict.keys())
        self.assertIn("updated_at", a_dict.keys())
        self.assertNotEqual(rv1, rv2)


if __name__ == "__main__":
    unittest.main()
