from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from django.conf import settings
import pytest

from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_view(client):

    response = client.get(reverse('lettings_index'))
    """
    In the first assert, We are testing if our get request returns 200 (OK) status code
    For the second assert, we are making sure that our view returns the home.html template
    """
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')


@pytest.mark.django_db
def test_letting_view(client):
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

    path = reverse('letting', args=[letting_test.id])
    response = client.get(path)
    """
    In the first assert, We are testing if our get request returns 200 (OK) status code
    For the second assert, we are making sure that our view returns the home.html template
    """
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/letting.html')


@pytest.mark.django_db
def test_letting_view_error_404(client):

    path = reverse('letting', args=[654])       # pylint: disable=R0801
    response = client.get(path)                             # pylint: disable=R0801
    """
    In the first assert, We are testing if our get request returns 200 (OK) status code
    For the second assert, we are making sure that our view returns the home.html template
    """
    if settings.DEBUG:                                      # pylint: disable=R0801
        assert response.status_code == 404                  # pylint: disable=R0801
    else:                                                   # pylint: disable=R0801
        assert response.status_code == 200                  # pylint: disable=R0801
        assertTemplateUsed(response, 'error/404.html')      # pylint: disable=R0801
