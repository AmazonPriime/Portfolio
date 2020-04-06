# Generated by Django 3.0.3 on 2020-04-06 01:46

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('title_slug', models.SlugField(unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('views', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('date_updated', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewer_id', models.CharField(max_length=64)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
