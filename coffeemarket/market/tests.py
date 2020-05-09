from django.test import TestCase, Client


# Create your tests here.CoffeeMarket
class CoffeeMarket(TestCase):

    def setUp(self):
        self.client = Client()

    def test_top(self):
        res = self.client.get('/market/bean/list/')
        self.assertEqual(200, res.status_code)

    def test_newbeans(self):
        res = self.client.get('/market/newbeans/')
        self.assertEqual(302, res.status_code)

    def test_bean_filter(self):
        res = self.client.get('/market/bean/list/filter/1')
        self.assertEqual(301, res.status_code)

    def test_user_cart(self):
        res = self.client.get('/market/user/cart/')
        self.assertEqual(302, res.status_code)