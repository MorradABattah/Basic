import unittest
from flask import url_for
from runner import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
