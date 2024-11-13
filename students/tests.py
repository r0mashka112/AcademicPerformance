from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


# Create your tests here.
class StudentModelTestCase(APITestCase):
    def test_get(self):
        url = reverse('api/students-list')
        print(url)
        response = self.client.get(url)
        print(response)