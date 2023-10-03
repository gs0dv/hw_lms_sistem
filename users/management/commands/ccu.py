from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@mail.ru',
            first_name='test_name',
            last_name='test_last_name',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('12345')
        user.save()
