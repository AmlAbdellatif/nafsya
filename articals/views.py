from django.shortcuts import render
from django.http import HttpResponse
from .models import Artical
# Create your views here.
def viewarticals(request):
    artical=Artical.objects.all()
    return render(request,'articals.html',{'artical':artical})