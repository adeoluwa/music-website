# Generated by Django 3.1.1 on 2021-10-04 09:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20211004_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='album_of_genres',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='genre_album', to='frontend.album'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 4, 10, 23, 20, 714762), verbose_name='date added'),
        ),
    ]
