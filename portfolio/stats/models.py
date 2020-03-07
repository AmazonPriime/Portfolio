from django.db import models

class Visitor(models.Model):
    visitor_id = models.CharField(max_length = 64)
