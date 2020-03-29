from django.test import TestCase, Client


# Create your tests here.
class Test(TestCase):

    def setUp(self):
        self.client = Client()

    def login_test(self):
        res = self.client.get('/accounts/login')
        self.assertEqual(200, res)
