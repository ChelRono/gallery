from django.shortcuts import render
from .models import Gallery

# Create your views here.
def index(request):

    gall1 = Gallery()
    gall1.name = 'Hello there'
    gall1.desc = 'This is hello world'
    gall1.img = 'flower1.jpeg'

    gall2 = Gallery()
    gall2.name = 'Hello world'
    gall2.desc = 'This is hello world'
    gall2.img = 'mountain.jpeg'

    gall3 = Gallery()
    gall3.name = 'Hello Kenya'
    gall3.desc = 'This is hello world'
    gall3.img = 'flower1.jpeg'

    gall4 = Gallery()
    gall4.name = 'Hello Kenya'
    gall4.desc = 'This is hello world'
    gall4.img = 'flower1.jpeg'

    galls = [gall1,gall2,gall3,gall4]


    return render(request,'sidebar.html',{'galls' : galls})
