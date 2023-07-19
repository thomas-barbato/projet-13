from django.urls import reverse
from django.test import Client


def test_index_is_reachable():
    response = Client.get(reverse("index"))
    assert response.status_code == 200
