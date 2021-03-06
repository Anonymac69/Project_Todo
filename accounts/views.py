from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import SignUpForm, EditProfileForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import List
from .forms import ListForm


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            # messages.success(request, ('Item Has Been Added To List...'))
            return render(request, 'accounts/home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'accounts/home.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    # messages.success(request, ('Item Has Been Deleted!.'))
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Your Registration Was Successful...')
            return redirect('login')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, f'Hi {username}, You\'re Welcome, Click on "my todo" on the Dashboard to create & see your Todo List')
            return redirect('home')
        else:
            messages.success(
                request, 'Oops! Something is Wrong, Kindly Try Again...')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', {})


def edit_user(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(
                request, 'You Have Successfully Modified Your Profile...')
            return redirect('login')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'accounts/modify_user.html', context)


def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(
                request, 'You Have Successfully Changed Your Password...')
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'accounts/password.html', context)


def logout_user(request):
    logout(request)
    messages.success(
        request, 'You\'re now logged out, See you some other time...')
    return redirect('home')
