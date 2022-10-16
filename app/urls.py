from django.urls import path, include
from rest_framework import routers
from app.views import BlogViewSet, ServiceViewSet

router = routers.DefaultRouter()
router.register('Blog', BlogViewSet)
router.register('Service', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]