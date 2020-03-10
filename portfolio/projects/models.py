from django.db import models
from datetime import datetime

class Project(models.Model):
    name = models.CharField(max_length = 128)
    description = models.TextField()
    language = models.CharField(max_length = 128)
    views = models.IntegerField(default = 0)
    url = models.URLField(default = "https://github.com")
    date_created = models.DateField(default = datetime.now)
    date_updated = models.DateField(default = datetime.now)

    def __str__(self):
        return self.name

class View(models.Model):
    viewer_id = models.CharField(max_length = 64)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
