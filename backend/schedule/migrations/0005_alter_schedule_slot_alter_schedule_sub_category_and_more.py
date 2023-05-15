# Generated by Django 4.2 on 2023-05-15 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('educational_programs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0004_alter_schedule_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='slot',
            field=models.TimeField(verbose_name='Время начала'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_category', to='educational_programs.programsubcategories'),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_date', models.DateField(auto_now_add=True, verbose_name='Дата лекции')),
                ('attestation_date', models.DateField(verbose_name='Дата аттестации')),
                ('internal', models.BooleanField(default=True, verbose_name='Без выезда')),
                ('for_employees', models.BooleanField(default=True, verbose_name='Для сотрудников')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Пометка на удаление')),
                ('schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule', to='schedule.schedule')),
                ('teachers', models.ManyToManyField(to='teacher.teacher')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Внутренний пользователь')),
            ],
            options={
                'verbose_name': 'Lecture',
                'verbose_name_plural': 'Lectures',
                'db_table': 'lecture',
            },
        ),
    ]
