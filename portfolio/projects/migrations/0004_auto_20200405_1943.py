# Generated by Django 3.0.3 on 2020-04-05 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]