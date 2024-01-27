from django.test import TestCase
from django.core.exceptions import ValidationError
from lettings.models import Address, Letting


class TestAdress(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=60,
            street='Avenue de l emeraude',
            city='bruxelles',
            state='Bruxelles capitale',
            zip_code='1030',
            country_iso_code='BE')

    def test_str(self):
        """ Test the __str__ method"""
        expected = "60 Avenue de l emeraude"
        actual = str(self.address)

        self.assertEqual(expected, actual)

    def test_number(self):
        """ Test the __str__ method"""
        obj = Address.objects.create(number=10000,
                                     street='Avenue de l emeraude',
                                     city='bruxelles',
                                     state='Bruxelles capitale',
                                     zip_code='1030',
                                     country_iso_code='BE')
        self.assertRaises(ValidationError, obj.full_clean)


class TestLetting(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=60,
            street='Avenue de l emeraude',
            city='bruxelles',
            state='Bruxelles capitale',
            zip_code='1030',
            country_iso_code='BE')

        self.letting = Letting.objects.create(
            title='A la maison',
            address=self.address)

    def test_str(self):
        """ Test the __str__ method"""
        expected = 'A la maison'
        actual = str(self.letting)

        self.assertEqual(expected, actual)
