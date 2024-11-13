from django.contrib import admin
from .models import *

# Register your models here.
model_list = [Student, Discipline, Speciality, Group, AcademicPerformance]
admin.site.register(model_list)