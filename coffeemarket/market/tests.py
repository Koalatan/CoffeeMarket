from django.test import TestCase, Client


# Create your tests here.
class CoffeeMarket(TestCase):

    def setUp(self):
        self.client = Client()

    def test_top(self):
        res = self.client.get('/market/top/')
        self.assertEqual(200, res.status_code)

    def test_newbeans(self):
        res = self.client.get('/market/newbeans/')
        self.assertEqual(200, res.status_code)
