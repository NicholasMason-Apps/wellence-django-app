# Generated by Django 5.1 on 2024-08-17 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_by',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 17, 18, 4, 40, 63263)),
        ),
    ]
