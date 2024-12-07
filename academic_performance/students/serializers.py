from rest_framework.serializers import ModelSerializer
from .models import *


class StudentSerializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'


class SpecialitySerializer(ModelSerializer):
    
    class Meta:
        model = Speciality
        fields = '__all__'


class FormOfEducationSerializer(ModelSerializer):
    class Meta:
        model = FormOfEducation
        fields = '__all__'


class DisciplineSerializer(ModelSerializer):
    
    class Meta:
        model = Discipline
        fields = '__all__'


class AcademicPerformanceSerializer(ModelSerializer):

    class Meta:
        model = AcademicPerformance
        fields = '__all__'