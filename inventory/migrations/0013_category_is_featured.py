# Generated by Django 4.1.7 on 2023-03-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
