""" tests if urls are ok"""
from django.urls import reverse, resolve
from oc_lettings_site.views import home


def test_url_home():

    """
    Testing if the 'home' route is mapping to home View
    """

    url = reverse('home')
    assert resolve(url).view_name == 'home'
    assert resolve(url).func == home
