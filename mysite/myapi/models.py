from django.db import models
from django.contrib.auth.models import AbstractUser


class ImagePost(models.Model):
    image = models.CharField(max_length=60)
    caption = models.TextField(max_length=100)
    author = models.CharField(max_length=30)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.image


class User(AbstractUser):
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )
    bio = models.TextField(max_length=200, blank=True, default="Bio")
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.username} Profile"
