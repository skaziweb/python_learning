# Generated by Django 4.2 on 2023-05-15 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('position', '0001_initial'),
        ('customer', '0004_rename_is_delete_customer_is_deleted'),
        ('schedule', '0011_remove_lecture_teachers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hologram', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер голограммы')),
                ('medical_book_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер медецинской книжки')),
                ('lecture_number_in_lmk', models.CharField(blank=True, max_length=1, null=True, verbose_name='Номер обучения в ЛМК')),
                ('first_lecture', models.BooleanField(default=False, verbose_name='Первичное обучение')),
                ('attestation_required', models.BooleanField(default=True, verbose_name='Требуется аттестация')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Пометка на удаление')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_customer', to='customer.customer')),
                ('lecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_lecture', to='schedule.lecture')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_lecture', to='position.position')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Внутренний пользователь')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'db_table': 'group',
            },
        ),
    ]
