# Generated by Django 5.1.5 on 2025-01-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_category_description_product_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="images/", verbose_name="Изображение"
            ),
        ),
    ]
