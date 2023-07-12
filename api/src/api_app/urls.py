from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r"message", views.MessageViewSet, basename="message")

urlpatterns = router.urls
