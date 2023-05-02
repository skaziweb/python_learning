from django.db import models
from educational_programs.models import ProgramSubCategories
from helpers.decorators.track_create_and_change import track_creation_and_change


@track_creation_and_change
class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name='Фамилия Имя Отчество')
    phone = models.CharField(max_length=50, unique=True, verbose_name='Телефон', null=True)
    email = models.EmailField(max_length=50, unique=True, verbose_name='Электронная почта', null=True)
    sub_categories = models.ManyToManyField(ProgramSubCategories)

    class Meta:
        db_table = 'teachers'
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f'{self.name} {self.phone}'
