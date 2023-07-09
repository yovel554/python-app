import unittest
from app import validate_username, validate_password

class RegistrationTests(unittest.TestCase):

    def test_validate_username_valid(self):
        # Test valid usernames
        valid_usernames = ["john", "johndoe", "john123"]
        for username in valid_usernames:
            result = validate_username(username)
            self.assertTrue(result)

    def test_validate_username_invalid(self):
        # Test invalid usernames
        invalid_usernames = ["", " ", "john.doe", "john!123"]
        for username in invalid_usernames:
            result = validate_username(username)
            self.assertFalse(result)

    def test_validate_password_valid(self):
        # Test valid passwords
        valid_passwords = ["Password123", "P@ssw0rd", "SecurePassword!"]
        for password in valid_passwords:
            result = validate_password(password)
            self.assertTrue(result)

    def test_validate_password_invalid(self):
        # Test invalid passwords
        invalid_passwords = ["password", "12345678", "abcde"]
        for password in invalid_passwords:
            result = validate_password(password)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()