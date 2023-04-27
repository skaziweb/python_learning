from django.contrib import admin

from .models import ProgramCategories, ProgramSubCategories

# Register your models here.
admin.site.register(ProgramCategories)
admin.site.register(ProgramSubCategories)
