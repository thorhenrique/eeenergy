# Generated by Django 2.1.1 on 2018-10-30 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20181030_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='dica',
            name='pub_data',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Data de publicacao'),
        ),
    ]
