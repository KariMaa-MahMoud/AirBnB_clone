#!/usr/bin/python3
"""Testing the BaseModel module."""

import json
import os
import time
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization_positive(self):
        """Test passing cases BaseModel initialization."""
        bm1 = BaseModel()
        bm2_uuid = str(uuid.uuid4())
        bm2 = BaseModel(id=bm2_uuid, name="The weeknd", album="Trilogy")
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)
        self.assertEqual(bm_uuid, bm2.id)
        self.assertEqual(bm2.album, "Trilogy")
        self.assertEqual(bm2.name, "The weeknd")
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertEqual(str(type(bm1)), "<class 'models.base_model.BaseModel'>")

    def test_dict(self):
        """Test method for dict"""
        bm1 = BaseModel()
        bm2_uuid = str(uuid.uuid4())
        bm2 = BaseModel(id=bm2_uuid, name="The weeknd", album="Trilogy")
        bm1_dict = bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        self.assertIn("id", bm1_dict.keys())
        self.assertIn("created_at", bm1_dict.keys())
        self.assertIn("updated_at", bm1_dict.keys())
        self.assertEqual(bm1_dict["__class__"], type(bm1).__name__)
        with self.assertRaises(KeyError) as e:
            bm2.to_dict()

    def test_save(self):
        """Test method for save"""
        bm = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        bm.save()
        diff = bm.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_save_storage(self):
        """Tests that storage.save() is called from save()."""
        bm = BaseModel()
        bm.save()
        key = "{}.{}".format(type(bm).__name__, bm.id)
        d = {key: bm.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        message_error = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), message_error)

    def test_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        message_error = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), message_error)

    def test_str(self):
        """Test method for str representation"""
        bm1 = BaseModel()
        string = f"[{type(bm1).__name__}] ({bm1.id}) {bm1.__dict__}"
        self.assertEqual(bm1.__str__(), string)


if __name__ == "__main__":
    unittest.main()
