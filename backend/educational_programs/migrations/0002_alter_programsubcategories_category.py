# Generated by Django 4.2 on 2023-05-15 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('educational_programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programsubcategories',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_sub_category', to='educational_programs.programcategories'),
        ),
    ]
