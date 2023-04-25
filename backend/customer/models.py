from datetime import datetime

from django.db import models
from decorators.track_create_and_change import track_creation_and_change



@track_creation_and_change
class Customer(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    second_name = models.CharField(max_length=50, verbose_name='Отчество')
    phone = models.CharField(max_length=50, unique=True, verbose_name='Телефон')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Электронная почта')

    class Meta:
        db_table = 'customers'
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.second_name}'
