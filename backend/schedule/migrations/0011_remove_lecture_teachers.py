# Generated by Django 4.2 on 2023-05-15 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_alter_lecture_schedule_alter_schedule_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='teachers',
        ),
    ]
