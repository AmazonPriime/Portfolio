from django.db import models
from datetime import datetime

class Language(models.Model):
    name = models.CharField(primary_key = True, max_length = 32)

    def __str__(self):
        return self.name

class Project(models.Model):
    project_id = models.CharField(primary_key = True, max_length = 128)
    name = models.CharField(max_length = 128)
    description = models.TextField()
    url = models.URLField(default = "https://github.com/amazonpriime")
    date_created = models.DateTimeField(default = datetime.now)
    date_updated = models.DateTimeField(default = datetime.now)
    language = models.ForeignKey(Language, on_delete = models.CASCADE)
    stars = models.IntegerField(default = 0)
    watchers = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class View(models.Model):
    viewer_id = models.CharField(max_length = 64)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)