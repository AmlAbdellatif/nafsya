from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Artical(models.Model):
    pic=models.ImageField(upload_to='static/img',default='static/img/shattered.png')
    title=models.CharField(max_length=1000)
    content=models.CharField(max_length=10000)
    visit=models.URLField(max_length=2000)
    added_by=models.ForeignKey(User,related_name='Book',on_delete=models.CASCADE)
    def __str__(self):
        return self.title