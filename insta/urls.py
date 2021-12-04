# from django.conf.urls import  url,include
from django.urls import path
from django.contrib import admin
from insta import views



urlpatterns = [
    path('',views.index,name= 'index'),
    path('profile/', views.profile, name='profile'),


]