from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path("", views.index, name="index"),
    path("", include("profiles.urls")),
    path("", include("lettings.urls")),
    path("sentry-debug/", trigger_error),
    path("admin/", admin.site.urls),
]
