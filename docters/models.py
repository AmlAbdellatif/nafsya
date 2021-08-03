from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Docter(models.Model):
    pic=models.ImageField(upload_to='static/img',default='static/img/shattered.png')
    name=models.CharField(max_length=100)
    specizaltion=models.CharField(max_length=500)
    email=models.URLField(max_length=50)
    added_by=models.ForeignKey(User,related_name="doctor",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
