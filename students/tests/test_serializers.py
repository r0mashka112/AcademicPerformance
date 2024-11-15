from django.test import TestCase

from students.models import Student, Group, Speciality
from students.serializers import StudentSerializer


class StudentSerializerTestCase(TestCase):
    def test_ok(self):
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

        data = StudentSerializer([student_1, student_2], many = True).data

        expected_data = [
            {
                'id': student_1.id,
                'first_name' : 'Иван',
                'last_name' : 'Иванов',
                'middle_name' : 'Иванович',
                'year_of_entry' : 2022,
                'form_of_education' : 'Очная',
                'group' : 2
            },

            {
                'id': student_2.id,
                'first_name': 'Григорий',
                'last_name': 'Петров',
                'middle_name': 'Александрович',
                'year_of_entry': 2022,
                'form_of_education': 'Очная',
                'group': 2
            }
        ]

        self.assertEqual(data, expected_data)
