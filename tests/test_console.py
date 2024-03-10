import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.test_object = BaseModel(name="test", age=25)

    def test_init(self):
        self.assertEqual(self.test_object.name, "test")
        self.assertEqual(self.test_object.age, 25)
        self.assertIsInstance(self.test_object.created_at, datetime)
        self.assertIsInstance(self.test_object.updated_at, datetime)

    def test_save(self):
        self.test_object.save()
        saved_object = models.storage.all()[self.test_object.id]
        self.assertEqual(saved_object.__dict__, self.test_object.__dict__)

    def test_to_dict(self):
        obj_dict = self.test_object.to_dict()
        self.assertIn("name", obj_dict)
        self.assertIn("age", obj_dict)
        self.assertIn("__class__", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)

if __name__ == '__main__':
    unittest.main()
