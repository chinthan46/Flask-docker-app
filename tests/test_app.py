import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_root_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello from Flask", response.data)

    def test_health_endpoint(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"healthy", response.data)

if __name__ == '__main__':
    unittest.main()
