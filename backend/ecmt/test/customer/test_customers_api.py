from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from customer.models import Customer
from customer.serializers import CustomerSerializer


class CustomerApiTestCases(APITestCase):
    def setUp(self) -> None:
        self.customer1 = Customer.objects.create(
            last_name='Иванов',
            first_name='Иван',
            second_name='Иванович',
            phone='789123456789',
            email='789123456789@test.ru',
            is_deleted=False
        )
        self.customer2 = Customer.objects.create(
            last_name='Иванов',
            first_name='Петр',
            second_name='Иванович',
            phone='+789123456788',
            email='+789123456788@test.ru',
            is_deleted=False
        )
        self.customer3 = Customer.objects.create(
            last_name='Петров',
            first_name='Петр',
            second_name='Петрович',
            phone='+789123456787',
            email='+789123456787@test.ru',
            is_deleted=False
        )
        self.customer4 = Customer.objects.create(
            last_name='Сидоров',
            first_name='Петр',
            second_name='Петрович',
            phone='+789123456786',
            email='+789123456786@test.ru',
            is_deleted=False
        )

    def test_get_customer(self):
        url = reverse('customer-list')
        res = self.client.get(url)
        customer = [self.customer1, self.customer2, self.customer3, self.customer4]
        expected_result = CustomerSerializer(customer, many=True).data
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertEqual(expected_result, res.data)
    def test_get_customer_search(self):
        url = reverse('customer-list')
        res = self.client.get(url, data={'search': 'Петр'})
        customer = [self.customer2, self.customer3, self.customer4]
        expected_result = CustomerSerializer(customer, many=True).data
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertEqual(expected_result, res.data)

    def test_get_customer_filter_by_first_name(self):
        url = reverse('customer-list')
        res = self.client.get(url, data={'first_name': 'Иван'})
        customer = [self.customer1]
        expected_result = CustomerSerializer(customer, many=True).data
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertEqual(expected_result, res.data)

    def test_get_customer_filter_by_second_name(self):
        url = reverse('customer-list')
        res = self.client.get(url, data={'second_name': 'Петрович'})
        customer = [self.customer3, self.customer4]
        expected_result = CustomerSerializer(customer, many=True).data
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertEqual(expected_result, res.data)

    def test_get_customer_filter_by_name_last_name(self):
        url = reverse('customer-list')
        res = self.client.get(url, data={'last_name': 'Иванов'})
        customer = [self.customer1, self.customer2]
        expected_result = CustomerSerializer(customer, many=True).data
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertEqual(expected_result, res.data)