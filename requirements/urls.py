from rest_framework.routers import DefaultRouter
from .views import RequirementViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('', RequirementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
