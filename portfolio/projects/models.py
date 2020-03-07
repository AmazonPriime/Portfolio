from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 128)
    description = models.TextField()
    language = models.CharField(max_length = 128)
    views = models.IntegerField(default = 0)
    url = models.URLField(default = "https://github.com")
    date_created = models.DateField()
    date_updated = models.DateField()

    def __str__(self):
        return self.name
