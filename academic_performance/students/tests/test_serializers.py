from django.test import TestCase

from students.models import Student, Group, Speciality, Discipline, AcademicPerformance
from students.serializers import StudentSerializer, GroupSerializer, SpecialitySerializer, DisciplineSerializer, \
    AcademicPerformanceSerializer, FormOfEducation


class StudentSerializerTestCase(TestCase):
    def test_ok(self):
        speciality_1 = Speciality.objects.create(
            id = 2,
            name = 'Информационная безопасность'
        )

        group_1 = Group.objects.create(
            id = 2,
            group_number = '221-331',
            speciality = Speciality.objects.get(id = 2)
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
            group = Group.objects.get(id = 2)
        )

        student_2 = Student.objects.create(
            id = 2,
            first_name = 'Григорий',
            last_name = 'Петров',
            middle_name = 'Александрович',
            year_of_entry = 2022,
            year_of_ending = 2028,
            form_of_education = FormOfEducation.objects.get(id = 1),
            group = Group.objects.get(id = 2)
        )

        data = StudentSerializer([student_1, student_2], many = True).data

        expected_data = [
            {
                'id' : student_1.id,
                'first_name' : 'Иван',
                'last_name' : 'Иванов',
                'middle_name' : 'Иванович',
                'year_of_entry' : 2022,
                'year_of_ending' : 2026,
                'form_of_education' : 1,
                'group' : 2
            },

            {
                'id' : student_2.id,
                'first_name' : 'Григорий',
                'last_name' : 'Петров',
                'middle_name' : 'Александрович',
                'year_of_entry' : 2022,
                'year_of_ending' : 2028,
                'form_of_education' : 1,
                'group' : 2
            }
        ]

        self.assertEqual(data, expected_data)


class GroupSerializerTestCase(TestCase):
    def test_ok(self):
        speciality_1 = Speciality.objects.create(
            id = 1,
            name = 'Програмная инженерия'
        )

        group_1 = Group.objects.create(
            id = 1,
            group_number = '221-351',
            speciality = Speciality.objects.get(id = 1)
        )

        group_2 = Group.objects.create(
            id = 2,
            group_number = '221-353',
            speciality = Speciality.objects.get(id = 1)
        )

        data = GroupSerializer([group_1, group_2], many = True).data

        expected_data = [
            {
                'id' : group_1.id,
                'group_number' : '221-351',
                'speciality' : 1
            },

            {
                'id' : group_2.id,
                'group_number': '221-353',
                'speciality': 1
            }
        ]

        self.assertEqual(data, expected_data)


class SpecialitySerializerTestCase(TestCase):
    def test_ok(self):
        speciality_1 = Speciality.objects.create(
            id = 1,
            name = 'Информационная безопасность'
        )

        speciality_2 = Speciality.objects.create(
            id = 2,
            name = 'Програмная инженерия'
        )

        speciality_3 = Speciality.objects.create(
            id = 3,
            name = 'Веб-разработка'
        )

        data = SpecialitySerializer([speciality_1, speciality_2, speciality_3], many = True).data

        expected_data = [
            {
                'id' : speciality_1.id,
                'name' : 'Информационная безопасность'
            },

            {
                'id': speciality_2.id,
                'name': 'Програмная инженерия'
            },

            {
                'id': speciality_3.id,
                'name': 'Веб-разработка'
            }
        ]

        self.assertEqual(data, expected_data)


class DisciplineSerializerTestCase(TestCase):
    def test_ok(self):
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

        data = DisciplineSerializer([discipline_1, discipline_2], many = True).data

        expected_data = [
            {
                'id' : discipline_1.id,
                'name' : 'Теория вероятности',
                'number_of_hours' : 70,
                'reporting_form' : 'Экзамен',
                'speciality' : 1
            },

            {
                'id' : discipline_2.id,
                'name' : 'Програмирование алгоритмов',
                'number_of_hours' : 120,
                'reporting_form' : 'Экзамен',
                'speciality' : 1
            }
        ]

        self.assertEqual(data, expected_data)


class AcademicPeriodSerializerTestCase(TestCase):
    def test_ok(self):
        speciality_1 = Speciality.objects.create(
            id = 1,
            name = 'Информационная безопасность'
        )

        group_1 = Group.objects.create(
            id = 1,
            group_number = '221-351',
            speciality = Speciality.objects.get(id=1)
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
            year_of_entry = 2021,
            year_of_ending = 2025,
            form_of_education = FormOfEducation.objects.get(id = 1),
            group = Group.objects.get(id = 1)
        )

        discipline_1 = Discipline.objects.create(
            id = 2,
            name = 'Теория вероятности',
            number_of_hours = 70,
            reporting_form = 'Экзамен',
            speciality = Speciality.objects.get(id = 1)
        )

        academic_performance = AcademicPerformance.objects.create(
            id = 1,
            year = 2022,
            mark = 5,
            student = Student.objects.get(id = 1),
            discipline = Discipline.objects.get(id = 2),
        )

        data = AcademicPerformanceSerializer(academic_performance).data

        expected_data = [
            {
                'id' : academic_performance.id,
                'year' : 2022,
                'mark' : 5,
                'student' : 1,
                'discipline' : 2,
            }
        ]

        self.assertEqual(data, *expected_data)
