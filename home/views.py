from django.shortcuts import render, reverse
from django.shortcuts import render, HttpResponseRedirect
import os, random
from pathlib import Path
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from django.conf.urls.static import static

# Create your views here.


def makePC(request):
    budget = request.GET.get('user_budget')
    budget = int(budget)
    print(budget)
    rind = random.randint(0, 1)
    if budget > 50000:
        fetchError = False

        mobo = Mobo.objects.filter(mPrice__lte = budget, isAmdorIntel = 0)
        mobop = Mobo.objects.filter(mPrice__lte = budget, isAmdorIntel = 0).values_list('mPrice',flat= True).first()
        budget = (budget-mobop)

        cpu = Processor.objects.filter(pPrice__lte = budget)
        cpup = Processor.objects.filter(pPrice__lte = budget).values_list('pPrice',flat= True).first()
        budget = budget - cpup

        ssd = SSD.objects.filter(sPrice__lte = budget)
        ssdp = SSD.objects.filter(sPrice__lte = budget).values_list('sPrice',flat= True).first()
        budget = budget - ssdp

        ram = Ram.objects.filter(rPrice__lte = budget)
        ramp = Ram.objects.filter(rPrice__lte = budget).values_list('rPrice',flat= True).first()
        budget = budget - ramp
        if budget > 0:
            gpu = GPU.objects.filter(gPrice__lte = budget)
            gpup = GPU.objects.filter(gPrice__lte = budget).values_list('gPrice',flat= True).first()
            budget = budget - gpup


        if len(cpu) < 0 or len(ram) < 0 or len(ssd) < 0 or len(mobo) < 0:
            fetchError = True
            context = {
                'fetchError': fetchError,
            }
        else:
            fetchError = False
            context = {
                'budget':budget,
                "mobo": mobo,
                'cpu': cpu,
                'ram': ram,
                'gpu': gpu,
                'ssd':ssd,
                'fetchError':fetchError,
            }
    else:
        fetchError = True
        context = {
            'fetchError': fetchError,
        }
    return render(request, 'makepc.html',context)

def getBudget(request):
    if request.method == "POST":
        budget = request.POST.get('user_budget')
        # makePC(budget, request)


def index(request):
    getBudget(request)
    return render(request, 'index.html')

def signin(request):
    getBudget(request)
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
    getBudget(request)
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


def pList(request):
    getBudget(request)
    items = Processor.objects.all()
    context = {
        'items': items,
    }  
    return render(request, 'cpulist.html', context)


def gList(request):
    getBudget(request)
    items = GPU.objects.all()
    context = {
        'items': items,
    }  
    return render(request, 'gpulist.html', context)


def rList(request):
    getBudget(request)
    items = Ram.objects.all()
    context = {
        'items': items,
    }  
    return render(request, 'rlist.html', context)


def sList(request):
    getBudget(request)
    items = SSD.objects.all()
    context = {
        'items': items,
    }  
    return render(request, 'slist.html', context)


def hList(request):
    getBudget(request)
    items = HDD.objects.all()
    context = {
        'items': items,
    }  
    return render(request, 'hlist.html', context)


def mList(request):
    getBudget(request)
    items = Mobo.objects.all()
    context = {
        'items': items,
    }  
    return render(request, 'mlist.html', context)


