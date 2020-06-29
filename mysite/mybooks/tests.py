from django.test import TestCase

class FirstTest(TestCase):
    def test_index(self):
        req = self.client.get("/")
        self.assertEqual(req.status_code, 200)
