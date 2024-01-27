from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User

class TestProfile(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='jps01',
                         email='jps01@mail.be',
                         password="toto")

        self.profile = Profile.objects.create(favorite_city = 'chez moi',
                                    user = self.user)

    def test_str(self):
        """ Test the __str__ method"""
        expected = 'jps01'
        actual = str(self.profile)

        self.assertEqual(expected, actual)
