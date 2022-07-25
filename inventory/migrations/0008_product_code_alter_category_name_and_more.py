# Generated by Django 4.0.6 on 2022-07-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_product_entry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='identifier',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]