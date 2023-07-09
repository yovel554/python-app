import unittest
import json
from app import app

class RegistrationTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_registration_successful(self):
        registration_data = {
            'username': 'yovel',
            'password': 'yovel',
        }

        response = self.client.post('/register', json=registration_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'User registration successful!')

    def test_missing_fields(self):
        registration_data = {
            'username': 'yovel',
            'password': 'yovel'
        }

        response = self.client.post('/register', json=registration_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Missing required fields')

if __name__ == '__main__':
    unittest.main()