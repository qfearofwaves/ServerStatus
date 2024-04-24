import unittest
import server
from client import StatusClient

class UnitTest(unittest.TestCase):
    def test_status_completion(self):
        tester = server.test_client(self)
        client = StatusClient("http://localhost:5000")
        result = client.get_status()
        self.assertIn(result, ["pending", "completed", "error"])

if __name__ == '__main__':
    unittest.main()
