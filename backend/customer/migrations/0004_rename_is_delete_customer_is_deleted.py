# Generated by Django 4.2 on 2023-04-25 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customer_options_remove_customer_is_deleted_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='is_delete',
            new_name='is_deleted',
        ),
    ]
