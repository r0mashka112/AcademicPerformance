from django.contrib import admin
from .models import Student, Discipline, Speciality, Group, AcademicPerformance, FormOfEducation

# Регистрация каждой модели по отдельности
admin.site.register(Student)
admin.site.register(Discipline)
admin.site.register(Speciality)
admin.site.register(Group)
admin.site.register(AcademicPerformance)
admin.site.register(FormOfEducation)
