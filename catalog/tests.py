from django.test import TestCase
from .models import Category, Product


class ModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test_category_name", description="test description")
        self.product = Product.objects.create(
            name="test_product", description="description product", stock=5, category=self.category, price=100
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), "test_product")

    def test_category_str(self):
        self.assertEqual(str(self.category), "test_category_name")

    def test_product_category_relationship(self):
        self.assertEqual(self.product.category, self.category)
