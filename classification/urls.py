from django.urls import path
from classification.views import ClassificationView

urlpatterns = [
    path("", ClassificationView.as_view()),
]
