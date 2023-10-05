from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from proyecto.views import *
from django.contrib.auth.views import LogoutView
from . import views
from .views import *

app_name = 'proyecto'

urlpatterns = [
    url(r'^$',filtrosv, name="fitrosv"),
]