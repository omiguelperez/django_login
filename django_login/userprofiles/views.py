from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def authentication(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})

