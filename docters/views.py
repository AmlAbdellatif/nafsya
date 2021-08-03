from django.shortcuts import render
from django.http import HttpResponse
from .models import Docter
# Create your views here.
def showdocters(request):
    doctor=Docter.objects.all()
    return render(request,'doctors.html',{'doctor':doctor})
