from django.test import TestCase, Client


class SignupTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_signup(self):
        response = self.c.post('/user/signup', {'first_name':'ali',
                                                'last_name': 'arabi',
                                                'username': 'aliarabi',
                                                'email': 'ali@gmail.com',
                                                'password': '123145'})
        self.assertEqual(response.status_code, 200)
