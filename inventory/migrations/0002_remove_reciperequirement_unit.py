# Generated by Django 5.1 on 2024-08-08 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reciperequirement',
            name='unit',
        ),
    ]
