from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth

from django.core.context_processors import csrf

from django.shortcuts import render_to_response, render, redirect
from account.forms import *

#Import a user registration form

# User Login View

def junk(request):
	return HttpResponse("hello account")

def login_form(request):
    return render(request, 'account/login_form.html')

def user_login(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect(request.GET.get('next','/'))
    return render(request, 'account/login_form.html', {'form': form })


# User Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# User Register View
def user_register(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('User created succcessfully.')
        else:
            form = UserRegisterForm()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('account/register.html', context)
    else:
        return HttpResponseRedirect('/')
