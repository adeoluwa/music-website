# Generated by Django 3.1.1 on 2021-10-07 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_auto_20211006_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 7, 10, 15, 42, 543897), verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='track',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 7, 10, 15, 42, 544896), verbose_name='date added'),
        ),
    ]