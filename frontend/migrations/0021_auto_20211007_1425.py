# Generated by Django 3.1.1 on 2021-10-07 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0020_auto_20211007_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterField(
            model_name='album',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 7, 14, 25, 0, 494328), verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='track',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 7, 14, 25, 0, 495328), verbose_name='date added'),
        ),
    ]
