import django
import unittest
from django.test import Client

django.setup()


class MainTest(unittest.TestCase):
    client = Client()

    # Test for a valid link

    def test_valid_link(self):
        response = self.client.get('/index/analyse/')
        self.assertEqual(response.status_code, 200)

    # Test for an invalid link : 404 (Not Found)

    def test_invalid_link(self):
        response = self.client.get('/index/analyse/daf')
        self.assertEqual(response.status_code, 404)










