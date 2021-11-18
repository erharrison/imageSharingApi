from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class ImagePost(models.Model):
    image = models.ImageField(upload_to='images')
    caption = models.TextField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption


class User(models.Model):
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )
    username = models.TextField(max_length=30, blank=True, default="username")
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.username} Profile"
