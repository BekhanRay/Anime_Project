# Generated by Django 4.0 on 2023-05-15 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
