from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from students.models import Student, Group, Speciality
from students.serializers import StudentSerializer


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

        student_1 = Student.objects.create(
            id = 1,
            first_name = 'Иван',
            last_name = 'Иванов',
            middle_name = 'Иванович',
            year_of_entry = 2022,
            form_of_education = 'Очная',
            group = Group.objects.get(id = 2)
        )

        student_2 = Student.objects.create(
            id = 2,
            first_name = 'Григорий',
            last_name = 'Петров',
            middle_name = 'Александрович',
            year_of_entry = 2022,
            form_of_education = 'Очная',
            group = Group.objects.get(id = 2)
        )

        url = reverse('student-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            StudentSerializer([student_1, student_2], many = True).data,
            response.data
        )
