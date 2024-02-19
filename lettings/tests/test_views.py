""" tests views lettings """
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed  # pylint: disable=E0611
from django.conf import settings                      # pylint: disable=C0412
import pytest

from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_view(client):
    """ test all lettings view """
    response = client.get(reverse('lettings_index'))

    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')


@pytest.mark.django_db
def test_letting_view(client):
    """ test one letting """
    address_test = Address(number=1,
                           street='Rue du Saphir',
                           city='Bruxelles',
                           state='Belgique',
                           zip_code=1030,
                           country_iso_code='BE'
                           )
    address_test.save()
    letting_test = Letting(title='chez moi',
                           address=address_test)
    letting_test.save()

    path = reverse('letting', args=[letting_test.id])   # pylint: disable=E1101
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/letting.html')


@pytest.mark.django_db
def test_letting_view_error_404(client):
    """ test one letting """
    path = reverse('letting', args=[654])       # pylint: disable=R0801
    response = client.get(path)                             # pylint: disable=R0801

    if settings.DEBUG:                                      # pylint: disable=R0801
        assert response.status_code == 404                  # pylint: disable=R0801
    else:                                                   # pylint: disable=R0801
        assert response.status_code == 200                  # pylint: disable=R0801
        assertTemplateUsed(response, 'error/404.html')      # pylint: disable=R0801
