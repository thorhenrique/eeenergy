# Generated by Django 2.1.1 on 2018-10-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_auto_20181030_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gasto',
            options={'get_latest_by': 'data'},
        ),
        migrations.AlterField(
            model_name='gasto',
            name='gasto',
            field=models.FloatField(default=0, verbose_name='Gasto em Reais'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='kw',
            field=models.FloatField(default=0, verbose_name="Kw's gastos"),
        ),
    ]