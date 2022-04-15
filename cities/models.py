from django.db import models


class Ciry(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name = 'Город')
# Create your models here.
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']