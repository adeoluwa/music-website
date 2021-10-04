# Generated by Django 3.1.1 on 2021-10-04 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20211004_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_member_names',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 4, 10, 26, 26, 510163), verbose_name='date added'),
        ),
    ]