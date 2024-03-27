""" tests models for lettings """
from django.test import TestCase
from django.core.exceptions import ValidationError
from lettings.models import Address, Letting


class TestAdress(TestCase):
    """ test model address """

    def setUp(self):
        """create data to test the address model"""
        self.address = Address.objects.create(   # pylint: disable=E1101
            number=60,
            street='Avenue de l emeraude',
            city='bruxelles',
            state='Bruxelles capitale',
            zip_code='1030',
            country_iso_code='BE')

    def test_str(self):
        """ Test the __str__ method of address model"""
        expected = "60 Avenue de l emeraude"
        actual = str(self.address)

        self.assertEqual(expected, actual)

    def test_number(self):
        """ Test the __str__ method of address model"""
        obj = Address.objects.create(number=10000,          # pylint: disable=E1101
                                     street='Avenue de l emeraude',
                                     city='bruxelles',
                                     state='Bruxelles capitale',
                                     zip_code='1030',
                                     country_iso_code='BE')
        self.assertRaises(ValidationError, obj.full_clean)


class TestLetting(TestCase):
    """ test model letting  """
    def setUp(self):
        """ create data to test the letting model"""
        self.address = Address.objects.create(  # pylint: disable=E1101
            number=60,
            street='Avenue de l emeraude',
            city='bruxelles',
            state='Bruxelles capitale',
            zip_code='1030',
            country_iso_code='BE')

        self.letting = Letting.objects.create(  # pylint: disable=E1101
            title='A la maison',
            address=self.address)

    def test_str(self):
        """ Test the __str__ method of letting model"""
        expected = 'A la maison'
        actual = str(self.letting)

        self.assertEqual(expected, actual)
