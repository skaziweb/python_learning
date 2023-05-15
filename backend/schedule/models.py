from django.db import models

from helpers.decorators.track_create_and_change import track_creation_and_change

from .constants import DAYS_CHOICES
from educational_programs.models import ProgramSubCategories


@track_creation_and_change
class Schedule(models.Model):
    day = models.IntegerField("День недели", choices=DAYS_CHOICES)
    slot = models.TimeField("Время лекции", auto_now=False, auto_now_add=False)
    active_until = models.DateField("Активен до", auto_now=False, auto_now_add=False)
    sub_category = models.ForeignKey(
        ProgramSubCategories,
        on_delete=models.SET_NULL,
        null=True,
        related_name="education_program"
    )

    class Meta:
        db_table = "schedule"
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        day = DAYS_CHOICES[self.day][1]
        return f'{self.sub_category}: День - {day}, Время - {self.slot}, активно до {self.active_until}'
