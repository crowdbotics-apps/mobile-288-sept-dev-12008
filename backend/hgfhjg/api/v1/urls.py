from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GfkhgkjhgkjViewSet

router = DefaultRouter()
router.register("gfkhgkjhgkj", GfkhgkjhgkjViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
