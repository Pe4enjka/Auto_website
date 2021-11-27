from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('enter', views.enter, name='enter'),
    path('', views.prev, name='prev'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
]