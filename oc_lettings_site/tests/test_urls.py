from django.urls import reverse, resolve
from oc_lettings_site.views import home


def test_url_home():

    """
    Testing if the 'favourite-products' route is mapping to FavouriteProductListView
    """

    url = reverse('home')
    assert resolve(url).view_name == 'homeless'
    assert resolve(url).func == home
