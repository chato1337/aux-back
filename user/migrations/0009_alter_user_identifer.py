# Generated by Django 4.1 on 2022-08-11 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_id_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='identifer',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
    ]
