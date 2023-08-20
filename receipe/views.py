from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *

def  index(request):
    load=loader.get_template('pro.html')
    return HttpResponse(load.render({},request))

def createuser(request):
    username=request.POST['user']
    email=request.POST['email']
    password=request.POST['password']
    data=User(username=username,email=email,password=password)
    data.save()
    return redirect('index')

def login(request):
    email=request.POST['email']
    password=request.POST['password']
    data=User.objects.filter(email=email)
    if data:
        data=User.objects.get(email=email)
        if data.password == password:
            load=loader.get_template('recipe.html')
            return HttpResponse(load.render({},request))
        else:
            return HttpResponse('password not match')
    else:
        return HttpResponse('User name not found')

def recipe(request):
    load=loader.get_template('recipe.html')
    return HttpResponse(load.render({},request))
