from django.db import models
from datetime import datetime


class ImagePost(models.Model):
    # class defining the model for a post of an image
    image = models.ImageField(upload_to='images')
    caption = models.TextField(max_length=100)
    author = models.CharField(max_length=30)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    upload_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.caption


class User(models.Model):
    # class defining a user of the app
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )
    username = models.TextField(max_length=30, blank=True, default="username")
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.username} Profile"
