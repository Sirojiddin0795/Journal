from rest_framework.routers import DefaultRouter
from .views import FAQViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
