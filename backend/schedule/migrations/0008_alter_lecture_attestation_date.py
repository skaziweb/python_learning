# Generated by Django 4.2 on 2023-05-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_alter_lecture_attestation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='attestation_date',
            field=models.DateField(null=True, verbose_name='Дата аттестации'),
        ),
    ]
