from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, default='General post', blank=False)
    content = models.CharField(max_length=255, default='Just saying Hi !')
    published = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)


