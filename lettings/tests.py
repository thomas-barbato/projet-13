from django.test import TestCase
from django.urls import reverse
from .models import Letting, Address


class ProfilesTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=742,
            street="Evergreen Terrace",
            city="Springfield",
            state="Illinois",
            zip_code="62701",
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Simpson's letting", address=self.address
        )

    def test_profile_index_reachable(self):
        response = self.client.get(reverse("lettings_index"))
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

    def test_profile_exists(self):
        response = self.client.get(reverse("letting", args=[self.letting.id]))
        assert response.status_code == 200
        assert b"<p>Springfield, Illinois 62701</p>" in response.content
