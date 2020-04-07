from django.test import TestCase, Client


# Create your tests here.
class Test(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login(self):
        res = self.client.get('/accounts/login/')
        self.assertEqual(200, res.status_code)

    def test_logout(self):
        res = self.client.get('/accounts/logout/')
        self.assertEqual(200, res.status_code)