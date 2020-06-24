from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# added password change stuff
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _


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
    if user is not None:  # username and password matched a user
        login(request, user)
        return HttpResponseRedirect(reverse('lg_app:index'))
    else:
        message = {
            "error": "Incorrect password, or you are not yet registered.",
        }
        # return HttpResponseRedirect(reverse('users:login_register'))
        return render(request, 'users/login.html', message)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login_register'))


# change password view

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _(
                'Your password was successfully updated!'))
            return redirect('accounts:change_password')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
