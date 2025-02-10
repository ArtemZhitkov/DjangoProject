from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление тестовых продуктов в БД"

    def handle(self, *args, **options):
        # Удаление всех продуктов и категорий
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание категорий
        category, _ = Category.objects.get_or_create(name="Категория1")

        products = [
            {
                "name": "Продукт1",
                "stock": 1,
                "description": "Описание продукта1",
                "price": 100,
                "category": category,
            },
            {
                "name": "Продукт2",
                "stock": 1,
                "description": "Описание продукта1",
                "price": 200,
                "category": category,
            },
            {
                "name": "Продукт3",
                "stock": 1,
                "description": "Описание продукта1",
                "price": 300,
                "category": category,
            },
        ]

        # Создание продуктов
        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                print(f"Создан продукт: {product}")
            else:
                print(f'Продукт с названием {product_data["name"]} уже существует')
