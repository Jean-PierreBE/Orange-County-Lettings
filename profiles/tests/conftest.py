from django.test import Client
import pytest


@pytest.fixture
def client():
    client = Client()
    return client
