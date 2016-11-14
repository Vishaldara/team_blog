from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("auth.User")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', blank=True, null=True)


    def published(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title




