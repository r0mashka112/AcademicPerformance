from django.contrib import admin
from django.urls import path

from students.views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('api/students', StudentViewSet)
router.register('api/groups', GroupViewSet)
router.register('api/specialities', SpecialityViewSet)
router.register('api/disciplines', DisciplineViewSet)

urlpatterns = [
    path('admin/', admin.site.urls)
]

urlpatterns += router.urls
