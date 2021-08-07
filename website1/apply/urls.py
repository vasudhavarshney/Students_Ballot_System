from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import userinfo,application

urlpatterns = [
    path('',application),
    path('userinfo',userinfo)
]