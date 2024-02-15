"""Defines unittests for base.py."""
import unittest
import os
import json
from models import Base

class TestBase(unittest.TestCase):
    """
    Unittests for testing instantiation of the Base class.
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = {"id": 9, "width": 10, "height": 11, "x": 12, "y": 13}
        self.assertEqual(Base.to_json_string([d]), '[{"id": 9, "width": 10, "height": 11, "x": 12, "y": 13}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        json_str = '[{"id": 9, "width": 10, "height": 11, "x": 12, "y": 13}]'
        self.assertEqual(Base.from_json_string(json_str), [{"id": 9, "width": 10, "height": 11, "x": 12, "y": 13}])

    def test_save_to_file(self):
        b1 = Base(1)
        Base.save_to_file([b1])
        with open("Base.json", "r") as file:
            self.assertEqual([b1.to_dictionary()], json.load(file))

    def test_create(self):
        b1 = Base(1)
        b1_dict = b1.to_dictionary()
        b2 = Base.create(**b1_dict)
        self.assertEqual(b1.id, b2.id)
        self.assertNotEqual(b1, b2)

    def test_load_from_file(self):
        b1 = Base(1)
        Base.save_to_file([b1])
        bases = Base.load_from_file()
        self.assertEqual(bases[0].id, b1.id)
        self.assertNotEqual(bases[0], b1)

    def test_load_from_file_no_file(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        self.assertEqual(Base.load_from_file(), [])

    def test_create_no_args(self):
        with self.assertRaises(TypeError):
            Base.create()

if __name__ == "__main__":
    unittest.main()
