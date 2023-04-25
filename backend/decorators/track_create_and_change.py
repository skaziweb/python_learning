from django.db import models
from django.contrib.auth.models import User

def track_creation_and_change(cls: models.Model):
    models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания').contribute_to_class(
        cls,
        name="created_at",
    )
    models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения').contribute_to_class(
        cls,
        name="updated_at",
    )

    models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Внутренний пользователь').contribute_to_class(
        cls,
        name="user",
    )
    models.BooleanField(
        default=False,
        verbose_name='Пометка на удаление').contribute_to_class(
        cls,
        name="is_deleted",
    )

    return cls