import unittest
from flask import url_for
from runner import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = 'localhost:5000'
        self.client = app.test_client()

    def test_index(self):
        with app.app_context():
            response = self.client.get(url_for('index'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Welcome', response.data)

# Rest of the code...
