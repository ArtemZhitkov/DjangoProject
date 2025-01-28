from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта")
    stock = models.PositiveIntegerField(verbose_name="Количество в наличии")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="Продукты"
    )
    image = models.ImageField(
        upload_to="images/", verbose_name="Изображение", blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
