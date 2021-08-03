from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showhome(request):

    return render(request,'../templates/base.html')
