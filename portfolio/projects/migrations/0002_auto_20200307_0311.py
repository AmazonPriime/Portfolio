# Generated by Django 3.0.3 on 2020-03-07 03:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_updated',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]