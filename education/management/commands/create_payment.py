from django.core.management import BaseCommand
from django.utils.timezone import now

from education.models import Payment, Course
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        Payment.objects.create(
            user=User.objects.get(pk=2),
            date_payment=None,
            paid_course=Course.objects.get(pk=1),
            paid_lesson=None,
            payment_amount=100000,
            payment_method='Перевод на счет'
        )
