from fastapi.testclient import TestClient
import unittest
from app.main import app

class MyTestCase(unittest.TestCase):

    client = TestClient(app)

    def test_ask_api(self):
        response = self.client.post(
            "http://192.168.2.40:8000/ask?question=%22How%20much%20is%20a%20mouse%20weight%3F%22",
        )
        self.assertIn("I don't know", response.json()["answer"])


if __name__ == '__main__':
    unittest.main()

