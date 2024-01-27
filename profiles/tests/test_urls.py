from django.urls import reverse, resolve
from profiles.views import index, profile


def test_url_profile_index():

    """
    Testing if the 'favourite-products' route is mapping to FavouriteProductListView
    """

    url = reverse('profiles_index')
    assert resolve(url).view_name == 'profiles_index'
    assert resolve(url).func == index


def test_url_profile():

    """
    Testing if the 'favourite-products' route is mapping to FavouriteProductListView
    """

    url = reverse('profile', args=[1])
    assert resolve(url).view_name == 'profile'
    assert resolve(url).func == profile
