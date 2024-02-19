""" test models profiles """
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class TestProfile(TestCase):
    """ test model profile """

    def setUp(self):
        self.user = User.objects.create(username='jps01',
                                        email='jps01@mail.be',
                                        password="toto")

        self.profile = Profile.objects.create(favorite_city='chez moi',     # pylint: disable=E1101
                                              user=self.user)

    def test_str(self):
        """ Test the __str__ method"""
        expected = 'jps01'
        actual = str(self.profile)

        self.assertEqual(expected, actual)
