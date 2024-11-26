from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personalaccount/add/', views.add, name="add"),
    path('personalaccount/', views.personalaccount, name="personalaccount"),
    path('personalaccount/acc/', views.acc, name="acc"),
    path('personalaccount/authuserout/', views.authuserout),
    path('enter/', views.enter, name="enter"),
    path('enter/authuser/', views.authuser),
    path('enter/register/', views.register, name="register"),
    path('enter/register/newuser/', views.newuser),
    path('', views.index, name="index"),
]