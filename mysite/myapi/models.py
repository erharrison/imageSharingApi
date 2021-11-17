from django.db import models


class ImagePost(models.Model):
    image = models.ImageField(upload_to='images')
    caption = models.TextField(max_length=100)
    author = models.CharField(max_length=30)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.caption
