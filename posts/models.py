from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=5000)
    image = image = models.ImageField(upload_to="posts/images/", blank=True, null=True)
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}'s post"