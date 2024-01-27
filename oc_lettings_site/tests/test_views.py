from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
import pytest


@pytest.mark.django_db
def test_HomeView(client):
    response = client.get(reverse('home'))
    """
    In the first assert, We are testing if our get request returns 200 (OK) status code
    For the second assert, we are making sure that our view returns the home.html template"""

    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
