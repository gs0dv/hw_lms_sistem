from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=300, verbose_name='название')
    preview = models.ImageField(upload_to='education/', verbose_name='превью')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
