from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny


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
    
    permission_classes = [AllowAny]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    permission_classes = [AllowAny]


class SpecialityViewSet(ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    permission_classes = [AllowAny]


class DisciplineViewSet(ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    permission_classes = [AllowAny]


class AcademicPerformanceViewSet(ModelViewSet):
    queryset = AcademicPerformance.objects.all()
    serializer_class = AcademicPerformanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    permission_classes = [AllowAny]


class FormOfEducationViewSet(ModelViewSet):
    queryset = FormOfEducation.objects.all()
    serializer_class = FormOfEducationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    permission_classes = [AllowAny]
