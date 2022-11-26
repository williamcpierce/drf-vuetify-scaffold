from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"message", views.MessageViewSet, basename="message")


urlpatterns = [
    path("", include(router.urls)),
]
