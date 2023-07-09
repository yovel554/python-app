import unittest
from app import app

class RegistrationTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_registration_successful(self):
        registration_data = {
            'username': 'john',
            'password': 'password123',
            'email': 'john@example.com'
        }

        response = self.client.post('/register', data=registration_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'User registration successful!')

    def test_missing_fields(self):
        registration_data = {
            'username': 'john',
            'password': 'password123'
        }

        response = self.client.post('/register', data=registration_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Missing required fields')

if __name__ == '__main__':
    unittest.main()