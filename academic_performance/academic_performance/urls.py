from django.contrib import admin
from django.urls import path, include

from students.views import *
from rest_framework.routers import SimpleRouter

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

router = SimpleRouter()

router.register('api/students', StudentViewSet, basename = 'student')
router.register('api/groups', GroupViewSet, basename = 'group')
router.register('api/specialities', SpecialityViewSet, basename = 'speciality')
router.register('api/disciplines', DisciplineViewSet, basename = 'discipline')

router.register('api/form-of-education', FormOfEducationViewSet, basename = 'form-of-education')

router.register('api/academic-performance', AcademicPerformanceViewSet, basename = 'academic-performance')

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

    path('auth/', include('academic_performance.auth.urls')),
]

urlpatterns += router.urls
