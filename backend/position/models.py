from django.db import models
from helpers.decorators.track_create_and_change import track_creation_and_change

@track_creation_and_change
class Position(models.Model):
    title = models.CharField('Название должности', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)

    class Meta:
        db_table = 'position'
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return f'{self.title}'
