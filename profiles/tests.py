from django.test import TestCase
from django.contrib.auth.models import User
import os
from django.urls import reverse
from django.apps import apps

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projet-13.settings")

# db_profile = (next((m for m in apps.get_models()
# if m._meta.db_table=='oc_lettings_site_profile'), None))
# self.x = apps.get_model(app_label="profiles", model_name="Profile")
# self.profile = Profile.objects.create(user=self.user, favorite_city="prout")


class ProfilesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test123",
            password="Thomas404*",
            email="test@email.com",
        )
        self.p = next(
            (
                m
                for m in apps.get_models()
                if m._meta.db_table == "oc_lettings_site_profile"
            ),
            None,
        )
        self.p.objects.create(user=self.user, favorite_city="ici")
        print(self.p)

    def test_profile_index(self):
        response = self.client.get(reverse("index"))
        assert response.status_code == 200
        assert b"<title>Holiday Homes</title>" in response.content
