from django.db import models


class Task(models.Model):
    title = models.CharField('VIN', max_length=20)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'VIN'
        verbose_name_plural = 'VIN NUMBERS'