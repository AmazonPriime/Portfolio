from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length = 128, unique = True)
    title_slug = models.SlugField(unique = True)
    content = RichTextField()
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    date_created = models.DateTimeField(default = datetime.now)
    date_updated = models.DateTimeField(default = datetime.now)

    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class View(models.Model):
    viewer_id = models.CharField(max_length = 64)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

class Like(models.Model):
    liker_id = models.CharField(max_length = 64)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
