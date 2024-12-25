from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product, Category
from decimal import Decimal

class ProductTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password123'
        )
        self.category = Category.objects.create(name='Electronics')
        self.product_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': '99.99',
            'category_id': self.category.id,
            'stock_quantity': 10
        }
        self.client.force_authenticate(user=self.user)

    def test_create_product(self):
        response = self.client.post('/api/products/', self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_product_list(self):
        Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=Decimal('99.99'),
            category=self.category,
            stock_quantity=10
        )
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_product_filter(self):
        Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=Decimal('99.99'),
            category=self.category,
            stock_quantity=10
        )
        response = self.client.get('/api/products/?min_price=90&max_price=100')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
