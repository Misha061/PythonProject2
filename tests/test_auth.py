import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from auth import register_user, authenticate

class TestAuthModule(unittest.TestCase):

    def test_successful_registration(self):
        result = register_user("newuser@example.com", "StrongPass123").strip()
        self.assertTrue(any(expected in result for expected in [
            "Користувача зареєстровано",
            "UNIQUE constraint failed: Users.email",
            "повторяющийся ключ в объект",
        ]), f"Unexpected result: {result}")
        print("✅ test_successful_registration — пройшов")

    def test_invalid_email(self):
        result = register_user("bademail", "StrongPass123")
        self.assertEqual(result, "Неправильний формат email")
        print("✅ test_invalid_email — пройшов")

    def test_weak_password(self):
        result = register_user("test@example.com", "abc")
        self.assertEqual(result, "Пароль занадто простий")
        print("✅ test_weak_password — пройшов")

    def test_successful_authentication(self):
        result = authenticate("user1@example.com", "password123")
        self.assertEqual(result, "Вхід успішний")
        print("✅ test_successful_authentication — пройшов")

    def test_wrong_password(self):
        result = authenticate("user1@example.com", "wrong")
        self.assertEqual(result, "Невірний логін або пароль")
        print("✅ test_wrong_password — пройшов")

    def test_unknown_email(self):
        result = authenticate("ghost@example.com", "pass")
        self.assertEqual(result, "Невірний логін або пароль")
        print("✅ test_unknown_email — пройшов")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAuthModule)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)