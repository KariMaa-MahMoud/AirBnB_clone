#!/usr/bin/python3
"""Unit tests for the State module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for the `State` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        st1 = State()
        st3 = State("hello", "wait", "in")

        km = f"{type(st1).__name__}.{st1.id}"
        self.assertIsInstance(st1.name, str)
        self.assertEqual(st3.name, "")
        st1.name = "Chicago"
        self.assertEqual(st1.name, "Chicago")
        self.assertIn(km, storage.all())

    def test_init(self):
        """Test method for public instances"""
        st1 = State()
        st2 = State(**st1.to_dict())
        self.assertIsInstance(st1.id, str)
        self.assertIsInstance(st1.created_at, datetime)
        self.assertIsInstance(st1.updated_at, datetime)
        self.assertEqual(st1.updated_at, st2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        st1 = State()
        string = f"[{type(st1).__name__}] ({st1.id}) {st1.__dict__}"
        self.assertEqual(st1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        st1 = State()
        old_update = st1.updated_at
        st1.save()
        self.assertNotEqual(st1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        st1 = State()
        st2 = State(**st1.to_dict())
        a_dict = st2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict["__class__"], type(st2).__name__)
        self.assertIn("created_at", a_dict.keys())
        self.assertIn("updated_at", a_dict.keys())
        self.assertNotEqual(st1, st2)


if __name__ == "__main__":
    unittest.main()
