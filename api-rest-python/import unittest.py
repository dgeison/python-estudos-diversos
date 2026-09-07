import unittest
from flask import Response
from main import app


class TestBuscarPessoas(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_success(self):
        response = self.client.get("/pessoas")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertIn("pessoas", response.json)
        self.assertIsInstance(response.json["pessoas"], list)
        self.assertIn("count", response.json)
        self.assertIsInstance(response.json["count"], int)

    def test_invalid_response(self):
        response = self.client.get("/pessoas")
        self.assertNotEqual(response.status_code, 404)
        self.assertNotEqual(response.status_code, 500)
        self.assertIsInstance(response.json, dict)
        self.assertNotIn("error", response.json)
        self.assertNotIn("message", response.json)


if __name__ == "__main__":
    unittest.main()
