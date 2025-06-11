from rest_framework.routers import DefaultRouter
from .views import PublicationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('', PublicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
