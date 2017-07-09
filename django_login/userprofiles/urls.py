from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import reverse

from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^login/', views.authentication, name='authentication'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^logout/', auth_views.logout, {'next_page': '/login/'}, name='logout'),
]
