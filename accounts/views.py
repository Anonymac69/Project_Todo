from django.shortcuts import render, redirect


def login(request):
    return render(request, 'accounts/login.html')
