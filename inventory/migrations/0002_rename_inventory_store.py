# Generated by Django 3.2.6 on 2021-08-12 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inventory',
            new_name='Store',
        ),
    ]
