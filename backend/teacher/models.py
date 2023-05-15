from django.db import models
from educational_programs.models import ProgramSubCategories
from helpers.decorators.track_create_and_change import track_creation_and_change

from schedule.models import Lecture


@track_creation_and_change
class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name='Фамилия Имя Отчество')
    phone = models.CharField(max_length=50, unique=True, verbose_name='Телефон', null=True)
    email = models.EmailField(max_length=50, unique=True, verbose_name='Электронная почта', null=True)
    sub_categories = models.ManyToManyField(ProgramSubCategories, related_name='teacher_sub_category')

    class Meta:
        db_table = 'teachers'
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f'{self.name} {self.phone}'


@track_creation_and_change
class Workload(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name="workload_teacher"
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.SET_NULL,
        null=True,
        related_name="workload_lecture"
    )
    hours = models.DecimalField('Часы', max_digits=4, decimal_places=2)

    class Meta:
        db_table = 'workload'
        verbose_name = "Workload"
        verbose_name_plural = "Workloads"

    def __str__(self):
        return f'{self.teacher.name} {self.hours}'

