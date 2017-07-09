from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html', {})


def authentication(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user and user.is_authenticated():
            login(request, user)
            return redirect(reverse('home'))
    return render(request, 'login.html', {})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect(reverse('home'))
    return render(request, 'signup.html', {})
