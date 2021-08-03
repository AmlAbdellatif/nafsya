from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):

    name = models.CharField(max_length=150)
    pic=models.ImageField(upload_to='static/img',default='static/img/shattered.png')
    describtion = models.CharField(max_length=300)
    visit = models.FileField(upload_to='media')
    added_by = models.ForeignKey(User, related_name='download', on_delete=models.CASCADE)

    def __str__(self):
        return self.name