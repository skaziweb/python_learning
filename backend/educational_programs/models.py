from django.db import models

from decorators.track_create_and_change import track_creation_and_change


# Create your models here.
@track_creation_and_change
class ProgramCategories(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название категории')
    code = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Код категории')

    class Meta:
        db_table = 'program_categories'
        verbose_name = "Program Category"
        verbose_name_plural = "Program Categories"

    def __str__(self):
        return f'{self.code} {self.title}'

@track_creation_and_change
class ProgramSubCategories(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название подкатегории')
    code = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Код подкатегории')
    category = models.ForeignKey(ProgramCategories, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'program_sub_categories'
        verbose_name = "Program SubCategory"
        verbose_name_plural = "Program SubCategories"

    def __str__(self):
        return f'{self.code} {self.title}'

