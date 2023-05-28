# Generated by Django 4.1.7 on 2023-05-28 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0007_remove_dinnerorder_products_dinnerorder_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='orders',
        ),
        migrations.AlterField(
            model_name='table',
            name='total',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='table',
            name='orders',
            field=models.ManyToManyField(blank=True, to='dinner.dinnerorder'),
        ),
    ]
