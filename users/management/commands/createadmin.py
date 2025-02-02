from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Создание нового пользователя с ролью 'admin'"

    def handle(self, *args, **options):
        User = get_user_model()

        user = User.objects.create(
            username='admin',
            email='admin@mail.ru',
            first_name='Admin',
            last_name='Adminex',
        )
        user.set_password('admin')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f"Создан новый пользователь: {user}"))
