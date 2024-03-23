from django.shortcuts import render
from .models import Gallery

# Create your views here.
def index(request):

    galls = Gallery.objects.all()

    return render(request,'sidebar.html',{'galls' : galls})

def images(request):

    return render(request,'images.html')