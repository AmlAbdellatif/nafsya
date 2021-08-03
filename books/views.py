import os
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Book
from django.conf import settings
# Create your views here.
def showbooks(request):
    book=Book.objects.all()
    return render(request,'books.html',{'book':book})


def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/visit")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404
