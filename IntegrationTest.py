import unittest
import threading
import requests
import time
from server import create_app

class TestServerIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the Flask server in a background thread
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.server_thread = threading.Thread(target=cls.app.run, kwargs={'debug': False, 'use_reloader': False})
        cls.server_thread.start()
        time.sleep(1)  # Give the server a second to ensure it is up

    def test_status_endpoint(self):
        # Test the /status endpoint
        response = requests.get('http://127.0.0.1:5000/status')
        self.assertIn(response.json()['result'], ['pending', 'completed', 'error'])

if __name__ == '__main__':
    unittest.main()
