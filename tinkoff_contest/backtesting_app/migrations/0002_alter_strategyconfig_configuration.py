# Generated by Django 4.0.4 on 2022-05-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtesting_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategyconfig',
            name='configuration',
            field=models.JSONField(blank=True, default={'Empty': 'Empty'}),
        ),
    ]
