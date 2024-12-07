from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from students.models import Student, Group, Speciality, Discipline, AcademicPerformance
from students.serializers import StudentSerializer, GroupSerializer, SpecialitySerializer, DisciplineSerializer, \
    AcademicPerformanceSerializer, FormOfEducation


# Create your tests here.
class StudentModelTestCase(APITestCase):
    def test_get(self):
        speciality_1 = Speciality.objects.create(
            id = 1,
            name = 'Информационная безопасность'
        )

        group_1 = Group.objects.create(
            id = 2,
            group_number = '221-331',
            speciality = Speciality.objects.get(id = 1)
        )

        form = FormOfEducation.objects.create(
            id = 1,
            form = 'Очная'
        )

        student_1 = Student.objects.create(
            id = 1,
            first_name = 'Иван',
            last_name = 'Иванов',
            middle_name = 'Иванович',
            year_of_entry = 2022,
            year_of_ending = 2028,
            form_of_education = FormOfEducation.objects.get(id = 1),
            group = Group.objects.get(id = 2)
        )

        student_2 = Student.objects.create(
            id = 2,
            first_name = 'Григорий',
            last_name = 'Петров',
            middle_name = 'Александрович',
            year_of_entry = 2022,
            year_of_ending = 2026,
            form_of_education = FormOfEducation.objects.get(id = 1),
            group = Group.objects.get(id = 2)
        )

        url = reverse('student-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            StudentSerializer([student_1, student_2], many = True).data,
            response.data
        )


class GroupModelTestCase(APITestCase):
    def test_get(self):
        speciality_1 = Speciality.objects.create(
            id = 1,
            name = 'Веб-разработка'
        )

        group_1 = Group.objects.create(
            id = 1,
            group_number='221-351',
            speciality = Speciality.objects.get(id = 1)
        )

        group_2 = Group.objects.create(
            id = 2,
            group_number = '221-353',
            speciality = Speciality.objects.get(id = 1)
        )

        url = reverse('group-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            GroupSerializer([group_1, group_2], many = True).data,
            response.data
        )


class SpecialityModelTestCase(APITestCase):
    def test_get(self):
        speciality_1 = Speciality.objects.create(
            id = 1,
            name = 'Big Data'
        )

        speciality_2 = Speciality.objects.create(
            id = 2,
            name = 'Програмная инженерия'
        )

        url = reverse('speciality-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            SpecialitySerializer([speciality_1, speciality_2], many = True).data,
            response.data
        )


class DisciplineModelTestCase(APITestCase):
    def test_get(self):
        speciality_1 = Speciality.objects.create(
            id = 1,
            name = 'Програмная инженерия'
        )

        discipline_1 = Discipline.objects.create(
            id = 1,
            name = 'Теория вероятности',
            number_of_hours = 70,
            reporting_form = 'Экзамен',
            speciality = Speciality.objects.get(id = 1)
        )

        discipline_2 = Discipline.objects.create(
            id = 2,
            name = 'Програмирование алгоритмов',
            number_of_hours = 120,
            reporting_form = 'Экзамен',
            speciality = Speciality.objects.get(id = 1)
        )

        url = reverse('discipline-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            DisciplineSerializer([discipline_1, discipline_2], many = True).data,
            response.data
        )


class AcademicPerformanceModelTestCase(APITestCase):
    def test_get(self):
        speciality_1 = Speciality.objects.create(
            id = 1,
            name = 'Информационная безопасность'
        )

        group_1 = Group.objects.create(
            id = 1,
            group_number = '221-331',
            speciality = Speciality.objects.get(id = 1)
        )

        form = FormOfEducation.objects.create(
            id = 1,
            form = 'Очная'
        )

        student_1 = Student.objects.create(
            id = 1,
            first_name = 'Иван',
            last_name = 'Иванов',
            middle_name = 'Иванович',
            year_of_entry = 2022,
            year_of_ending = 2026,
            form_of_education = FormOfEducation.objects.get(id = 1),
            group = Group.objects.get(id = 1)
        )

        discipline_1 = Discipline.objects.create(
            id = 1,
            name = 'Теория вероятности',
            number_of_hours = 70,
            reporting_form = 'Экзамен',
            speciality = Speciality.objects.get(id=1)
        )

        academic_performance = AcademicPerformance.objects.create(
            id = 1,
            year = 2022,
            mark = 5,
            student = Student.objects.get(id = 1),
            discipline = Discipline.objects.get(id = 1),
        )

        url = reverse('academic-performance-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            AcademicPerformanceSerializer(academic_performance).data,
            *response.data
        )
