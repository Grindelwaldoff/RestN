from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class ApiTest(APITestCase):
    def test_get_category(self):
        """Проверка на вывод данных о продукте."""
        url = reverse('category_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
