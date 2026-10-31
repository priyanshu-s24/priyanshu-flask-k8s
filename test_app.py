import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_developer_name(self):
        response = self.app.get('/')
        self.assertIn(b'Priyanshu Singh', response.data)

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Priyanshu Singh', response.data)

if __name__ == "__main__":
    unittest.main()

