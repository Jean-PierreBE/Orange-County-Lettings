""" tests views profiles """
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed  # pylint: disable=E0611
import pytest
from django.conf import settings                      # pylint: disable=C0412
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_index_view(client):
    """ test view all profiles """
    response = client.get(reverse('profiles_index'))

    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/index.html')


@pytest.mark.django_db
def test_profile_view(client):
    """ test view profile """
    user_test = User(username='jps01',
                     email='jps01@mail.be',
                     password="toto",)
    user_test.save()
    profile_test = Profile(favorite_city='chez moi',
                           user=user_test)
    profile_test.save()

    path = reverse('profile', args=[user_test.username])
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/profile.html')


@pytest.mark.django_db
def test_profile_view_error_404(client):
    """ test error 404"""
    path = reverse('profile', args=['jps'])                 # pylint: disable=R0801
    response = client.get(path)                             # pylint: disable=R0801

    if settings.DEBUG:                                      # pylint: disable=R0801
        assert response.status_code == 404                  # pylint: disable=R0801
    else:                                                   # pylint: disable=R0801
        assert response.status_code == 200
        assertTemplateUsed(response, 'error/404.html')      # pylint: disable=R0801
