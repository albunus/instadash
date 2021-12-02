from django.conf.urls import url
from django.contrib import admin
from insta import views


urlpatterns = [
    url(r'^$',views.index,name= 'index'),

]