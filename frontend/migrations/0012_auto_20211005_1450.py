# Generated by Django 3.1.1 on 2021-10-05 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_auto_20211005_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 5, 14, 50, 39, 363667), verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='track',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 5, 14, 50, 39, 364666), verbose_name='date added'),
        ),
    ]
