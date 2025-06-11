from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, ReviewViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
