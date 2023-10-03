from django.conf import settings
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Course(models.Model):
    title = models.CharField(max_length=300, verbose_name='название')
    preview = models.ImageField(upload_to='education/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=300, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='education/', verbose_name='превью', **NULLABLE)
    link = models.TextField(verbose_name='ссылка на видео', **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    CASH = 'Наличные'
    TRANSFER_TO_ACCOUNT = 'Перевод на счет'

    PAYMENT_METHOD = (
        (CASH, 'Наличные'),
        (TRANSFER_TO_ACCOUNT, 'Перевод на счет'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                             verbose_name='пользователь')
    date_payment = models.DateField(verbose_name='дата оплаты', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный урок')
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, verbose_name='периодичность рассылки')

    def __str__(self):
        return f'{self.user} - {self.payment_amount} ({self.paid_course if self.paid_course else self.paid_lesson})'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
