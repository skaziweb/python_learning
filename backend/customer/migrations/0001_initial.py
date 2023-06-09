# Generated by Django 4.2 on 2023-04-25 06:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=50, unique=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Электронная почта')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 25, 13, 24, 22, 368658))),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
    ]
