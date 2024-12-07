from django.db import models
from django import forms

# Create your models here.
class Speciality(models.Model):
    name = models.CharField(max_length = 128)

    class Meta:
        db_table = 'specialities'
        verbose_name = 'speciality'
        verbose_name_plural = 'specialities'

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length = 128)
    number_of_hours = models.IntegerField()
    reporting_form = models.CharField(max_length = 50)
    speciality = models.ForeignKey(Speciality, on_delete = models.CASCADE)

    class Meta:
        db_table = 'disciplines'
        verbose_name = 'discipline'
        verbose_name_plural = 'disciplines'

    def __str__(self):
        return self.name


class Group(models.Model):
    group_number = models.CharField(max_length = 10)
    speciality = models.ForeignKey(Speciality, on_delete = models.CASCADE)

    class Meta:
        db_table = 'groups'
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.group_number


class FormOfEducation(models.Model):
    form = models.CharField(max_length = 64)

    class Meta:
        db_table = 'form-education'
        verbose_name = 'form-education'
        verbose_name_plural = 'form-educations'

    def __str__(self):
        return self.form


class Student(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    middle_name = models.CharField(max_length = 25)
    year_of_entry = models.IntegerField()
    year_of_ending = models.IntegerField()
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    form_of_education = models.ForeignKey(FormOfEducation, on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'students'
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class AcademicPerformance(models.Model):
    year = models.IntegerField()
    mark = models.IntegerField()
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete = models.CASCADE)

    class Meta:
        db_table = 'academic_performance'
        verbose_name = 'academic_performance'
        verbose_name_plural = 'academic_performances'

    def __str__(self):
        return str(self.student)
