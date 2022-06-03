from django.db import models
from matplotlib.pyplot import title
from models.user.models import User

# Create your models here.

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)


    def __str__(self) :
        return self.title
