from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'main/home.html')


def login_user(request):
    return render(request, 'accounts/login.html', {})
