from django.urls import path as url
from . import views


urlpatterns = [
    url('',views.index,name='index'),
    url(r'^authentication/$', views.register, name = 'register'),
 

]