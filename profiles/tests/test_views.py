from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
import pytest

from profiles.views import index, profile
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_index_view(client):

    response = client.get(reverse('profiles_index'))

    """ 
    In the first assert, We are testing if our get request returns 200 (OK) status code 
    For the second assert, we are making sure that our view returns the home.html template
    """

    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/index.html')

@pytest.mark.django_db
def test_profile_view(client):
    user_test = User(username = 'jps01',
                    email = 'jps01@mail.be',
                    password="toto",)
    user_test.save()
    profile_test = Profile(favorite_city = 'chez moi',
                    user = user_test)
    profile_test.save()

    path = reverse('profile', args=[user_test.username])
    response = client.get(path)

    """ 
    In the first assert, We are testing if our get request returns 200 (OK) status code 
    For the second assert, we are making sure that our view returns the home.html template
    """

    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/profile.html')
