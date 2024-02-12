""" parameters for test lettings"""
from django.test import Client
import pytest


@pytest.fixture
def client():
    """ define client """
    client_test = Client()
    return client_test
