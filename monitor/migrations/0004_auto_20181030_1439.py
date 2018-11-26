# Generated by Django 2.1.1 on 2018-10-30 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_dica_pub_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dica',
            options={'get_latest_by': 'pub_data'},
        ),
        migrations.AddField(
            model_name='gasto',
            name='kw',
            field=models.FloatField(default=0, verbose_name='Voltagem gasta'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='data',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Data'),
        ),
    ]