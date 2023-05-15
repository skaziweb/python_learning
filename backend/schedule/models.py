from django.db import models

from helpers.decorators.track_create_and_change import track_creation_and_change

from .constants import DAYS_CHOICES
from educational_programs.models import ProgramSubCategories


@track_creation_and_change
class Schedule(models.Model):
    day = models.IntegerField("День недели", choices=DAYS_CHOICES)
    slot = models.TimeField("Время начала", auto_now=False, auto_now_add=False)
    active_until = models.DateField("Активен до", auto_now=False, auto_now_add=False)
    sub_category = models.ForeignKey(
        ProgramSubCategories,
        on_delete=models.SET_NULL,
        null=True,
        related_name="schedule_sub_category"
    )

    class Meta:
        db_table = "schedule"
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        day = DAYS_CHOICES[self.day][1]
        return f'{self.sub_category}: День - {day}, Время - {self.slot}, активно до {self.active_until}'


@track_creation_and_change
class Lecture(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.SET_NULL,
        null=True,
        related_name="lecture_schedule"
    )
    lecture_date = models.DateField("Дата лекции", auto_now=False, auto_now_add=False)
    attestation_date = models.DateField("Дата аттестации", auto_now=False, auto_now_add=False, null=True, blank=True)
    internal = models.BooleanField("Без выезда", default=True)
    for_employees = models.BooleanField("Для сотрудников", default=True)
    class Meta:
        db_table = "lecture"
        verbose_name = "Lecture"
        verbose_name_plural = "Lectures"


    def __str__(self):
        return f'{self.schedule.sub_category}'
