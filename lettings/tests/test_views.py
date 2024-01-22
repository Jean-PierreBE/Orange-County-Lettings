from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
import pytest

from lettings.views import index, letting


@pytest.mark.django_db
def test_indexview(client):
    response = client.get(reverse('lettings_index'))

    """ 
    In the first assert, We are testing if our get request returns 200 (OK) status code 
    For the second assert, we are making sure that our view returns the home.html template
    """

    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')


@pytest.mark.django_db
def test_lettingview(client):
    response = client.get(reverse('lettings:letting', args=[1]))

    """ 
    In the first assert, We are testing if our get request returns 200 (OK) status code 
    For the second assert, we are making sure that our view returns the home.html template
    """

    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/letting.html')
