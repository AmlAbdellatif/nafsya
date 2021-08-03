from django.db import models

# Create your models here.
class Team(models.Model):
    pic=models.ImageField(upload_to='static/img',default='static/img/shattered.png')
    name=models.CharField(max_length=1000)
    spcialztion=models.CharField(max_length=500)
    email=models.URLField(max_length=500)
    def __str__(self):
      return self.name