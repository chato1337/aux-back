# Generated by Django 4.1 on 2022-08-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_organization_owner_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identifer',
            field=models.CharField(max_length=12, null=True),
        ),
    ]