import unittest

import sys, os
sys.path.append(os.path.abspath("../../"))
from project.server import db
from project.server.models import User
from project.tests.base import BaseTestCase

class TestUserModel(BaseTestCase):
    def test_encode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)

        self.assertTrue(isinstance(auth_token, str))

    def test_decode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, str))
        self.assertTrue(User.decode_auth_token(auth_token) == 1)

if __name__ == '__main__':
    unittest.main()