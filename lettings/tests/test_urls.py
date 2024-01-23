from django.urls import reverse, resolve
from lettings.views import index, letting


def test_url_index():

    """
    Testing if the 'favourite-products' route is mapping to FavouriteProductListView
    """

    url = reverse('lettings_index')
    assert resolve(url).view_name == 'lettings_index'
    assert resolve(url).func == index


def test_url_letting():

    """
    Testing if the 'favourite-products' route is mapping to FavouriteProductListView
    """

    url = reverse('letting', args=[1])
    assert resolve(url).view_name == 'letting'
    assert resolve(url).func == letting
