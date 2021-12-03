from django.conf.urls import url, include
from django.contrib import admin
from insta import views
from django.urls import re_path,path


urlpatterns = [
    path('',views.index,name= 'index'),
    path(r'^accounts/', include('registration.backends.simple.urls')),

]