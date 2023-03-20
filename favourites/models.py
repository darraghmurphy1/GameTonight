from django.db import models
from django.contrib.auth.models import User
from social.models import Post


# Create your models here.
class Favourite(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favourite', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post} has been added to {self.user}'s favourites"
