""" tests views main app """
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed   # pylint: disable=E0611
import pytest


@pytest.mark.django_db
def test_homeview(client):
    """ test how view """
    response = client.get(reverse('home'))

    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
