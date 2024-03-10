import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):

    def setUp(self):
        self.test_user = User(
            first_name="John",
            last_name="Doe",
            email="<EMAIL>",
            password="password"
        )

    def test_init(self):
        self.assertEqual(self.test_user.first_name, "John")
        self.assertEqual(self.test_user.last_name, "Doe")
        self.assertEqual(self.test_user.email, "<EMAIL>")
        self.assertIsInstance(self.test_user.created_at, datetime)
        self.assertIsInstance(self.test_user.updated_at, datetime)

    def test_save(self):
        self.test_user.save()
        saved_user = models.storage.all()["User.{}".format(self.test_user.id)]
        self.assertEqual(saved_user.__dict__, self.test_user.__dict__)

    def test_to_dict(self):
        user_dict = self.test_user.to_dict()
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)
        self.assertIn("email", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)

    def test_inheritance(self):
        self.assertIsInstance(self.test_user, BaseModel)
        self.assertIsInstance(self.test_user, User)

    def test_attributes(self):
        self.assertEqual(self.test_user.id, "User.{}".format(self.test_user.id))

if __name__ == '__main__':
    unittest.main()