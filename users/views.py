from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_register(request):
    context = {}
    return render(request, 'users/login.html', context)


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    
    if User.objects.filter(username=username).exists():
        message = {
            "error": "Username and/or email are already taken.",
        }
        return render(request, 'users/login.html', message)
        # return HttpResponseRedirect(reverse('users:login_register'))
    else:    
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return HttpResponseRedirect(reverse('lg_app:index'))
    
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None: # username and password matched a user
        login(request, user)
        return HttpResponseRedirect(reverse('lg_app:index'))
    else:
        return HttpResponseRedirect(reverse('users:login_register'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login_register'))