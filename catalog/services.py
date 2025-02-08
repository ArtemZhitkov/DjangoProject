from .models import Category, Product

class CategoryService:
    @staticmethod
    def get_all_categories():
        """
        Возвращает все категории
        """
        return Category.objects.all()

    @staticmethod
    def get_products_from_category(category):
        """
        Возвращает продукты из указанной категории
        """
        return Product.objects.filter(category=category)
