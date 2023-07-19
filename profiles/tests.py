from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class ProfilesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="Thomas404*", email="test@email.com"
        )
        self.profile = Profile.objects.create(
            user=self.user, favorite_city="Flagstaff en arizona"
        )

    def test_profile_index_reachable(self):
        response = self.client.get(reverse("profiles_index"))
        assert response.status_code == 200
        assert b"<title>Profiles</title>" in response.content

    def test_profile_exists(self):
        response = self.client.get(reverse("profile", args=[self.user.username]))
        assert response.status_code == 200
        assert b"<p>Favorite city: Flagstaff en arizona</p>" in response.content
