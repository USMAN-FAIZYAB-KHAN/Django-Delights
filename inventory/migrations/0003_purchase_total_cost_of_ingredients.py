# Generated by Django 5.1 on 2024-08-08 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_reciperequirement_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='total_cost_of_ingredients',
            field=models.FloatField(default=0.0),
        ),
    ]
