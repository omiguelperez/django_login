from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^login/', views.authentication, name='authentication'),
    url(r'^signup/', views.signup, name='signup'),
]
