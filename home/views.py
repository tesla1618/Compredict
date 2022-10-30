from django.shortcuts import render, reverse
from django.shortcuts import render, HttpResponseRedirect
import os
from pathlib import Path
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from django.conf.urls.static import static

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == "POST":
        uname = request.POST['loginName']
        pwd = request.POST['loginPassword']

        user = authenticate(username = uname, password = pwd)

        if user is not None:
            passName = uname
            login(request,user)
            return redirect('home')
            
        else:
            messages.error(request, "Wrong Credentials!")
    context = {
        'thisPage':2,
        'urlpage':'login',
    }
    return render(request, 'login.html', context)

def reg(request):
    if request.method == "POST":
        username = request.POST['regName']
        pass1 = request.POST['regPassword1']
        pass2 = request.POST['regPassword2']
        email = request.POST['regMail']
        
        if pass1 != pass2:
            messages.error(request, "Re-typed password does not match!")
            return redirect('reg')

        if User.objects.filter(username=username):
            messages.error(request, "User with the same Name already exists! Please use a different UserID. Or you may use "+username+"123 or something else!")
            return redirect('reg')
        
        if ' ' in username:
            messages.error(request, "UserID must be a single string! For Example: wokewojak")
            return redirect('reg')

        else:
            password = pass1
            passName = username
            gbtusr = User.objects.create_user(username,email, password)
            gbtusr.save()
            # return render(request, 'profile.html', {'showName':passName})
            # return render(request, 'profile.html', {'showName':passName})
            messages.success(request, "Account creation was Successfull! Please Login to proceed.")
            return redirect('login')

    context = {
        'thisPage':3,
        'urlpage':'reg',
    }
    return render(request, 'reg.html', context)

def signout(request):
    logout(request)
    return redirect('home')