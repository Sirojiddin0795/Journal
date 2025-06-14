from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Journal API",
        default_version='v1',
        description="Tadqiqot maqolalari uchun backend API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/', include('articles.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/requirements/', include('requirements.urls')),
    path('api/faq/', include('faq.urls')),
    path('api/pages/', include('pages.urls')),
    path('api/publications/', include('publications.urls')),
    path('api/contacts/', include('contacts.urls')),




    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
