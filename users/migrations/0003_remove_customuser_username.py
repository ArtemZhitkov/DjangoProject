# Generated by Django 5.1.5 on 2025-02-01 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_customuser_token"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="username",
        ),
    ]
