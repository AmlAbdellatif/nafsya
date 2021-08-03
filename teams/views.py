from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from teams.models import Team


def showteam(request):
    team=Team.objects.all()
    return render(request,'team.html',{'team':team})
