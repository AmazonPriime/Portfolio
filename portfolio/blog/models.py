from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length = 128, unique = True)
    title_slug = models.SlugField(unique = True)
    content = models.TextField()
    date_created = models.DateField(default = datetime.now)
    date_updated = models.DateTimeField(default = datetime.now)

    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class View(models.Model):
    viewer_id = models.CharField(max_length = 64)
    title = models.ForeignKey(Post, on_delete = models.CASCADE)

class Like(models.Model):
    liker_id = models.CharField(max_length = 64)
    title = models.ForeignKey(Post, on_delete = models.CASCADE)
