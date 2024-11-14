from django.contrib import admin
from django.urls import path

from students.views import *
from rest_framework.routers import SimpleRouter

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

router = SimpleRouter()

router.register('api/students', StudentViewSet)
router.register('api/groups', GroupViewSet)
router.register('api/specialities', SpecialityViewSet)
router.register('api/disciplines', DisciplineViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/schema/',
        SpectacularAPIView.as_view(), name = 'schema'
    ),
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name = 'schema'),
        name = 'swagger-ui'
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name = 'schema'),
        name = 'redoc'
    ),
]

urlpatterns += router.urls
