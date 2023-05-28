# Generated by Django 4.1.7 on 2023-05-28 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0006_alter_dinnerorder_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dinnerorder',
            name='products',
        ),
        migrations.AddField(
            model_name='dinnerorder',
            name='products',
            field=models.ManyToManyField(blank=True, to='dinner.dinnerproduct'),
        ),
    ]