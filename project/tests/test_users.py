import json
import unittest
import sys, os
sys.path.append(os.path.abspath("../../"))

from project.server import db
from project.server.models import User
from project.tests.base import BaseTestCase

class TestUsersBlueprint(BaseTestCase):
    def test_get_registered_users(self):
        """ Test for user registration """
        with self.client:
            response = self.client.get(
                '/users/index',
            )
            data = json.loads(response.data.decode())
            users = data["users"]
            self.assertEqual(len(users), 0)

            user = User(
                email='test@test.com',
                password='test'
            )
            db.session.add(user)
            db.session.commit()

            response = self.client.get(
                '/users/index',
            )
            data = json.loads(response.data.decode())
            users = data["users"]
            self.assertEqual(len(users), 1)

if __name__ == '__main__':
    unittest.main()
