from django.shortcuts import render
from .models import Gallery

# Create your views here.
def index(request):

    galls = Gallery.objects.all()

    return render(request,'sidebar.html',{'galls' : galls})

def images(request):

    galls = Gallery.objects.all()

    return render(request,'images.html',{'galls' : galls})

def videos(request):

    return render(request,'videos.html')