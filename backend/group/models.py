from django.db import models
from helpers.decorators.track_create_and_change import track_creation_and_change

from customer.models import Customer
from schedule.models import Lecture
from position.models import Position

from .constants import LECTURE_NUMBER_CHOICES


@track_creation_and_change
class Group(models.Model):
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.SET_NULL,
        null=True,
        related_name='group_customer',
        verbose_name='Клиент'
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        related_name='group_lecture',
        verbose_name='Должность'
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.SET_NULL,
        null=True,
        related_name='group_lecture',
        verbose_name='Лекция'
    )
    hologram = models.CharField('Номер голограммы', max_length=50, blank=True, null=True)
    # Перенести книжку в клиента?
    medical_book_number = models.CharField('Номер медецинской книжки', max_length=50, blank=True, null=True)
    lecture_number_in_lmk = models.CharField(
        'Номер обучения в ЛМК', 
        max_length=1, 
        blank=True, 
        null=True,
        choices=LECTURE_NUMBER_CHOICES,
        default=LECTURE_NUMBER_CHOICES[0]
    )
    first_lecture = models.BooleanField('Первичное обучение', default=False)
    attestation_required = models.BooleanField('Требуется аттестация', default=True)


    class Meta:
        db_table = 'group'
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return f'Клиент {self.customer}: должность - {self.position} - {self.lecture} '
