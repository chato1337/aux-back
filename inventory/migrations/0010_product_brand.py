# Generated by Django 4.1.7 on 2023-03-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_product_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='generic', max_length=30),
        ),
    ]
