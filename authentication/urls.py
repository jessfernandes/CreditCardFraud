from django.urls import path
from authentication.views import login, renovate


urlpatterns = [
    path("login/", login),
    path("renovate/", renovate),
]