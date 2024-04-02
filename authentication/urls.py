from django.urls import path as url
from . import views


urlpatterns = [
    url(r'^authentication/$', views.register, name = 'register'),
 

]