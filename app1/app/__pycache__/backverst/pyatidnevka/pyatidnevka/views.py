from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from pyatidnevka.models import *
from django.db import models

def index(request):
    return TemplateResponse(request, "index.html")

def personalaccount(request):
    return TemplateResponse(request, "personalaccount.html")

def add(request):
   fsku = request.POST.get("sku")
   fstrih = request.POST.get("strih")
   farticul = request.POST.get("articul")
   fNameTovara = request.POST.get("NameTovara")
   fBrendTovara = request.POST.get("BrendTovara")
   fOpisanie = request.POST.get("Opisanie")
   db = Order(SKU=fsku, Strih=fstrih, Articul=farticul, NameTovara=fNameTovara, BrendTovara=fBrendTovara, Opisanie=fOpisanie)
   db.save()
   return HttpResponseRedirect("http://127.0.0.1:8000/personalaccount")

def acc(request):
   zama = Order.objects.all()
   return TemplateResponse(request, "acc.html", context={"zamac":zama})



def register(request):
    return TemplateResponse(request, "register.html")

def newuser(request):
    flogin = request.POST.get("login")
    fpsswd = request.POST.get("password")
    # запись данных пользователя в db.sqlite3 (таблица auth_user)
    profile = User.objects.create_user(flogin, fpsswd)
    profile.save()
    return HttpResponseRedirect("http://127.0.0.1:8000/personalaccount")

def enter(request):
    return TemplateResponse(request, "enter.html")

# def acc(request):
#     return TemplateResponse(request, "acc.html")

def authuser(request):
    flogin = request.POST.get("login")
    fpsswd = request.POST.get("password")
    profile = authenticate(username=flogin, password=fpsswd)
    # если пользователь существует в таблице auth_user
    if profile is not None:
        # если пользователь активен
        if profile.is_active:
            # выполнить авторизацию
            login(request, profile)
            # выполнить перенаправление на страницу
            return HttpResponseRedirect("http://127.0.0.1:8000/personalaccount")
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/enter")

def authuserout(request):
    logout(request)
    return HttpResponseRedirect("http://127.0.0.1:8000")