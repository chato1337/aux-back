# Generated by Django 4.0.6 on 2022-07-19 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='entry_date',
            field=models.DateField(auto_now=True),
        ),
    ]