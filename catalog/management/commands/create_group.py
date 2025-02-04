from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group


class Command(BaseCommand):
    help = "Создание новой группы с ролью 'Модератор'"

    def handle(self, *args, **options):
        moderators_group = Group.objects.create(name="Moderators")

        publish_product = Permission.objects.get(codename="can_unpublish_product")
        delete_product = Permission.objects.get(codename="can_delete_product")

        moderators_group.permissions.add(publish_product, delete_product)
        moderators_group.save()
        print("Группа модераторов создана")
