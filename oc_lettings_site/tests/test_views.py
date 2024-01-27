from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from django.conf import settings
import pytest
from django.http import HttpResponse

from oc_lettings_site.views import home


@pytest.mark.django_db
def test_HomeView(client):
    response = client.get(reverse('home'))

    """ 
    In the first assert, We are testing if our get request returns 200 (OK) status code 
    For the second assert, we are making sure that our view returns the home.html template
    """

    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
