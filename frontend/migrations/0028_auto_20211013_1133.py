# Generated by Django 3.1.1 on 2021-10-13 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0027_auto_20211012_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 11, 33, 55, 608314), verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='track',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 11, 33, 55, 608314), verbose_name='date added'),
        ),
    ]
