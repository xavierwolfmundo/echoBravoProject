from django.test import TestCase
from .models import Product

class DigitalStorefrontTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=10.99,
            description='This is a test product.',
            is_active=True
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 10.99)
        self.assertTrue(self.product.is_active)

    # Add more tests for other features as needed
