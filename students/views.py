from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'

    search_fields = [
        'last_name', 
        'first_name',  
        'middle_name'
    ]

    ordering_fields = [
        'last_name', 
        'year_of_entry', 
        'form_of_education'
    ]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class SpecialityViewSet(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class DisciplineViewSet(ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class AcademicPerformanceViewSet(ModelViewSet):
    queryset = AcademicPerformance.objects.all()
    serializer_class = AcademicPerformanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'